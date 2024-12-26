from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#uri
uri="mongodb+srv://raunak:7614@cluster0.gfxyh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to new server
client=MongoClient(uri)

#create a database name and collection name
DATABASE_NAME="first_project"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\dhruv\Downloads\sensor fault\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)