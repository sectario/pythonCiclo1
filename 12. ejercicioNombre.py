name = str(input("Nombre"))

print(name.upper())
print(name.lower())

divideName = name.split()
capitalizeName = ""


for i in range(len(divideName)):
    capitalizeName = capitalizeName + " " + divideName[i].capitalize()

print(capitalizeName.strip())