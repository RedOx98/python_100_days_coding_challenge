class User:
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow_account(self, user):
        user.followers+=1
        self.following += 1

user_1 = User("olahammed",  2000)
user_2 = User("Angela Yu",  2000)
user_1.follow_account(user_1)
user_1.follow_account(user_2)

# print(user_1.username, user_1.id, user_1.followers)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_1.following)