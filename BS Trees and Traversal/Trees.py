""""""
"""
---Problem---
We need to create a data structure which can store 100 million records and perform 
insertion, search, update and list operations efficiently.

---Input---
The key inputs to our data structure are user profiles, which contain the username, 
name and email of a user.

A Python class would be a great way to represent the information for a user. A class is 
a blueprint for creating objects. Everything in Python is an object belonging to some 
class. Here's the simples possible class in Python, with nothing in it:
"""

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        # print(f'Welcome {name}!')

    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"

    def __str__(self):
        return self.__repr__()
    # def introduce_yourself(self, guest_name):
    #     print(f"Hi {guest_name}, I'm {self.name}!. Contact me at {self.email} :)")

touseef = User('rainyjoke', 'Touseef Ahmed', 'touseefahmed0707@gmail.com')
habiba = User('habiba.ak_5', 'Habiba Akter Nupur', 'habibaakter0707@gmail.com')
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [touseef, habiba, aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
# print(user1)
# print(user1.name, user1.username, user1.email)
# user1.introduce_yourself('Tahseen')

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # find the first username greater than the new users username
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

database = UserDatabase()

database.insert(touseef)
database.insert(habiba)
database.insert(sonaksh)

# print(database.list_all())

# database.update(User(username='sonaksh', name='Sonaksh U', email='blabla@gmail.com'))
# print(database.find('sonaksh'))

