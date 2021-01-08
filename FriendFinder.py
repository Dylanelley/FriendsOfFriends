from PeopleGenerator import generate_people_with_friends, visualise_people

import random

number_of_people = 100
max_friends = 90
total_connections = 50

# generating list of people with friends
people = generate_people_with_friends(number_of_people, max_friends, total_connections)
visualise_people(people)
# selecting 2 people to connect
values = random.sample(range(len(people)), 2)
root = people[values[0]]
target = people[values[1]]
print("is", root, "connected with", target)

print(root.is_connected(target))



