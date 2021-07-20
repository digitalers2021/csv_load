import sys
import csv
import sqlite3


def generar_csv(nombre_archivo):

    rows = []
    csvfile = open(nombre_archivo, "r")
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader.__next__()
    for row in reader:
        rows.append(row)

    csvfile.close()
    return rows


def create_table(cursor):
    tabla = """
    CREATE TABLE IF NOT EXISTS "pasajeros" 
    (	
        "id" NUMBER NOT NULL PRIMARY KEY, 
        "sobrevivio" NUMBER, 
        "class" NUMBER, 
        "nombre" TEXT, 
        "genero" TEXT,
        "edad" NUMBER
        );
    """
    cursor.execute(tabla)


def insertar_datos(data, conn, cursor):
    """ Inserto datos en la tabla pasajero
    """
    for row in data:
        sql_pasajero = '''INSERT INTO pasajeros(id, sobrevivio, class, nombre, genero, edad)
                    VALUES(?, ?, ?, ?, ?, ?)'''

        cursor.execute(sql_pasajero, row[:6])
        print(f"Insertando pasajero {row[3]}")

    conn.commit()


def count_sobrevivientes(cur, sobrevivio=1):
    query = f"select count(*) from pasajeros where sobrevivio={sobrevivio};"
    iterable = cur.execute(query)

    rsp = cur.fetchone()

    return rsp[0]


def print_rows(data, limit):
    for x in csv_data[:limit]:
        print(x)


# Abro y proceso csv file
nombre_archivo = sys.argv[1]
csv_data = generar_csv(nombre_archivo)


# Genero mi base de datos sqlite
conn = sqlite3.connect("titanic.db")
cursor = conn.cursor()

# Creo la tabla para titanic
create_table(cursor)

# Inserto los datos
# insertar_datos(csv_data, conn, cursor)

resultado = count_sobrevivientes(cursor)
print("Los sobrevivientes fueron en total: ", resultado)

conn.close()
