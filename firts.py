#Bibliotecas
from abc import abstractmethod
import matplotlib.pyplot as plt
import numpy as np

# Clase para representar un punto en coordenadas homogéneas
class Point:
    
    """
    Esta clase, contiene el método homogéneo que es el necesario para 
    homogenizar el sistema dado, sea x & y.
    
    """
    @abstractmethod
    def __init__(self, x, y): #Funcion inicializadora
        self.x = x
        self.y = y
    
    def homogeneous(self):
        """
        Se hace un arreglo que añade el uno para que quedé homogéno.
        """
        return np.array([self.x, self.y, 1])

# Clase para representar una línea mediante dos puntos
class Line:
    """
    Constructor de la clase co parámetros

    :param point1: primer punto de la lina
    :param point2: segundo punto de la linea


    """
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def direction(self):
        """
        Calcula la direción de la linea
        """
        return np.cross(self.point1.homogeneous(), self.point2.homogeneous())
   # Método para graficar la línea
    def plot(self):
        """
        Método para trazar la linea de un gráfico
        """
        plt.plot([self.point1.x, self.point2.x], [self.point1.y, self.point2.y], label='Line')

    
# Clase para calcular la intersección de dos líneas en coordenadas homogéneas
class HomogeneousIntersection:
    def __init__(self, line1, line2):

        """
        Constructor de la clase
        :param line1 and line 2 objetos de linea que representan dichas lineas

        """
        self.line1 = line1
        self.line2 = line2
    
    def intersect(self):
        """
        Calcula la intersección de las dos líneas en coordenadas homogéneas.

        :return: Un vector que representa el punto de interseccoón en coordenadas homogémeas.
        """
        direction1 = self.line1.direction()
        direction2 = self.line2.direction()
        intersection = np.cross(direction1, direction2)
        return intersection / intersection[2]

    # Método para graficar las líneas y el punto de intersección
    def plot(self):

        """
        Método para graficar las líneas y el punto de intersecion

        Muestra un gráfico que representa visualmente las dos líneas y el punto de intersección.
        """
         
        intersection = self.intersect()

        #Gráficas
        plt.plot([self.line1.point1.x, self.line1.point2.x], [self.line1.point1.y, self.line1.point2.y], label='Line 1')
        plt.plot([self.line2.point1.x, self.line2.point2.x], [self.line2.point1.y, self.line2.point2.y], label='Line 2')

        plt.scatter(intersection[0], intersection[1], color='red', label='Intersection')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Homogeneous Line Intersection')
        plt.legend()

        plt.grid()
        plt.show()