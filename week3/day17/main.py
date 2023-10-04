class Users:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
# self.followers = 0 is default and doesnt need to be add when creating a user
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self. following += 1


# Making new users
user_1 = Users("001", "test name 1")
print(user_1.username)
print(user_1.id)

user_2 = Users("002", "test name 2")
print(user_2.username)
print(user_2.id)

user_1.follow(user_2)

print("followers stuff")
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
