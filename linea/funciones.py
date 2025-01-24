#archivo con todas las funciones necesarias para la aplicación "línea"
def calcular_y(x,m,b):
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección de y
    '''
    return (m*x)+b

def test_linea():
    '''
    Comprobamos calcular_y()
    '''
    y = calcular_y(0, 2, 3)
    return y

if __name__ == '__main__':
    if test_linea():
        print('Test exitoso')
    else:
        print('Test fallido')