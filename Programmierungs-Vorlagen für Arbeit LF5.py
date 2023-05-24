#Inhalt:

# 1. Eingabe/ Ausgabe von Werten

eingabe = input("Gib estwas ein: ") #Eingabe
zahlen_eingabe = int(input ("Gib etwas ein:")) #Eingabe

print("Ausgegeben wird: HI" +eingabe) #Reine Konsolen Ausgabe, (alterntaive = "return" (-->fuer Funktionen) )

# Bsp
print('Enter number 1: ')
number1 = int(input())
print('Enter number 2: ')
number2 = int(input())
print('Summe =  ', number1 + number2) 
print(f'nummer1 = {number1} und nummer zwei = {number2} davon die summe ist {number1 + number2}') 

# 2. Speichern von Werten in Feld oder Liste,

# Array vs. Liste 
arr = []
liste = (1,2,3)

arr.append(eingabe)  # Fuegt am Ende etwas hinzu  =>  "arr.pop()" # entfernt lezten Eintrag
arr += eingabe # Alternativ

# Zusatz Laenge von Arrays
bspArry = [1, 2, 3, 4, 5] # Zahl 1 wird aber mit 0 angesprochen -->Arry zaehlt ab 0
anzahlArrayEntrys = len(bspArry) # Ausgabe 5

# Zusatz

#def function_name(x,y,z):
#    print(y) #-->Ausgabe = 2 

#function_name(liste[0],liste[1],liste[2]) #Funktions-Aufruf mit "Parametern"

#print(liste[1]) # alternativer Aufruf von der Listen-Ausgabe


# Konktretes Bsp. mit while-Schleife
i = 0
while (i < 5):
     eingabe = int(input("Tipp 5 Eintraege ein dann wird Array ausgegeben, Zahl an der Stelle " +str(i)+ " "))
     arr.append(eingabe)
     i += 1
print(arr)

# 3. Anwenden von Schleifen und Verzweigungen -->siehe verstreut, groestenteils bei Aufgabe 5.

Kuchen =input("Was für einen Kuchen möchtest du?") # ! Verwendung von Hunger und Kuchen zur Veranschaulichung, ansonsten jede Bedingung mit dem selben Bezug
Hunger = 0,3

if (Kuchen != "" or Kuchen == "Apfel" ):
    print("supi, Kuchen da")
elif (Hunger > 0):
    print("hungry")
else:
    print("dann halt net")


# 4. Bestimmen von Maximum, Minimum oder Durchschnitt

def max(arr):
    maxNum = arr[0]
    
    for num in arr:
        if num > maxNum:
            maxNum = num  
            
    return maxNum

def min(arr):
    minNum = arr[0]
    
    for num in arr:
        if num < minNum:
            minNum = num
            
    return minNum

testZahlenArray = [1,2,3,4]

def median(arr):
    curr = 0
    i=0
    for num in arr:
        curr += num
        i+= 1  # alternativ "x/ len(arr)"
    return curr/i

print(median(testZahlenArray)) # Ausgabe = 2.5


    # Alternativ mit Werten-Vorgabe
    # checklow = 10000000 # vorgegebene groesse positive Zahl
    # checkmax = -1000000 # vorgegebene groesse negative Zahl
    # checkavg = 0
    # arr = [1,2,3,4,5]

    # for i in arr:
    #     checkavg += i
    #     # check for lowest value
    #     if (i < checklow):
    #         checklow = i
    #     # check for highest value
    #     if (i > checkmax):
    #         checkmax = i
    # checkavg = checkavg / len(arr)

# print(checkavg)
# print(checkmax)
# print(checklow)

# 5. Suchen aller Einträge die mit z.B. "A" beginnen"

arr2 = ["apfel", 'ananas', "birne", 'depp']

for i in arr2:
    #first = i.lower()
    #if (first[0] == "a"):
         #print(i)
    if (i[0] == "a" or i[0] == "A"):
        print(i)

    # Suchen aller Einträge die ein "a" beinhalten
    nameArray = ["Karla","Anton","Peter","Amelie"]

    for word in nameArray:      #Schleife: For each 
        for i in range(len(word)):  #Schleife: For (iterativ) # alternativ auch direkte zahlen Angabe "for i in range(5)"
            if(word[i] == "a" or word[i] == "A"):
                #print(word)
                print("Das Wort: " + word + " hat ein a an der Stelle: " + str(i))

# 6. zählen der Einträge die mit a, b, c, .... z beginnen

# 7. Ausgabe der eingegebenen Werte rückwärts

zahlenArray = [1,2,3,4,5,6]

for i in range(1, len(zahlenArray) + 1):
    print(zahlenArray[-i])
    
# ODER

def reverso(zahlenArray):
    start = 0
    end = len(zahlenArray) - 1

    while start < end:
        zahlenArray[start], zahlenArray[end] = zahlenArray[end], zahlenArray[start]
        start += 1
        end -= 1
    return zahlenArray

print(reverso(zahlenArray))

# 8. suchen ob ein bestimmter Wert in der Liste ist

# 9. Strings reverten

originalString = "Hello Wolrd!"
reversedString = ''

for char in originalString:
    reversedString = char + reversedString
print(reversedString)