import pymongo
from pymongo import MongoClient
Client=pymongo.MongoClient("localhost",27017);
print(Client.list_database_names())
db=Client.bookdb
print(db.list_collection_names())
from pprint import pprint
import pandas as pd
CM = [data for data in db.products.find()]
df_CM = pd.DataFrame(CM)
pprint(df_CM)