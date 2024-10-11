# JERCICIO DEL CUBO
# ==========================================
import random


# Funcion para inicializar el cubo usando valores aleatorios
def iniCubo(cb, semanas):
    for fil in range(len(cb)):  # Filas segun el número de empleados
        for col in range(6):  # Dias laborales trabajados, en este caso 6 (Lunes a Sabado)
            for pro in range(semanas):  # Cantidad de semanas del mes
                cb[fil][col][pro] = random.randint(1,
                                                   12)  # Aca se asignan las horas laboradas de manera aleatoria, con un maximo de 12hrs


# Imprime el cubo de horas trabajadas con formato
def impCubo(cb, empleados, semanas):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    for pro in range(semanas):
        print()  # imprime espaciado
        print('=====================================')
        print(f"Semana {pro + 1}")
        for col in range(6):
            print(f"{dias[col]}\t", end="")
        print()  # Imprimir espaciado

        for fil in range(len(cb)):  # por cada empleado
            print(f"{empleados[fil]}\t", end="")
            for col in range(6):  # por cada día
                print(f"{cb[fil][col][pro]:02}\t", end="")
            print()  # salto de línea
        print('=====================================')


# Calcula el salario mensual del empleado
def calcularSalarios(cb, empleados, salarios, semanas):
    print()  # Imprime espaciado
    print("PLANILLA:")
    print("---------")
    print("Empleado\tHoras\tSalario")

    for fil in range(len(cb)):
        total_horas = 0  # Horas
        for col in range(6):  # Días
            for pro in range(semanas):  # Semanas
