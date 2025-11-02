## Andriely Alejandro Casallas Calderon
### 1/11/2025

---

# Concesionario POO Python

Este es un mini-sistema de concesionario que implementa los 4 pilares de la Programación Orientada a Objetos en Python.

## Requisitos

- Python 3.7 o superior

## Estructura del Proyecto

```
python_version/
├── README.md
├── vehiculo.py
├── automovil.py
├── moto.py
├── main.py
├── run.sh
└── run.bat
```

## Cómo ejecutar el programa

### En Windows
1. Doble clic en `run.bat`

O desde la terminal:
```bash
.\run.bat
```

### En Linux/macOS
1. Dar permisos de ejecución al script:
```bash
chmod +x run.sh
```

2. Ejecutar el script:
```bash
./run.sh
```

### Ejecución manual (todos los sistemas)
```bash
python main.py
# o
python3 main.py
```

## Funcionalidades

- Gestión de vehículos (automóviles y motos)
- Cálculo de impuestos según tipo de vehículo
- Cálculo de precios finales
- Inventario total del concesionario

## Implementación POO

- **Encapsulamiento**: Atributos protegidos con propiedades
- **Herencia**: Clases Automovil y Moto heredan de Vehiculo
- **Abstracción**: Clase abstracta Vehiculo
- **Polimorfismo**: Manejo de diferentes tipos de vehículos a través de una interfaz común

## Estructura de Clases

- **Vehiculo**: Clase abstracta base
- **Automovil**: Hereda de Vehiculo, implementa impuestos específicos para autos
- **Moto**: Hereda de Vehiculo, implementa impuestos específicos para motos

## Reglas de Negocio

### Automóviles
- Impuesto base: 8% del precio base
- Si tiene 5 puertas: -1% del precio base

### Motos
- Cilindraje ≤ 250cc: 5% del precio base
- Cilindraje > 250cc: 9% del precio base
