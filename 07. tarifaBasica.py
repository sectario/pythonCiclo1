name = str(input("Ingrese su nombre"))
estratoLista = ("$10,000", "$15.000", "$30.000", "$50.000", "$65.000")

while True:
    estrato = int(input("Idique su estrato entre 1-5"))
    if estrato<1 or estrato>5:
        print(name + "ingrese un estrato entre 1-5 ")
        continue
    else:
        estratoEnLista = estrato - 1
        print(name + " su tarifa es " + str(estratoLista[estratoEnLista]))
        break
