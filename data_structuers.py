# data structures
# collection
# list , dictionary , set

scores:23 , 45 , 65 , 78 , 90 , 43 , 23 , 56 , 78 , 43 , 43 ]
print(scores)

# access score
print(scores[0])
print(scores[1])

# add a score
scores.append
print(scores)

# remove
scores.remove(43)
print(scores)

print(len(scores))
print(scores.count(45))

scores.sort  # ascending
print(scores)

scores.sort(reverse=True)
print(scores)

# slice a list
top_5 = scores[-5:]  # cutting the list
print(top_5)

# dictionary

person = {"name": "Halima", "age": 19, "weight": 45, "county": "Nairobi"}
print(person)

# set
days = { "mon", "tues", "wed" , "thu", "fri", "sat", "sun" ,"mon" }
print(days)


for each in scores:
    print(each)
if each < 50:
    print(each)
        


    















