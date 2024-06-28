
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
import pymongo


uri = "mongodb+srv://root:test1234@mongopractice.euq01ts.mongodb.net/?retryWrites=true&w=majority&appName=MongoPractice"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.mywebsite
collection = db.users

data1 = {'name':'archer', 
         'gender':'male',
         'email':'archer@gmail.com',
         'password':'archer',
         'level':3
         }

data2 = {'name':'ann', 
         'gender':'female',
         'email':'ann@gmail.com',
         'password':'ann',
         'level':1
         }

data3 = {'name':'tom', 
         'gender':'male',
         'email':'tom@gmail.com',
         'password':'tom',
         'level':0
         }

data4 = {'name':'peter', 
         'gender':'male',
         'email':'peter@gmail.com',
         'password':'peter',
         'level':5
         }


try:
    

    # 新增一筆資料
    # collection.insert_one(data1) 

    # 取得第二筆資料的id
    # result=collection.insert_one(data2)
    # print(result.inserted_id)
    
    # 新增多筆資料
    # result=collection.insert_many([data1, data2, data3, data4])
    # print(result.inserted_ids)



     # 查
    # 取得第一筆資料
    # data=collection.find_one()
    # print(data)

    # 利用 ObjectId 取得指定資料
    # ObjectId 雖然看起來像字串，但本質上是物件
    # data=collection.find_one(ObjectId('66583213d430521b0ed6e8a7'))
    # print(data)

    #  一次取得多筆資料，並且搭配迴圈印出來
    # cursor=collection.find()
    # print(cursor)

    # for doc in cursor:
    #     print(doc)

    criteria={'email':'peter@gmail.com'}
    newPassword={'password':'test'}
    description={'introduction':'hello, i am peter'}
    levelUp={'level':10}
    jump={'level':3}
    operation=['$set', '$unset', '$inc', '$mul']
    

    # result = collection.update_one(
    #     criteria,
    #     {operation[2]:jump}
    # )

    # print('docs matched', result.matched_count)
    # print('docs modified', result.modified_count)


    
    # 改
    # criteria2={'gender':'male'}
    # result2 = collection.update_many(
    #     criteria2,
    #     {operation[0]:levelUp}
    # )
    # print('docs matched', result2.matched_count)
    # print('docs modified', result2.modified_count)


    # 刪
    # criteria3 ={'level':10}
    # result3 = collection.delete_many(
    #     criteria3,
    # )
    
    # print('docs modified', result3.deleted_count)


    # 複合條件篩選資料
    # userAccount=[{'email':'archer@gmail.com'},{'password':'archer'}]
    # doc=collection.find_one(
    #     {'$and':userAccount}
    # )
    # print(doc)



    # 篩選並且排序

    cursor=collection.find(
        {
        '$or':[{'level':3},{'gender':'female'}]
        },
        sort=[
            ('level', pymongo.DESCENDING)
        ]
    )
    for record in cursor:
        print(record['name'])
        print(record)









except Exception as e:
    print(e)
