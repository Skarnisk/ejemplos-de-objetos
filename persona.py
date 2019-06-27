class Persona(object):
    edad= ""
    nombre= ""

    def caminar(self):
            return("de paseo")
    def saltar(self):
            return("pal techoooo")
    def correr(self):
            return("fuck the police")

Esteban = Persona()
Esteban.correr()
Esteban.saltar()
Esteban.caminar()
print(Esteban.caminar(), Esteban.correr(), Esteban.saltar())