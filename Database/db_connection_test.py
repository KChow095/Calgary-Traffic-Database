import ssl
from pymongo import MongoClient

''' connects to the MongoDB machine cluster

- admin:admin is the username:password for the database
- calgary_traffic_db is the name of the database

I had to import ssl and set the certificate to none in order to connect to MongoDB. Maybe you guys can remove these
parameters and see if you get an error connecting or not
'''

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.s0bw3.mongodb.net/calgary_traffic_db?retryWrites=true&w=majority", ssl=True,
                      ssl_cert_reqs=ssl.CERT_NONE)

# name of the database
db = cluster["calgary_traffic_db"]
# name of the collection
collection = db["zTest"]


''' testing MongoDB connection

MongoDB is not a relational database, rather it stores data in a key-value pairing like in a dictionary and stores the
dictionary into the database. In a traditional relational database we would store the data in rows but in a MongoDB 
database the dictionary objects represent the rows and are called 'documents'

Example: Change the "name" value to your name and see if you can write to the database
'''
#
document = {"name":"justin", "num":7}

# writing to the database
collection.insert_one(document)


# reading from the database
results = collection.find({"name":"justin"})

for res in results:
    print(res["name"], res["num"])
