# Importa la clases
from three import ConicFittingApp
from firts import Point, Line, HomogeneousIntersection
from second import Conic, ConicPlotter
import numpy as np


def main():
    # Crea una instancia de la clase ConicFittingApp
    app = ConicFittingApp()

    # El usuario agrega puntos haciendo clic en el gráfico

    # Realiza el ajuste de la cónica utilizando los puntos ingresados
    C = app.calcular_conica()

    # Punto de tangencia (si es necesario)
    x0 = 3
    y0 = 4

    # Graficar la cónica
    conic = Conic(C)
    conic_plotter = ConicPlotter(conic, x0, y0)
    #conic_plotter.plot()

    # Calcular e imprimir la intersección de líneas en coordenadas homogéneas
    # (si es necesario)
    line1 = Line(Point(-7, 4), Point(7, -4))
    line2 = Line(Point(-5, -5), Point(4, 5))
    intersec = HomogeneousIntersection(line1, line2)
    intersection_point = intersec.intersect()
    print("Intersection point:", intersection_point)
    #intersec.plot()


if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar la aplicación