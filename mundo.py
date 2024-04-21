import kivy
from kivy.app import App
from kivy.uix.label import Label

class HolaMundoApp(App):
    def build(self):
        # Configuración del tamaño de la ventana
        from kivy.core.window import Window
        Window.size = (400, 200)  # Tamaño de la ventana (ancho, alto)

        # Creación del contenido de la ventana
        return Label(text='¡Hola Mundo con Kivy!')

if __name__ == '__main__':
    HolaMundoApp().run()
