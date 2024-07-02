import random
from datetime import datetime, timedelta

def generate_inserts(start_year, end_year, employee_id):
    registroentrada_inserts = []
    registrosalida_inserts = []
    dias_no_trabajados = set()  # Usamos un conjunto para almacenar los días no trabajados
    
    # Días en cada mes
    days_in_month = {
        1: 31,
        2: 28,  # Consideramos años no bisiestos aquí
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Ajustar febrero en año bisiesto
            if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                days = 29
            else:
                days = days_in_month[month]
                
            for day in range(1, days + 1):  # Ajustar el rango de días según el mes
                # Generar una probabilidad de 10% para llegar tarde (retraso de hasta 30 minutos)
                if random.random() < 0.1:
                    retraso_ingreso_minutos = random.randint(0, 30)
                else:
                    retraso_ingreso_minutos = 0
                
                # Generar una probabilidad de 5% para que no registre entrada ni salida
                if random.random() < 0.05:
                    dias_no_trabajados.add((year, month, day))
                    continue  # Saltar este día
                
                # Generar fecha y hora de entrada
                hora_ingreso = datetime(year, month, day, 8, retraso_ingreso_minutos, random.randint(0, 59))
                
                # Generar fecha y hora de salida
                hora_salida = datetime(year, month, day, 17, random.randint(0, 10))

                # Formatear para SQL
                hora_ingreso_str = hora_ingreso.strftime('%Y-%m-%d %H:%M:%S')
                hora_salida_str = hora_salida.strftime('%Y-%m-%d %H:%M:%S')

                # Crear inserts solo si no es un día no trabajado
                if (year, month, day) not in dias_no_trabajados:
                    registroentrada_inserts.append("('{}', '{}')".format(hora_ingreso_str, employee_id))
                    registrosalida_inserts.append("('{}', '{}')".format(hora_salida_str, employee_id))

    # Crear los comandos SQL
    registroentrada_sql = "INSERT INTO registroentrada (horaIngreso_registro, rut_empleado) VALUES\n{};".format(",\n".join(registroentrada_inserts))
    registrosalida_sql = "INSERT INTO registrosalida (horaSalida_registro, rut_empleado) VALUES\n{};".format(",\n".join(registrosalida_inserts))

    # Combinar registros en un solo archivo
    combined_sql = registroentrada_sql + "\n\n" + registrosalida_sql

    return combined_sql, dias_no_trabajados

# Generar los inserts para los años 2023 y 2024 para el empleado '12345678-9'
combined_sql, dias_no_trabajados = generate_inserts(2023, 2024, '12345678-9')

# Guardar en archivo de texto
with open('registros.sql', 'w') as file:
    file.write(combined_sql)

# Imprimir los días que no se trabajaron
if dias_no_trabajados:
    print("Días que no se trabajaron:")
    for year, month, day in sorted(dias_no_trabajados):
        print(f"{year}-{month:02d}-{day:02d}")
else:
    print("No hubo días que no se trabajaron.")

print("Archivos generados correctamente: registros.sql")
