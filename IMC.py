peso= float(input("Digite o peso em Kg:"))
alt= float(input("Digite a altura em metros:"))
res=(peso/(alt*alt))
print(res,"Kg/m²")
if res < 18.5:
    print("Abaixo do peso")
if res > 18.5 and res<=24.9:
    print("Peso normal")
if res >= 25 and res<=29.9:
    print("Sobrepeso")
if res >= 30 and res<=34.5:
    print("Obesidade nivel 1")
if res >= 35 and res<=39.9:
    print("Obesidade nivel 2")    
if res >40:
    print("Obesidade nivel 3")    