import re

unos = input("Unesite string: ")

regex1 = "^(i|I).*[0-5].*(B|b)$"
regex2 = "\s"

rezultat1 = re.search(regex1, unos)
rezultat2 = re.search(regex2, unos)

if rezultat1 and rezultat2:
    print("Podudaranje!")
else:
    print("Nema podudaranja!")
