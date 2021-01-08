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

    def get_friend_count(self):
        return self.number_of_friends

    def get_friends(self):
        return self.friends

    def is_connected(self, target, visited=[]):

        if target in self.get_friends():
            return True
        else:
            visited.append(self)
            for friend in self.get_friends():
                if friend not in visited:
                    if friend.is_connected(target, visited):
                        return True
            return False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
