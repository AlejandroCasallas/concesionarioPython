from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        if cc <= 0:
            raise ValueError("El cilindraje debe ser mayor que 0")
        self._cc = cc

    @property
    def cc(self) -> int:
        return self._cc

    def impuesto(self) -> float:
        if self.cc <= 250:
            return self.precio_base * 0.05
        return self.precio_base * 0.09

    def ficha(self) -> str:
        return f"{super().ficha()}, Cilindraje: {self.cc}cc"