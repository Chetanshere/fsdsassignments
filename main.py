import pymongo
client = pymongo.MongoClient("mongodb+srv://chetanshere24:shere1234@cluster0.sqdy6as.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name": "Chetan",
     "surname":"Shere",
     "email": "chetanshere24@gmail.com"}
g= {"name": "Chetan",
   "surname": "Shere",
   "email": "chetanshere24@gmail.com"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )