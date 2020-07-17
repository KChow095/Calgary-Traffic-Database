import ssl
from pymongo import MongoClient

# link to MongoDB cluster
cluster = MongoClient("mongodb+srv://admin:admin@cluster0.s0bw3.mongodb.net/calgary_traffic_db?retryWrites=true&w=majority", ssl=True,
                      ssl_cert_reqs=ssl.CERT_NONE)

# name of the database and collection to read/write to
db = cluster["calgary_traffic_db"]
collection = db["zTest"]

# this is the object you will write to the db, change the name to your name for testing
document = {"name":"justin", "num":7}

# writing to the database
collection.insert_one(document)

# reading from the database
results = collection.find({"name":"justin"})

for res in results:
    print(res["name"], res["num"])

