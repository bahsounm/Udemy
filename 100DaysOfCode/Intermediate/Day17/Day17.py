# Creating our own classess our own blue prints
# Class names are Pascal naming, each word is Captialized
# Camel case is is first isnt bt rest are captialized (not really used)
# snake case us the underscore


class User:

    # initilize function, called everytime we create a new object from this class
    def __init__(self, id="N/A", username="N/A", password="N/A"):
        self.id = id
        self.username = username
        self.password = password

    def set_username(self, new_name):
        self.username = new_name

    def get_username(self):
        return self.username




user1 = User("ABC123", "John", "****")

print(user1.get_username())

user1.set_username("Jerry")

print(user1.get_username())