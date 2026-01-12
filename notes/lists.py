#AB 1st list types notes
#lists
siblings = ["Anna", "Kailyn", "Lauren", "Danielle", "Jason"]

print(siblings[3])
siblings[-1] = "Dude"

print(siblings)

#tuples
fruit = ("apple", "banana", "peach", "kiwi", "raspberry")
home = (0,0)
x,y = home

print(x)

#set
colors = {"orange", "purple", "green", "blue", "yellow","red"}
colors.add("pink")
colors.remove("purple")
for i in colors:
    if i == "orange":
        i = "marron"
    print(i)
print(colors)

