import math

if __name__ == "__main__":
    __name__ = 'Distancia entre pontos'
    
    print('Informe as coordenadas do primeiro ponto: ')
    x1,y1 = float(input('x: ')), float(input('y: '))

    print('Informe as coordenadas do segundo ponto: ')
    x2,y2 = float(input('x: ')), float(input('y: '))

    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print(f'Distância entre ({x1}, {y1}) e ({x2}, {y2}): {distancia:.2f}')