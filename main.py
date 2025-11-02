from vehiculo import Vehiculo
from automovil import Automovil
from moto import Moto

def main():
    # Crear lista de vehículos
    vehiculos: list[Vehiculo] = [
        Automovil("Toyota", "Corolla", 25000.0, 4),
        Automovil("Honda", "Civic", 27000.0, 5),
        Moto("Yamaha", "YZF", 12000.0, 200),
        Moto("Kawasaki", "Ninja", 15000.0, 400)
    ]

    # Mostrar información de cada vehículo
    print("=== Inventario del Concesionario ===")
    total_inventario = 0.0
    
    for vehiculo in vehiculos:
        precio_final = vehiculo.precio_final()
        print(f"\n{vehiculo.ficha()}")
        print(f"Precio Final: ${precio_final:.2f}")
        total_inventario += precio_final

    print(f"\nValor Total del Inventario: ${total_inventario:.2f}")

if __name__ == "__main__":
    main()