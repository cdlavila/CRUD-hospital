def heading():
    print('\n---------------------------------------------------------')
    print('Sistema de Gestión de Hospitales y Doctores de la Región')
    print('---------------------------------------------------------')


def main_menu():
    print('\tOPCIONES')
    print('\t1. Obtener información del Hospital')
    print('\t2. Obtener información del Doctor')
    option = input('\tOpción: ')
    return option


def input_hospital_name():
    return input('\nIngrese el nombre del Hospital: ')


def input_doctor_id():
    return input('\nIngrese el identificador(Id) del Doctor: ')


def print_hospital_information(records):
    print('\n-------------------------')
    print('Información del Hospital')
    print('--------------------------')
    for row in records:
        print("Hospital Id:", row[0], )
        print("Hospital Name:", row[1])


def print_doctor_information(records):
    print('\n-----------------------')
    print('Información del Doctor')
    print('------------------------')
    for row in records:
        print("Doctor Id:", row[0])
        print("Doctor Name:", row[1])
        print("Hospital Id:", row[2])
        print("Specialty:", row[3])
