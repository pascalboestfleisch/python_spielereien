somelist = [1,12,2,53,23,6,17,14] 

min_value = None
for value in somelist:
    if not min_value:
            min_value = value
    elif value < min_value:
            min_value = value
print(min_value)

max_value = None
for value in somelist:
        if not max_value:
              max_value = value
        elif value > max_value:
               max_value = value
print(max_value)
             
curr = 0
k = 0

median = None
for test in somelist:
      curr += test
      k += 1
print(curr/k)

originalString = "Hello World!"
reversedString = ''

for char in originalString:
     reversedString = char + reversedString
print(reversedString)

arr3 = ["zappelin", "zimt", "Zucker", "zebra", "Zickzack"]
numb = 0
for i in arr3:
    if(i[0] == "z" or i[0] == "Z"):
        numb += 1
print(numb)


arrayTest = []
listenList = (1,2,3)

f = 0
while f < 6:
        eingabe2 = int(input("Bitte ein Array von 6 Zahlen eingeben: "))
        arrayTest.append(eingabe2)
        f += 1
print(arrayTest)

newList = ("Anna", "Peter", "Hans")

gesuchterName = str(input("Bitte gesuchten Namen eingeben: "))
for i in newList:
    if(i == gesuchterName):
        vorhanden = True
    elif(i != gesuchterName):
        vorhanden = False
print(vorhanden)

arrayNamen = ["Hans", "Holger", "Hampelmann"]


for i in arrayNamen:
      if(i[0] == "H" or i[0] == "h"):
            print(i)

num = 0
for i in arrayNamen:
      if(i[0] == "H" or i[0] == "h"):
            num += 1
print(num)

originalString2 = input("Bitte einen Wert angeben: ")
reversedString2 = ''

for char in originalString2:
      reversedString2 = char + reversedString2
print(reversedString2)

    