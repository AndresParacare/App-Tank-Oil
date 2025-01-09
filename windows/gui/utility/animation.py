import numpy as np
from windows.gui.utility.custom_window import color_pallete #Function for color pallete

class animation():
    def __init__(self):
        """Create animation of a chart"""
        self._x = 0
        self._y = 0

        self.example()

        #Modificar color en el argumento c
        #self.ax is connect with graphTankModule
        self.line2 = self.ax.plot(self._x[0], self._y[0], label=f'v0 = {self._y[1:]/self._x[1:]} m/s')[0]
        self.ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]',)
        #self.ax.legend()

    def update(self, frame):
        """update the line plot"""
        self.line2.set_xdata(self._x[:frame])
        self.line2.set_ydata(self._y[:frame])
        return self.line2

    def example(self, t:float = 1000, inter:float = 10000):
        """Example of animation"""
        self._x = np.linspace(0, t, inter)
        self._y = self._x **2
