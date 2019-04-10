import mongoengine
from mongoengine import connect
#
# conn = connect(
#         db='test',
#         username='Siva_60',
#         password='12345',
#         host='mongodb://admin:qwerty@localhost/production'
#     )
#


client = mongoengine.connect("mongodb+srv://Siva_60:Siva@11160@cluster0-60b2o.gcp.mongodb.net/test?retryWrites=true")
# my_db = client["test"]
dblist = client.list_database_names()
for item in dblist:
    print(item)

if 'test' in dblist:
    print("yes")
else:
    print("No")