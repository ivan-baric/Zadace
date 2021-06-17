def pozdrav(ime):
    print("Pozdrav", ime + "!")


dobrodosao = lambda ime: print("Dobrodošao", ime + "!")

def treca(x):
    x("Ivan")


treca(pozdrav)
treca(dobrodosao)
