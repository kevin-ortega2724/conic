#Bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Clase para representar una cónica definida por una matriz C

class Conic:
    def __init__(self, C):
        """
        Constructor de la clase Conic.

        :param C: Matriz 3x3 que define la cónica en forma cuadrática.
        """

        self.C = C
    #ax1^2+bx1​x2​+cx2^2​+dx1​​+ex2​​+f​=0
    def evaluate(self, x, y):
        """
        Evalúa la cónica en un punto (x, y).

        :param x: Coordenada x del punto.
        :param y: Coordenada y del punto.
        :return: El valor resultante de la evaluación en el punto (x, y).
        """
        vector = np.array([x, y, 1])
        return np.dot(vector, np.dot(self.C, vector))

    def tangent_line(self, x0, y0):
        """
        Calcula la ecuación de la recta tangente a la cónica en un punto (x0, y0).

        :param x0: Coordenada x del punto de tangencia.
        :param y0: Coordenada y del punto de tangencia.
        :return: Una función que representa la ecuación de la recta tangente.
        """
        gradient = np.dot(self.C, np.array([x0, y0, 1]))
        return lambda x: (-gradient[0] * x - gradient[2]) / gradient[1]

class ConicPlotter:
    def __init__(self, conic, x0, y0):

        """
        Constructor de la clase ConicPlotter.

        :param conic: Un objeto de la clase Conic que representa la cónica.
        :param x0: Coordenada x del punto de tangencia.
        :param y0: Coordenada y del punto de tangencia.
        """
            
        self.conic = conic
        self.x0 = x0
        self.y0 = y0
    
    def plot(self):
        """
        TRaza la cónica , su punto tangente y su tangete
        """
        x_vals = np.linspace(-10, 10, 400)
        y_vals = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = np.vectorize(self.conic.evaluate)(X, Y)
        
        plt.figure(figsize=(8, 6))
        plt.contour(X, Y, Z, levels=[0], colors='blue', linewidths=2)
        plt.scatter([self.x0], [self.y0], color='red', marker='o', label='Punto de tangencia')
        plt.text(self.x0 + 0.5, self.y0 - 0.5, 'Cónica', color='blue')
        
        tangent_equation = self.conic.tangent_line(self.x0, self.y0)
        x_tangent = np.linspace(self.x0 - 8, self.x0 + 8, 400)
        y_tangent = tangent_equation(x_tangent)
        
        plt.plot(x_tangent, y_tangent, color='green', label='Tangente')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Cónica, Punto de tangencia y Tangente')
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(0, color='black', linewidth=0.8)
        plt.grid()
        plt.legend()
        plt.axis('equal')
        plt.show()