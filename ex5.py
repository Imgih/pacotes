while True:
    try:
        numero = int(input("Entre com um número: "))
        print(5/numero)
        break
    except ValueError:
        print('Valor Errado')
    except ZeroDivisionError:
        print("Desculpa.Não posso dividir por zero")
    except:
        print("Naõ sei o que fazer...")