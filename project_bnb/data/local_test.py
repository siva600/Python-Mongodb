from mongoengine import *
import datetime
conn = connect('mongoengine_test', host='localhost', port=27017)

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=200)
    published = DateTimeField(default=datetime.datetime.now())


post1 = Post(
    title = "sample post",
    content = "tutorial content",
    author = "Siva"
)

post1.save()
print(post1.title)