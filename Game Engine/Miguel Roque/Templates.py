import bge

def localScale():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    own.localScale.x = 2

localScale()