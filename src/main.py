from pymongo import MongoClient
from bson.objectid import ObjectId
#Connect to database
client = MongoClient('mongodb://localhost:27017')
#get the collection
grades = client.tracker.grades


#for _ in range(3):
 #   name = input('student name:')
  #  klass = input('student class:')
   # grade = float(input('grade:'))
    #d = {'name': name, 'klass': klass, 'grade': grade}

#insert only one value
#grades.insert_one(d)

total = 0
count = grades.find().count()
for g in grades.find():
    total += g['grade']
print(total / count)
