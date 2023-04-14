"""
Ingestion JOB
"""

from urllib.request import urlretrieve
import boto3
import urllib.request
from urllib.error import ContentTooShortError
import os
import json
import sys
sys.path.insert(0, './config')
from config.aws import LANDING_BUCKET
import requests
import zipfile
import glob

def s3_upload(bucket_name, source_file_path, destination_file):
  s3_client = boto3.client('s3')
  s3_client.upload_file(source_file_path, bucket_name, destination_file)
  print(f"file: {destination_file} uploaded to bucket: {bucket_name} successfully")


if __name__ == "__main__":
  print("Starting Job")
  SOURCE_URLS = os.getenv("SOURCE_URLS", "[]")
  print(f"{SOURCE_URLS}")
  urls = json.loads(SOURCE_URLS)
  print(f"Total files to extract: {len(urls)}")
  for url in urls:
    file_name = url.split("/")[-1]
    print(f"o nome do arquivo eh {file_name}")

    r = requests.get(url, verify=False)
    open(file_name, 'wb').write(r.content)

    print("terminei de baixar o arquivo")

    print("estou na pasta:")
    os.system('pwd')
    os.system('ls -lrt')
    
    with zipfile.ZipFile(f"/src/{file_name}", "r") as zip:
      zip.extract("DADOS/MICRODADOS_ENEM_2020.csv")

    print("terminei de descompactar o arquivo")

    print("Sending to S3")
    s3_upload(LANDING_BUCKET, "/src/DADOS/MICRODADOS_ENEM_2020.csv", f"enem/MICRODADOS_ENEM_2020.csv")
  print("Done!")