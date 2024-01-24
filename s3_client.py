import boto3
import settings

# S3 bucket and file information


class S3Client:

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name=settings.AWS_REGION)
    
    def upload_file(self, file_path, file_name):

        with open(file_path, 'rb') as file_data:
            response = self.s3.put_object(Bucket=settings.BUCKET_NAME, Key=file_name, Body=file_data)
            return f"https://{settings.BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{file_name}"


s3_client = S3Client()