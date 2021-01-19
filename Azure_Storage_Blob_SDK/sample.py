import os
from azure.storage import blob
from azure.storage.blob import BlockBlobService

connect_str = "DefaultEndpointsProtocol=http;BlobEndpoint=http://192.168.1.61:11002/azureblob;AccountName=azureblob;AccountKey=Q2w5lphZL7GsCPmX6163FaVGtnaATqJ2uXfuT+zmRCG3PVcwjtOZu8uYtdEM0u0WCI6YTO2Iy6aBb9O1ZYH0sg==;"

data = "2019-04-17"

def create_container(blob_client_name, container_name):
    try:
        blob_client_name.create_container(container_name)
    except Exception as e:
        print(e)

def upload_file(blob_client_name, container_name, path, filename):
    try:
        fullpath_to_file = os.path.join(path, filename)
        print(fullpath_to_file)
        blob_client_name.create_blob_from_path(
            container_name, filename, fullpath_to_file
        )
    except Exception as e:
        print(e)

def list_blobs(blob_client_name, container_name):
    try:
        print("\nList blobs in the container")
        generator = blob_client_name.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    filepath = r'C:\Users\alex\Downloads'
    file = 'flower.png'
    container_name = 'azuresdk21'

    blob_client = BlockBlobService(connection_string=connect_str)

    '''
    #Create Blob
    try:
        create_container(blob_client, container_name)
    except Exception as e:
        print(e)
    '''

    '''
    #Upload File
    try:
        upload_file(blob_client, container_name, filepath, file)
    except Exception as e:
        print(e)
    '''

    #List Blob
    try:
        list_blobs(blob_client, container_name)
    except Exception as e:
        print(e)    
