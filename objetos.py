class Antena():
    color=""
    longitud=""

class Pelo():
    color=""
    textura=""

class Ojo():
    forma=""
    color=""
    tamanio=""

class Objeto():
    color=""
    tamanio=""
    aspecto=""
    antenas= Antena()
    ojos= Ojo()
    pelos= Pelo()

    def flotar(self):
        pass

class Dedo():
    longitud=""
    forma=""
    color=""
    tamanio="Grande"

class Pie(object):
    forma = ""
    color = ""
    dedos = Dedo()

class NuevoObjeto():
    pie=Pie()
    pequeño=Dedo()