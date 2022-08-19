if __name__ == "__main__":
    __name__ = "Valor em cédulas"
    
    quantidade_1 = valor = int(input('Valor em R$ (inteiro): '))
    
    quantidade_200 = quantidade_1 // 200
    quantidade_1 %= 200
    quantidade_100 = quantidade_1 // 100
    quantidade_1 %= 100
    quantidade_50 = quantidade_1 // 50
    quantidade_1 %= 50
    quantidade_20 = quantidade_1 // 20
    quantidade_1 %= 20
    quantidade_10 = quantidade_1 // 10
    quantidade_1 %= 10
    quantidade_5 = quantidade_1 // 5
    quantidade_1 %= 5
    quantidade_2 = quantidade_1 // 2
    quantidade_1 %= 2

    print(f'{quantidade_200} nota(s) de R$ 200,00')
    print(f'{quantidade_100} nota(s) de R$ 100,00')
    print(f'{quantidade_50} nota(s) de R$ 50,00')
    print(f'{quantidade_20} nota(s) de R$ 20,00')
    print(f'{quantidade_10} nota(s) de R$ 10,00')
    print(f'{quantidade_5} nota(s) de R$ 5,00')
    print(f'{quantidade_2} nota(s) de R$ 2,00')
    print(f'{quantidade_1} moeda(s) de R$ 1,00')