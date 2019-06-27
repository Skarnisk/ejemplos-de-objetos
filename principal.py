from objetos import *
from empleado import *
from factura import *
et = Objeto()
print (et.color)
print (et.tamanio)
print (et.aspecto)
et.color = "rosa"
print (et.color)

objeto = Objeto()
print(Dedo().tamanio)
Dedo().tamanio = "dedo grande"
x = NuevoObjeto()
print (x)
print (x)

compra1 = Factura(12, 110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.a_pagar(), "euros")
print(Factura.__tasa) # error

empleado1 = Empleado("Francisco",30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco José")
print(empleado1.getnombre(),",", empleado1.getsalario())