import pyodbc

def dbConnect(username, password, server, database):
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            #'Trusted_Connection=yes;'  #Solo se ultiliza con autenticacion de Windows, caso sql va no
        )
        return pyodbc.connect(connection_string)
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    
"""
#Conexion a sql server
import pyodbc

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=Taller;'
    'Trusted_Connection=yes;'  #Solo se ultiliza con autenticacion de Windows, caso sql va no
    #'UID=GOATJR;'  #user
    #'PWD=1209;'    #contra
)

try:
    #Estableciendo conexion a la base
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()    #objeto que permite interactuar con la base de datos (ejecuta consultas y recupera resultados)

    #Consulta
    cursor.execute('SELECT * FROM Personas')   

    #Mostrar los resulatdos
    for row in cursor:
        print(row)

except pyodbc.Error as e:
    print("Error al coectarse a la DB", e   )

finally: 
    if connection:
        connection.close()
"""
