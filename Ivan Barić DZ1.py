import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael', 'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan', 'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan', 'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel', 'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario', 'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina', 'Josip', 'Lucija']

popisOcjena = []

for ime in imena:
    popisOcjena.append(random.randint(1, 5))

#print(popisOcjena)

sveOcjene = {
}

for ocjena in popisOcjena:
   sveOcjene[ocjena] = sveOcjene.get(ocjena, 0) + 1

parovi = sveOcjene.items()

for ime, ponavljanja in parovi:
  print('Ocjena', ime, 'pojavljuje se', ponavljanja, 'puta.')

sumaOcjena = sveOcjene[2] + sveOcjene[3] + sveOcjene[4] + sveOcjene[5]
brojOcjena = len(popisOcjena)
prolaznost = (sumaOcjena / brojOcjena) * 100

print('Prolaznost iznosi', prolaznost, '%.')
