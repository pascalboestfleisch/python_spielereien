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
             

originalString = "Hello World!"
reversedString = ''

for char in originalString:
     reversedString = char + reversedString
print(reversedString)


    