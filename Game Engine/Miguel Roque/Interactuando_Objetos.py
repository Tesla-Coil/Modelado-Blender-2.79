import bge

controlador = bge.logic.getCurrentController()

rojo = controlador.owner

# Localizamos el cubo azul

escena = bge.logic.getCurrentScene()

azul = escena.objects['Azul']

print(azul['puntos'])

azul['puntos'] -= 1

if azul['puntos'] <= 0:

    azul.endObject()