from ursina import *

class Main(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

    def update():
        pass
    
    
    def input():
        pass
    
    app = Ursina(title='Pong Game!')

    app.run()