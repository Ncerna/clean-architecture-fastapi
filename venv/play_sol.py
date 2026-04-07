
import requests

edad = 99
tiene_carnet= True

if edad <=99 and tiene_carnet:
    print(f" puedes conducir")
else:
    print(f"llamar ppolicia")

if not  tiene_carnet:
    print(f"el usuario no tiene carnet")

number = [2,85,7,96,89]
print(sorted(number))



animles =["pato","loro","lobo","arroz"]
animles.append("klo")
animles.remove("pato")
animles_mayuscula = [a.upper() for a in animles]

print(f"mayusculas {animles_mayuscula}")

for am in animles_mayuscula:
    print(am)

numerolrRenge = list(range(2))
for nr in numerolrRenge:
    print(nr)



response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)