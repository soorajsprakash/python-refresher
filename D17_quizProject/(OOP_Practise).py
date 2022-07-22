class User:
    def __init__(self, user_ID, userName):
        self.userId = user_ID
        self.username = userName
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

def report():
    print(f"User1 followers: {user1.followers}")
    print(f"User1 following: {user1.following}")
    print(f"User2 followers: {user2.followers}")
    print(f"User2 followers: {user2.following}")
    print("------------------")


user1 = User("001", "User 1")
user2 = User("002", "User 2")

user1.follow(user2)
report()
# user2.follow(user2)
# report()
