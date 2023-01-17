from random import *

prompt = "Name der Person: ('end' zum Beenden):\n"
people = list(iter(lambda:input(prompt), "end"))

shuffle(people)
people.append(people[0])
for i in range(len(people) - 1):
    print(people[i],"beschenkt", people[i + 1])