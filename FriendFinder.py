from PeopleGenerator import generate_people_with_friends, visualise_people

import random

number_of_people = 20
max_friends = 7
total_connections = 15

# generating list of people with friends
people = generate_people_with_friends(number_of_people, max_friends, total_connections)
visualise_people(people)
# selecting 2 people to connect
values = random.sample(range(len(people)), 2)
root = people[values[0]]
target = people[values[1]]

print("\nis", root, "connected with", target)
print(root.is_connected(target))

print ("\nFind Path from", root, "to", target)
print(root.find_path_to(target))




