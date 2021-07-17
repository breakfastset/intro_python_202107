

for i in range(5): # print 0 to 4
    print(i)

print()  # print a new line

for x in range(2, 8):   # print 2 to 7
    print(x)

print()

# super_heroes is a list (collection)
super_heroes = ["batman", "wonder woman", "green lantern", "flash", "hulk", "vision"]
#                 0              1             2             3         4      5
print(super_heroes[1])   # wonder woman

for super_hero in super_heroes:  # run through the list one by one
    print(super_hero)   # print out individual item

print()

super_heroes.append("scarlet witch")
super_heroes.append("superman")

print(super_heroes)   # print out the entire list , usually used for debugging

