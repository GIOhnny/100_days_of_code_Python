class User:
    #pass  ==> black class
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
user_2.follow(user_1)

