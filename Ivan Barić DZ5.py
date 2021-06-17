def parni(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

def neparni(x):
    for i in range(x):
        if i % 2 == 1:
            yield i

unos = int(input("Unesite broj: "))
generator_parni = parni(unos)
generator_neparni = neparni(unos)

brojevi = zip(generator_parni, generator_neparni)
for parni, neparni in brojevi:
    print(parni, "paran,", neparni, "neparan")
