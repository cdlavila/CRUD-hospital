from CRUD import ICrud
import mysql.connector
from Persistence import connection as cn


class ImpCrudHospital(ICrud.ICrud):
    def find(self, **kwargs):
        try:
            connection = cn.get_connection()
            cursor = connection.cursor()
            select_query = """select * from Hospital where Hospital_name = %s"""
            cursor.execute(select_query, (kwargs['hospital_name'],))
            records = cursor.fetchall()
            print(records)
            cn.close_connection(connection)
        except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)

        return records
