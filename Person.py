class Person:
    def __init__(self, name):
        self.name = name
        self.number_of_friends = 0
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
        self.number_of_friends += 1

    def get_name(self):
        return self.name

    def get_friend_cont(self):
        return self.number_of_friends

    def get_friends(self):
        return self.friends

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
