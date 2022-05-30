from UI import interface
from CRUD import ImpCrudDoctor
from CRUD import ImpCrudHospital


interface.heading()
option = interface.main_menu()

crud_hospital = ImpCrudHospital.ImpCrudHospital()
crud_doctor = ImpCrudDoctor.ImpCrudDoctor()

if option == '1':
    hospital_name = interface.input_hospital_name()
    records = crud_hospital.find(hospital_name=hospital_name)
    interface.print_hospital_information(records)
elif option == '2':
    doctor_id = interface.input_doctor_id()
    records = crud_doctor.find(doctor_id=doctor_id)
    interface.print_doctor_information(records)
else:
    print('Opción no válida')
