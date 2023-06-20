
#------------------------------------------------------------------------------------
# El presente código posee la finalidad de aprender y practicar conocimientos intermedios 
# del lenguaje de programación python y en ningún momento se pretende monetizar o hacer apropiación del trabajo del autor original.
#------------------------------------------------------------------------------------

# Código sustraido del canal: UskoKruM2010 / link-video: https://youtu.be/d3mYv1r4DkQ 
# link-repositorio: https://github.com/UskoKruM/app_consola_crud_python_mysql

# En este primer apartado realizamos la importación de las funciones que utilizaremos a lo largo del código.
import mysql.connector
from mysql.connector import Error

# Clase principal de conexión de la base de datos.
class DAO():
    # Defiinimos el constructor init para inicializar la variable con los valores requeridos.
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='crud-console'
            )
        except Error as ex:
            print("Error al intentar conectar : {0}".format(ex))
    
    # Definimos la varible con la consulta necesaria para poder seleccionar todos los elementos almacenados en la base de datos.
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar conectar : {0}".format(ex))

    # Definimos la variable con la consulta para registrar cursos en la base de datos.
    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO curso (codigo,nombre,creditos) VALUES ('{0}','{1}',{2})"
                cursor.execute(sql.format(curso[0],curso[1],curso[2]))
                self.conexion.commit()
                print("¡Curso registrado exitosamente UwU!")
            except Error as ex:
                print("Error al intentar conectar : {0}".format(ex))

    # Definimos la variable con la consulta para actualizar los atributos de un curso en especifico.
    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE curso SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1],curso[2],curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar conectar : {0}".format(ex))

    # Definir la variable con la consulta para eliminar un curso de la base de datos.
    def eliminarCurso(self,codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado exitosamente 7w7!")
            except Error as ex:
                print("Error al intentar conectar : {0}".format(ex))