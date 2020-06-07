import mongoengine
from mongoengine import connect



client = mongoengine.connect("mongodb+srv://<user_name>:<password>@cluster0-60b2o.gcp.mongodb.net/test?retryWrites=true")
# my_db = client["test"]
dblist = client.list_database_names()
for item in dblist:
    print(item)

if 'test' in dblist:
    print("yes")
else:
    print("No")
