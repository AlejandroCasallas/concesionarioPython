from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0")
        self._puertas = puertas

    @property
    def puertas(self) -> int:
        return self._puertas

    def impuesto(self) -> float:
        impuesto_base = self.precio_base * 0.08
        if self.puertas == 5:
            impuesto_base -= self.precio_base * 0.01
        return impuesto_base

    def ficha(self) -> str:
        return f"{super().ficha()}, Puertas: {self.puertas}"