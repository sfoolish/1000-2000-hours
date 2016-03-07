# http://api.mongodb.org/python/current/tutorial.html

import datetime

from pymongo import MongoClient
from pymongo import ASCENDING
from bson.objectid import ObjectId

client = MongoClient("mongodb", 27017)

db = client.test_database

# An important note about collections (and databases) in MongoDB is that they
# are created lazily - none of the above commands have actually performed any
# operations on the MongoDB server. Collections and databases are created when
# the first document is inserted into them.
collection = db.test_collection

post = {
	"author": "Mike",
	"text": "My first blog post!",
	"tags": ["mongodb", "python", "pymongo"],
	"date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print post_id

post = {
	"author": "SF",
	"text": "My first blog post!",
	"tags": ["mongodb", "python", "pymongo"],
	"date": datetime.datetime.utcnow()
}
post_id = posts.insert_one(post).inserted_id
print "post_id raw: %r" % post_id
print "post_id: %s " % str(post_id)
str_post_id = str(post_id)

db.collection_names(include_system_collections=False)

print "Getting a Single Document With: %r" % posts.find_one()
print "Getting a Single Document With: %r" % posts.find_one({"author": "SF"})

print "Querying By ObjectId:%r %r" % (post_id, posts.find_one({"_id": post_id}))

# Note that an ObjectId is not the same as its string representation
# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = db.posts.find_one({'_id': ObjectId(post_id)})
    return document

print "Querying By ObjectId: %r" % get(str_post_id)

print "Total posts count: %d " % posts.count()


# how to create a unique index

result = db.profiles.create_index([('user_id', ASCENDING)],
                                   unique=True)

list(db.profiles.index_information())

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]

result = db.profiles.insert_many(user_profiles)
print "profiles user 211, 212: %r inserted_ids %r" % (result, result.inserted_ids)

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
print "profiles user 213: %r inserted_id %s" % (result, result.inserted_id)
result = db.profiles.insert_one(duplicate_profile)
print "Duplicate proile: % r" % result

