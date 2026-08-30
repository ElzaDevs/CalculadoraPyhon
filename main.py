def calculadora():
    while True:
        print("== Calculadora Simples ==")
        print(" 1. Adição (+) ")
        print(" 2. Subtração (-) ")
        print(" 3. Multiplicação (*) ")
        print(" 4. Divisão ( / ) ")
        print(" 0. Sair do programa  ")

        operacao = input("Digite uma opção acima, ou aperte 0 para sair: ")

        if operacao == '0':
            print("== Muito obrigado por utilizar a calculadora simples! ==")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção Inválida! Tente novamente...")
            continue

        number_one = float(input("Digite o primeiro número: "))
        number_two = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = number_one + number_two
            print("O resultado da adição é:", resultado)

        elif operacao == '2':
            resultado = number_one - number_two
            print("O resultado da subtração é:", resultado)

        elif operacao == '3':
            resultado = number_one * number_two
            print("O resultado da multiplicação é:", resultado)

        elif operacao == '4':
            if number_two == 0:
            print("Divisões por zero não são possíveis. Tente novamente...")
            continue
        else:
            resultado = number_one / number_two
            print("O resultado da divisão é:", resultado)


calculadora()
