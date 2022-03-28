"""
LISTAS[]

"""
demo_list = [1, "hello", 1.32, True, [1, 2,3]]
colors = ["red","green","blue"]

numbers_list = list((1,2, 3, 4))
#print(type(numbers_list))

#r =list(range(1, 100))
#print(r)
print(type(colors))
print(dir(colors))
print(len(colors))
print(len(demo_list))
print(colors[1])
print(colors[2])
print(colors[0])
print(colors[-1])
print(colors[-2])
print(colors[0])
print("green" in colors)
print("violeta" in colors)
print("fsfdsggf" in colors)

print(colors)
colors[1] = "yellow"
print(colors)

#print(dir(colors))

#colors.append("violet")
colors.append("violet", "yellow")
print(colors)