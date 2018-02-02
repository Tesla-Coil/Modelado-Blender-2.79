import  bge

controlador = bge.logic.getCurrentController()

cubo = controlador.owner


print(cubo['vida'])

cubo['vida'] -= 1

if cubo['vida'] <= 0:

    cubo.endObject()