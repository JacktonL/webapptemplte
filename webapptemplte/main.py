from mongoengine import *

connect('webapp')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
