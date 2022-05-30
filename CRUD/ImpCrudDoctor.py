from CRUD import ICrud
import mysql.connector
from Persistence import connection as cn


class ImpCrudDoctor(ICrud.ICrud):
    def find(self, **kwargs):
        try:
            connection = cn.get_connection()
            cursor = connection.cursor()
            select_query = """select * from Doctor where Doctor_Id = %s"""
            cursor.execute(select_query, (kwargs['doctor_id'],))
            records = cursor.fetchall()
            cn.close_connection(connection)
        except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)

        return records
