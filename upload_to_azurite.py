from azure.storage.blob import BlobServiceClient
import os
 
CONNECT_STR = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;""AccountKey=Eby8vdM02xNOcqFlqCnrC4xYv1tEFcMFB3ZFNOZ5rIFvZZfeNm0Q7kBblK5xAn+Wy5Bv37Zm3qhGlaHQzH0Pdg==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)
 
CONTAINER_NAME = "datasets"
CSV_PATH = "/home/useruser/serverless_function/All_Diets.csv"
 
def upload_csv():
    client = BlobServiceClient.from_connection_string(CONNECT_STR)
 
    container_client = client.get_container_client(CONTAINER_NAME)
    try:
        container_client.create_container()
        print(f"Container '{CONTAINER_NAME}' created.")
    except Exception:
        print(f"Container '{CONTAINER_NAME}' already exists.")
 
    blob_client = container_client.get_blob_client("All_Diets.csv")
    with open(CSV_PATH, "rb") as f:
        blob_client.upload_blob(f, overwrite=True)
    print("All_Diets.csv uploaded to Azurite successfully!")
 
upload_csv()