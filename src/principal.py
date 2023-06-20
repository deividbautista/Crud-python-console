
#------------------------------------------------------------------------------------
# El presente código posee la finalidad de aprender y practicar conocimientos intermedios 
# del lenguaje de programación python y en ningún momento se pretende monetizar o hacer apropiación del trabajo del autor original.
#------------------------------------------------------------------------------------

# Código sustraido del canal: UskoKruM2010 / link-video: https://youtu.be/d3mYv1r4DkQ 
# link-repositorio: https://github.com/UskoKruM/app_consola_crud_python_mysql

# En este primer apartado realizamos la importación de las funciones que utilizaremos a lo largo del código.
from BD.conexion import DAO
import funciones

#-----------------------------------------------------
# Apartado de menú principal.
#-----------------------------------------------------
def menuPrincipal():
    continuar = True 
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("----------------MENU PRNCIPAL----------------")
            print("-1- Listar cursos")
            print("-2- Registrar curso")
            print("-3- Actualizar curso")
            print("-4- Eliminar curso")
            print("-5- Salir")
            print("---------------------------------------------")
            opcion =int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, digite un valor valido...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

#-----------------------------------------------------
# Apartado donde se encontraran las distintas funcionalidades de la matriz CRUD.
#-----------------------------------------------------
def ejecutarOpcion(opcion):

    # Vairable principal que guarda la conexión de la base de datos.
    dao = DAO()

    # Primera opción donde se enlistan e imprimen todos los cursos presentes en la base de datos.
    if opcion == 1:
        print("----------_----------")
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ha ocurrido un ERNO...")
    
    # Segunda opción donde se realizara registro de un nuevo curso con datos expedidos por el usuario.
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ha ocurrido un ERNO...")

    # Tercera opción en la que se actualizaran los atributos del curso seleccionado con datos expedidos por el usuario.
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualización(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("Codigo de curso no encontrado TnT...")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ha ocurrido un ERNO...")

    # Cuarta opción la cual eliminara el curso seleccionado por medio del numero del codigo de este.
    elif opcion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("\n---------------------------------------------------------------------------------")
                    print("Código de curso no encontrado\ncompruebe que esta digitando el código correcto...")
                    print("---------------------------------------------------------------------------------\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ha ocurrido un ERNO...")
    else:
        print("Opción no valida papu")

# Retornamos el menu principal despues de realizar la función requerida por elusuario, para mantener el bucle.
menuPrincipal()