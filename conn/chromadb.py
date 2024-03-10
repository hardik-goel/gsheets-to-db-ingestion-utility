import chromadb
from chromadb.config import Settings

#DEPRECATED

def conn_create():
    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                      persist_directory="db/"
                                      ))
    collection = client.create_collection(name="E_Commerce")
    return client, collection

