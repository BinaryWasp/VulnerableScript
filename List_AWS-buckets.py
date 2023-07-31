import boto3

def list_s3_buckets(access_key, secret_key, session_token):
       s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token
    )

    try:
        # List all S3 buckets
        response = s3.list_buckets()

        if 'Buckets' in response:
            print("List of S3 Buckets:")
            for bucket in response['Buckets']:
                print(bucket['Name'])
        else:
            print("No S3 buckets found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    access_key_id = "ASIATA4J3YYDJSRUJQNY"
    secret_access_key = "es8ljwR2AdAdj9THAQCjC6v3FqJ6MMhZMVnPphkDn"
    session_token = "lQoJb3JpZ2luX2VjEPT//////////wEaCXVzLWVhc3QtMSJHMEUCIQCsjZ0W"

    list_s3_buckets(access_key_id, secret_access_key, session_token)
