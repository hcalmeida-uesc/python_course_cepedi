if __name__ == "__main__":
    __name__ = 'Area Retangulo'
    #considerando que esse ponto será, SEMPRE, o superior esquerdo do retângulo
    print('Informe o ponto superior esquerdo: ')
    x_sup,y_sup = float(input('x: ')), float(input('y: '))

    print('Informe o ponto inferior direito: ')
    #considerando que esse ponto será, SEMPRE, o inferior direito do retângulo
    x_inf,y_inf = float(input('x: ')), float(input('y: '))

    base = abs(x_sup - x_inf)
    altura = abs(y_sup - y_inf)

    print(f'Area do retangulo: {base*altura}')