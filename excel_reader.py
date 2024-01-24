import pandas as pd
import redis
import sys
from datetime import datetime

# Read data from Excel file
adv_no = sys.argv[1]  # Replace with your Excel file path
file_path = sys.argv[2] 
data = pd.read_excel(file_path)

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Store data in Redis
for index, row in data.iterrows():
    advtno = f"{adv_no}-{row['RollNo']}"

    # print( row['advtno'], row['RollNo'], row['AdvtYear'], row['ExamDist'], row['RollNo'])
    print("========================", advtno , str(datetime.strftime(row['BirthDate'], '%Y-%m-%d')))
    redis_client.hset(advtno, 'advtno', str(row['advtno']))
    redis_client.hset(advtno, 'AdvtYear', str(row['AdvtYear']))
    redis_client.hset(advtno, 'ExamDist', str(row['ExamDist']))
    redis_client.hset(advtno, 'RollNo', str(row['RollNo']))
    redis_client.hset(advtno, 'BirthDate', str(datetime.strftime(row['BirthDate'], '%Y-%m-%d')))
    redis_client.hset(advtno, 'PRESENT_ABSENT', str(row['PRESENT_ABSENT']))

print("Data stored in Redis.")