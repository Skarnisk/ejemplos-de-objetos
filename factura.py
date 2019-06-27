class Factura:
    _tasa =19

    def _init_(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio

    def a_pagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura._tasa / 100
        return(total + impuesto)