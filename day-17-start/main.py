# Learning about class initialization
class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User(1, "Hrk")
user_2 = User(2, "lar")
user_3 = User(3, "Coc")

user_2.follow(user_3)
user_3.follow(user_2)

print(user_1.username, user_1.id, user_1.following)
print(user_2.username, user_2.id, user_2.following)
print(user_3.username, user_3.id, user_3.following)