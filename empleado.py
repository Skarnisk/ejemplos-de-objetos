class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    def getnombre(self):
        return self._nombre

    def getsalario(self):
        return self._salario

    def setnombre(self, nombre):
        self._nombre = nombre

    def setsalario(self, salario):
        self._salario = salario

    def delnombre(self):
        del self._nombre

    def delsalario(self):
        del self._salario
