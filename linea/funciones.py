#archivo con todas las funciones necesarias para la aplicación "línea"
import matplotlib.pyplot as plt

def calcular_y(x: float,m: float,b:float)->float:
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección de y
    '''
    return (m*x)+b

def grafica_linea(X:list, Y:list, m:float, b:float):
     '''
    Gráfica de una línea recta
    x: lista de valores de x
    y: lista de valores de y
    Regresa: nada
    '''
     plt.plot(X,Y)
     plt.title(f'Línea con pendiente {m} y ordenada al origen {b}')
     plt.xlabel('X')
     plt.ylabel('Y')
     plt.show()

def test_linea():
    '''
    Comprobamos calcular_y()
    '''
    y = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Test fallido')