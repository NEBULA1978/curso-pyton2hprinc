"""
LISTAS[]

"""
demo_list = [1, "hello", 1.32, True, [1, 2,3]]
colors = ["red","green","blue","red"]

numbers_list = list((1, 2, 3, 4))

#colors.extend(["violet", "yellow"])
#colors.extend(["pink", "black"])
#colors.insert(1, "violet")
#colors.insert(-1, "violet")
colors.insert(len(colors), "violet")

print(colors)

#colors.pop()
#colors.pop()

#colors.remove("green")
#colors.pop(0)
#colors.clear()#deja la lista vacia
#colors.sort()#ordena
#colors.sort(reverse=True)


print(colors.index("red"))

print(colors.index("blue"))

print(colors.count("red"))