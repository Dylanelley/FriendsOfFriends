import random
from Person import Person


def generate_people_with_friends(number_of_people, max_friends, min_friends):
    # how many poeple to generate
    people = []


    # create instances of person class to fill people list
    file = open("RandomNames.txt", "r")
    for i in range(number_of_people):
        people.append(Person(file.readline().rstrip("\n")))

    file.close()

    # Randomize who is friends with who
    for i in range(number_of_people):
        number_of_friends = random.randint(min_friends, max_friends)
        illegal_friends = [i]
        for j in range(number_of_friends):
            friend_number = i
            while friend_number in illegal_friends:
                friend_number = random.randint(0, number_of_people - 1)

            people[i].add_friend(people[friend_number])
            illegal_friends.append(friend_number)



    for person in people:
        print(person,person.get_friend_cont(), person.get_friends())


generate_people_with_friends(100, 50, 1)