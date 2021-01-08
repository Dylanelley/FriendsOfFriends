import random
from Person import Person


# generates grapth where nodes are people and edges are friends
def generate_people_with_friends(number_of_people, max_friends, total_connections):

    max_connections = (number_of_people * (number_of_people - 1)) // 2
    if total_connections > max_connections:
        total_connections = max_connections
        print("total connections too large, auto assign to:", max_connections)


    people = []
    connected_people = []

    # create instances of person class to fill people list
    file = open("RandomNames.txt", "r")
    for i in range(number_of_people):
        people.append(Person(file.readline().rstrip("\n")))

    file.close()

    # Randomize who is friends with who
    for i in range(total_connections):
        connection = random.sample(range(len(people)), 2)
        while people[connection[0]] in people[connection[1]].get_friends():
            connection = random.sample(range(len(people)), 2)
        connection.sort()
        people[connection[0]].add_friend(people[connection[1]])
        people[connection[1]].add_friend(people[connection[0]])

        if people[connection[1]].get_friend_count() >= max_friends:
            connected_people.append(people.pop(connection[1]))
        if people[connection[0]].get_friend_count() >= max_friends:
            connected_people.append(people.pop(connection[0]))

    # moving all people into connected_people list
    while people:
        connected_people.append(people.pop())

    return connected_people


def visualise_people(people):
    for person in people:
        print(person, person.get_friend_count(), person.get_friends())


#generate_people_with_friends(100, 50, 1)