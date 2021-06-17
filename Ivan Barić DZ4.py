import re

regex = "^([a-z]+).([a-z]+)([@]fpmoz[.]sum[.]ba$)"

while 1:
    unos = input("Unesite vaš mail: ")
    rezultat = re.match(regex, unos)
    if rezultat:
        print("Ispravan unos!")
        grupa = rezultat.groups()
        break
    else:
        print("Pogrešan unos!")

ime = grupa[0][0]
prezime = grupa[1]

regex2 = "^"+ime+prezime+"([0-9]*[@]sum[.]ba$)"

while 1:
    unos2 = input("Unesite vaš eduID: ")
    rezultat2 = re.match(regex2, unos2)
    if rezultat2:
        print("Ispravan unos!")
        break
    else:
        print("Pogrešan unos!")
