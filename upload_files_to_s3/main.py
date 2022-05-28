import os
import boto3

if __name__ == '__main__':

    s3 = boto3.client('s3')

    dir_path = 'C:\\path\\for\\test\\'

    s3_bucket = 'teste987654321'
    s3_prefix = 'teste_dataset'

    dir_walk = os.walk(dir_path)
    for root, dirs, files in dir_walk:
        for name in files:
            local_file_name = os.path.join(root, name)
            file_name = local_file_name.replace('C:\\path\\for\\test\\', '').replace('\\', '/')
            final_name = '/'.join([s3_prefix, file_name])
            s3.upload_file(local_file_name, s3_bucket, final_name)
