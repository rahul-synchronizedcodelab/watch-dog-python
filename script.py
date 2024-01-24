import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from s3_client import s3_client
import sys
import redis

advno = sys.argv[1]
directory_to_watch =  sys.argv[2]

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

class FileCreationHandler(FileSystemEventHandler):

    def get_(self, file_path):
        print("*"*9, file_path)
        path_parts = file_path.split('/')

        # Extract the last two parts to get the dynamic values
        value1 = path_parts[-4] if len(path_parts) >= 4 else None
        value2 = path_parts[-1].split('.')[0] if len(path_parts) >= 1 else None

        return (value1, value2)
    
    def get_redis_data(self, adv_no, roll_no):
        advtno_to_retrieve = f'{adv_no}-{roll_no}'  # Replace this with the advtno you want to fetch

        # Get data from Redis for the specified key
        data = redis_client.hgetall(advtno_to_retrieve)

        # If data is found for the specified key
        if data:
            decoded_data = {key.decode(): value.decode() for key, value in data.items()}
            return decoded_data
        else:
            return None

    def on_created(self, src_path):
        path = src_path
        key =  path.split(f'{directory_to_watch}/', 1)[-1]

        adv_no, roll_no = self.get_(path)
        redis_data=self.get_redis_data(adv_no, roll_no)
        if redis_data:
            redis_key = f"{advno}-{redis_data.get('RollNo')}-{redis_data.get('BirthDate')}"
            print("-"*9, redis_key )
            s3_url = s3_client.upload_file(path, key)
            redis_client.set(redis_key, s3_url)

# if __name__ == "__main__":
#     event_handler = FileCreationHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path=directory_to_watch, recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()

#     observer.join()



def list_files(directory_path):
    if not os.path.isdir(directory_path):
        print("The provided path is not a directory.")
        return
    
    print(f"Listing files in directory: {directory_path}")
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            FileCreationHandler().on_created(file_path)


if __name__ == "__main__":
    list_files(directory_to_watch)