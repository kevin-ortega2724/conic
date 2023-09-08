import numpy as np
import matplotlib.pyplot as plt

class ConicFittingApp:
    def __init__(self):
        """
        Inicializo

        Se crea la función para crear la ventana graáfoca vacia que contiene el botón
        Esto permite hacer el ajuste al presionar el boton

        Además se define el evento por la iteración del mouse.
        """
        self.puntos = [] #Lista vacia para los puntos

        # Crear una figura de Matplotlib y definir el evento de clic
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title('Ajuste de Cónica')
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        # Crear un botón para realizar el ajuste
        self.calcular_button = plt.axes([0.85, 0.01, 0.1, 0.05])
        self.button = plt.Button(self.calcular_button, 'Calcular')
        self.button.on_clicked(self.realizar_ajuste)

        plt.show()

    def on_click(self, event):
        """
        Manejador de eventos de clic en el gráfico

        Esta función se llama cuando el usuario hace clic en el gráfico. Agrega el punto clicado a la lista de
        puntos y actualiza el gráfico.

        Args:
            event (matplotlib.backend_bases.MouseEvent): El evento de clic en el gráfico.

        Returns:
            Ninguno.
        """
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.puntos.append([x, y])
            self.ax.plot(x, y, 'bo')
            self.fig.canvas.draw()

    def calcular_conica(self):
        """
        Calcula la matriz de la cónica mediante ajuste de mínimos cuadrados.

        Esta función calcula la matriz de la cónica a partir de la lista de puntos ingresados por el usuario. Se
        utiliza el método de mínimos cuadrados y la descomposición SVD para realizar el cálculo.

        Args:
            Ninguno.

        Returns:
            numpy.ndarray: La matriz de la cónica 3x3 calculada.
        """

        if len(self.puntos) < 5:
            print("Se necesitan al menos 5 puntos para calcular una cónica.")
            return None

        puntos = np.array(self.puntos)
        A = np.column_stack((puntos[:, 0] ** 2, puntos[:, 0] * puntos[:, 1], puntos[:, 1] ** 2, puntos[:, 0], puntos[:, 1], np.ones(len(puntos))))
        _, _, Vt = np.linalg.svd(A) #Desconposición de valor

        # Obtener el vector c de la matriz Vt
        c = Vt[-1]

        # Crear la matriz C a partir de c
        C = np.array([[c[0], c[1] / 2, c[3] / 2],
                      [c[1] / 2, c[2], c[4] / 2],
                      [c[3] / 2, c[4] / 2, c[5]]])

        return C

    def graficar_conica(self, C):
        """
        Grafica la cónica en el gráfico.

        Esta función utiliza la matriz de la cónica calculada para graficar la cónica en el gráfico junto con
        los puntos originales.

        Args:
            C (numpy.ndarray): La matriz de la cónica 3x3.

        Returns:
            Ninguno.
        """
        # Crear una malla de puntos
        x = np.linspace(-10, 10, 400)
        y = np.linspace(-10, 10, 400)
        X, Y = np.meshgrid(x, y)

        # Calcular la ecuación de la cónica
        Z = C[0, 0] * X**2 + C[1, 1] * Y**2 + 2 * C[0, 1] * X * Y + 2 * C[0, 2] * X + 2 * C[1, 2] * Y + C[2, 2]

        # Graficar la cónica
        self.ax.contour(X, Y, Z, levels=[0], colors='r')
        self.fig.canvas.draw()

    def realizar_ajuste(self, event):
        """
        Realiza el ajuste de cónica y grafica el resultado.

        Esta función se llama cuando el usuario presiona el botón "Calcular". Realiza el ajuste de cónica
        llamando a la función calcular_conica y luego grafica la cónica llamando a la función graficar_conica.

        Args:
            event (matplotlib.backend_bases.MouseEvent): El evento de clic en el botón "Calcular".

        Returns:
            Ninguno.
        """
        C = self.calcular_conica()
        if C is not None:
            self.graficar_conica(C)
        print(C)

if __name__ == "__main__":
    app = ConicFittingApp()
    cc = app.realizar_ajuste
    """
    Inicializa la aplicación de ajuste de cónica, crea una instancia de la clase ConicFittingApp y llama a la
    función realizar_ajuste para comenzar la aplicación.
    """
