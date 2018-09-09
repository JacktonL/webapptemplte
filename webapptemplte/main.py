from mongoengine import *

connect('webapp')

b = 1

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
clemente = User(email='clemente@example.com', first_name='Clemente', last_name='Ferrer').save()
