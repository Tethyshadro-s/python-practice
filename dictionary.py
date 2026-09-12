# dictionary = a collection of {key:value} pairs, ordered and changeable, no duplicates.

capitals= {"India": "New delhi",
           "USA": "Washungton DC.",
           "China": "Beijing",
           "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("India"))

if capitals.get("Japan"):
    print("Capital exists")
else:
    print("Capital does not exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
print(capitals)

capitals.pop("China")
print(capitals)

#capitals.clear()
