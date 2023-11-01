from fastapi import FastAPI, Body
import mysql.connector

# Configura la conexión a la base de datos
db_connection = mysql.connector.connect(
    host="sql.freedb.tech",
    user="freedb_rootdayler",
    password="cs$6sDcpHdtA84P",
    port="3306",
    database="freedb_platzi"
)
app =FastAPI()
app.title = "Mi aplicacion con fastAPI"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/')
def message():
    return "Hello world"

@app.get('/usuarios', tags=['usuarios'])
def get_users(): #devuelve el listado de las peliculas
    # Realiza una consulta SELECT a la base de datos
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    cursor.close()
    return result

@app.post('/usuario', tags=['registrar usuario'])
def post_user(id: str = Body(default="text"),
                 username: str = Body(default="text"),
                 name:str = Body(default="text")): #devuelve el listado de las peliculas
     # Realiza una consulta INSERT en la base de datos
    cursor = db_connection.cursor()
    insert_query = "INSERT INTO user (id, username, name) VALUES (%s, %s, %s)"
    insert_data = (id, username, name)
    cursor.execute(insert_query, insert_data)
    db_connection.commit()
    cursor.close()
    return {"mensaje": "Dato creado correctamente"}