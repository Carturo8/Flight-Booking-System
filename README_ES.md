# ✈️ Sistema de Reservas de Vuelos

### English Version
[Click here to see the README in English](https://github.com/Carturo8/Flight-Reservation-System/blob/main/README.md)

---

Este es un sencillo **Sistema de Reservas de Vuelos** basado en la terminal y escrito en Python. Permite a los usuarios:

- Reservar asientos disponibles en vuelos predefinidos.
- Ver los porcentajes de ocupación de cada vuelo.
- Exportar un informe ordenado con los horarios y disponibilidad de los vuelos.
- Interactuar a través de un menú de texto amigable.

---

## 📁 Estructura del Proyecto

```bash
flight_reservation/
├── flight_reservation.py # Main script
└── flight_schedule_report_example.txt # Auto-generated report file
```

---

## 🧰 Funcionalidades

- ✅ **Reservar Asientos**: Selecciona un vuelo y reserva un asiento disponible.
- 📊 **Cálculo de Ocupación**: Visualiza qué tan lleno está cada vuelo.
- 📝 **Generación de Reportes**: Exporta un informe estructurado ordenado por hora de salida.
- 💬 **Menú Interactivo**: Interfaz amigable en la línea de comandos para la interacción del usuario.

---

## 🧪 Validación de Entrada

- El **código de vuelo** debe seguir el formato: `XX-123`.
- El **asiento** debe seguir el formato: Letra + 1 o 2 dígitos (por ejemplo, `A1`, `D12`).

Si se ingresa un formato inválido, el sistema mostrará una advertencia y pedirá que se ingrese nuevamente.

---

## 🚀 Cómo Ejecutar

1. Asegúrate de tener instalado **Python 3**.  
2. Clona este repositorio o descarga el script.  
3. Ejecuta el script principal:

```bash
python flight_reservation_system.py
```

---

## 💡 Ejemplos de Uso

### ✈️ Vuelos Disponibles

El sistema inicia con tres vuelos precargados:

| Código de Vuelo | Origen   | Destino    | Hora de Salida | Asientos                   |
|-----------------|----------|------------|----------------|----------------------------|
| AV-201          | Londres  | París      | 09:45          | A1, A2, B1, B2, C1, C2     |
| AV-305          | Nueva York | Miami    | 14:15          | A1, A2, B1, B2, E1, E2     |
| AV-408          | Tokio    | Seúl       | 21:30          | A1, A2, B1, B2, D1, D2     |

### 📋 Menú de Ejemplo

Cuando ejecutes el script, verás el menú principal:

```bash
---------- 📊 Flight Reservation System ----------

1. Reserve a seat
2. Calculate occupancy percentage per flight
3. Export sorted flights report
4.🚪 Exit

👉 Enter the number of the action you want to perform:
```

### ✅ Reservar un Asiento

```bash
👉 Enter the number of the action you want to perform: 1

 -------------------- RESERVE A SEAT --------------------

Enter the flight code (format: XX-###): av-201

Available seats for flight AV-201: A1, A2, B1, B2, C1, C2

Enter the seat you wish to reserve (e.g., A1 or D12): a2

✅ Seat A2 has been successfully reserved for flight AV-201.

Would you like to reserve another seat? (y/n): n
```

### 📊 Calcular el Porcentaje de Ocupación

```bash
👉 Enter the number of the action you want to perform: 2

 -------- CALCULATE OCCUPANCY PERCENTAGE --------

Flight AV-201:
Total seats: 6 
Occupied seats: 1 
Occupancy rate: 16.67%

Flight AV-305:
Total seats: 6 
Occupied seats: 0 
Occupancy rate: 0.00%

Flight AV-408:
Total seats: 6 
Occupied seats: 0 
Occupancy rate: 0.00%
```

### 📝 Generar Reporte

```bash
👉 Enter the number of the action you want to perform: 3

 --------- EXPORT SORTED FLIGHTS REPORT ---------

✅ Flight schedule report has been generated successfully!
```

El archivo `flight_schedule_report_example.txt` será creado con información detallada y ordenada de los vuelos, como:

```bash
FLIGHT SCHEDULE REPORT
==================================================

Flight Code: AV-201
Departure Time: 09:45
Origin: London
Destination: Paris
Available Seats: 5
Occupancy Rate: 16.67%

...

Report generated at: 2025-05-16 10:42:31
```

---

## 🛠️ Tecnologías Utilizadas

- Python 3.
- Librerías Estándar:
  - `copy` para integridad de datos.
  - `re` para validación de entrada basada en expresiones regulares.
  - `datetime` para la marca de tiempo en los reportes.

---

## 📜 Licencia

Este proyecto está bajo la [Licencia MIT](https://github.com/Carturo8/Flight-Reservation-System/blob/main/LICENSE).
