def listarCursos(cursos):
    print("Cursos: ")
    contador = 1
    for cur in cursos:
        datos = "{0} | Codigo: {1} | Nombre: {2} ({3} Créditos)"
        print(datos.format(contador, cur[0], cur[1], cur [2]))
        contador += 1
    print(" ")

def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo=input("Ingrese codigo: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 digitos.")

    nombre=input("Ingrese nombre: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if(int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben de ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe se ser un valor númerico, no se permiten caracteres, decimales o negativos.")

    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualización(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre=input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                if(int(creditos) > 0):
                    creditosCorrecto = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben de ser mayor a 0.")
            else:
                print("Créditos incorrectos: Debe se ser un valor númerico, no se permiten caracteres, decimales o negativos.")

        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None
    
    return curso

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar =""

    return codigoEliminar