from utility.Generate_DDL_and_DMLs import generate_dml, generate_ddl
from utility.data_generation import create_dummy_data
from utility.read_from_gsheets import read_from_gsheets
import chromadb

df, expected_headers, table_name, table_values,document = read_from_gsheets()
print ("READ DONE")
data, table_name, ddl = generate_ddl(df)
print ("DDL done")
dml = generate_dml(data, table_name)
print ("DML done")

# chroma run --path /Users/hardikgoel/PycharmProjects/Custom_ingestion_LLM/db  --- to run chromadb
client = chromadb.HttpClient(host='localhost', port=8000)
collection = client.get_or_create_collection(name="E_Commerce")
# client.delete_collection(name="E_Commerce")
print (collection.count())
print (collection.peek())
print ("**************")
embeddings, metadatas, ids = create_dummy_data()
collection.add(documents=document, embeddings=embeddings, metadatas=metadatas, ids=ids)
print (collection.peek())








#
# client.execute(ddl)
# print ("EXECUTION DONE")
# for statement in dml:
#     client.execute(statement)
#
# print ("Fetching from chromadb")
# check_data(client, "E_Commerce")





