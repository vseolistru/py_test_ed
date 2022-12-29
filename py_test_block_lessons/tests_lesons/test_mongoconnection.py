import pymongo



client = pymongo.MongoClient('localhost', 27017)
#db = ski-commerce.orders
db = client['ski-commerce']

for i in db.orders.find({'id':'636434dcaabc25592fe31a03'}):
    print(i)



print(db.orders.find({'_id':'636434dcaabc25592fe31a03'}))


