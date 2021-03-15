import pymongo
client = pymongo.MongoClient(
   "mongodb+srv://m220student:m220password@sandbox.4wx90.mongodb.net/test?retryWrites=true&w=majority")
db = client.test