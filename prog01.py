nome=input("Digite o seu nome:")
idade=int(input("Digite a sua idade:"))
if idade>80: print(nome,", como você está velho(a)!!!")
else:
    if idade>50:
        print(nome,", você é uma pessoa de meia idade!!!")
        print("Meia idade? Quantas pessoas de",idade*2,"anos você conhece?")
    else:
        if idade>20:
            print(nome,", você é uma com ",idade,"anos de idade (óbvio)")
        else: print(nome," como você tá novo(a)!!!")