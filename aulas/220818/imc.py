if __name__ == "__main__":
    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    imc = peso/(altura*altura)

    print(f'IMC: {imc}')