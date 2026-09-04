import os 
os.system("cls")

print("Bem Vindo(a) ao Comparador de Preços")

produto = input("Informe o produto escolhido:")

mercado01 = float(input("Informe o preço do produto no mercado bom:"))
mercado02 = float(input("Informe o preço do produto no mercado du bom:"))
mercado03 = float(input("Informe o preço do produto no mercado bala:"))

if mercado01 < mercado02 and mercado03:
    print("Melhor Preço em: Mercado bom")

elif mercado02 < mercado01 and mercado03:
    print("Melhor Preço em: Mercado du bom")

elif mercado03 < mercado01 and mercado02:
    print("Melhor Preço em: Mercado bala")

