while True:
    try:
        numero = int(input("Entre com um número: "))
        print(5/numero)
        break
    except (ValueError,ZeroDivisionError):
        print('Valor Errado ou Não é possível dividir por zero')
    except:
        print("Desculpa, algo errado aconteceu...")