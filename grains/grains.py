
def square(number):
    if number not in range(1, 65):
        raise ValueError("Los cuadrados del tablero de ajedrez deben ser números enteros entre 1 y 64.")
    return 2 ** (number - 1)

def total():
    return 2**64 - 1