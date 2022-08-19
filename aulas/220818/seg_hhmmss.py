if __name__ == "__main__":
    segundos = tempo = int(input('Segundos:'))
    
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    print(f'{tempo}s equivalem a {horas}h:{minutos}m:{segundos}s')