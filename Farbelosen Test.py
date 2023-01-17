from random import *

prompt = "Name der Person: ('end' zum Beenden):\n"
people = list(iter(lambda:input(prompt), "end"))
options = ["Rot", "Blau", "Gelb", "Grün", "Lila", "Pink", "Orange", "Schwarz/Weiß"]

if len(people) > len(options):
    raise ValueError("Es dürfen nicht mehr Menschen als Farben teilnehmen")

colors = list(options)

shuffle(people)
people.append(people[0])
for i in range(len(people) - 1):
    print(people[i],"hat", colors[i])

