import  bge

def raton():

    controlador = bge.logic.getCurrentController()
    objeto = controlador.owner

    # Accedemos al controlador

    mouse = controlador.sensors['Mouse']

    if mouse.positive:

        print('Esto funciona')


raton()