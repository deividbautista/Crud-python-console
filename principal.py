
from BD.conexion import DAO
import funciones

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

def ejecutarOpcion(opcion):
    dao = DAO()
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
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ha ocurrido un ERNO...")
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

menuPrincipal()