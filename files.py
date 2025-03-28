# files
file = open("text.txt", "w")

file.write("hello world")

file.close()

file = open("text.txt", "a")
file.write("hello world\n")
file.close()

file = open("text.txt", "r")
data = file.read()
file.close()


# read and create csv files
data = [9, 10]
# x = data[0]
# y = data[1]

x, y = data
print(x)
print(y)


def population():
    return "Nairobi", 4000000

name, pp = population()
print(pp)
print(name)

===




