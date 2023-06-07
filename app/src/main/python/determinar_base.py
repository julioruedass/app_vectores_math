from com.chaquo.python.console import ClaseDatosPythonJava as Datos
from sympy import Matrix, pprint, symbols, Eq, zeros,  init_printing
from sympy import latex

init_printing()
matr = []
#dato_1 =""
#dato_2 =""
#dato_3 =""

def array_to_LaTeX(arr):
    return latex(arr)

def crear_matrix_porvector(mat):
    cadena_vector= ""
    compo = Datos.componentes
    tam_vectores = Datos.tamano_vector
    print("vectores     : "  +  str(compo))
    print("tam vectores : "  +  str(tam_vectores))
    print("Matrix   : "  +  str(mat[0]))
    mimat =mat[0]
    for v in range(0,tam_vectores,1) :
        if cadena_vector=="":
            cadena_vector =""+ str(mimat[v])
        else:
            cadena_vector =cadena_vector+","+ str(mimat[v])
        print("VALOR DE VECTOR " + str(mimat[v]))
    return cadena_vector

def Matriz2(modo):
    tam_vectores = Datos.tamano_vector
    A = []
    STRING_VECTOR_1=""
    STRING_VECTOR_2=""
    STRING_VECTOR_3=""
    STRING_VECTOR_4=""
    AB1 = []
    AB2 = []
    AB3 = []
    AB4 = []
    GLOB =[]
    #CEROS =[]
    #LETRAS =[]
    CEROS =""
    LETRAS =""
    V1 = []
    V2 = []
    V3 = []
    V4 = []
    compo = Datos.componentes
    print("Matriz A original de vectores")
    pprint(compo)
    if compo > 0:
        V1.append(Matrix(Datos.d_vector1))
        STRING_VECTOR_1 =crear_matrix_porvector(V1)
        A.append(STRING_VECTOR_1.split(","))
        print("Vector 1  :")
        pprint(V1)
    if compo > 1:
        V2.append(Matrix(Datos.d_vector2))
        STRING_VECTOR_2 =crear_matrix_porvector(V2)
        A.append(STRING_VECTOR_2.split(","))
        print("Vector 2  :")
        pprint(V2)
    if compo > 2:
        V3.append(Matrix(Datos.d_vector3))
        STRING_VECTOR_3 =crear_matrix_porvector(V3)
        A.append(STRING_VECTOR_3.split(","))
        print("Vector 3  :")
        pprint(V3)
    if compo > 3:
        V4.append(Matrix(Datos.d_vector4))
        STRING_VECTOR_4 =crear_matrix_porvector(V4)
        A.append(STRING_VECTOR_4.split(","))
        print("Vector 4 :")
        pprint(V4)
        print(" ---------------- Iniciar -------------------------")
        Datos.vectoresentrada = array_to_LaTeX(A)
    try:
        if tam_vectores == 1:
            if (modo =="DETERMINANTE"):
                #CEROS =[0]
                CEROS ="0"
            if (modo =="GENERADOR"):
                #LETRAS =["w"]
                LETRAS="W"
        if tam_vectores == 2:
            if (modo =="DETERMINANTE"):
                #CEROS =[0,0]
                CEROS="0,0"
            if (modo =="GENERADOR"):
                #LETRAS =["w","x"]
                LETRAS="W,X"
        if tam_vectores == 3:
            if (modo =="DETERMINANTE"):
               # CEROS =[0,0,0]
                CEROS ="0,0,0"
            if (modo =="GENERADOR"):
                #LETRAS =["w","x","y"]
                LETRAS="W,X,Y"
        if tam_vectores == 4:
            if (modo =="DETERMINANTE"):
                #CEROS =[0,0,0,0]
                CEROS ="0,0,0,0"
            if (modo =="GENERADOR"):
                #LETRAS =["w","x","y"]
                LETRAS="W,X,Y,Z"
        copya = A.copy()
        if (modo =="DETERMINANTE"):
            copya.append(CEROS.split(","))
        if (modo =="GENERADOR"):
            copya.append(LETRAS.split(","))
        copya = Matrix(copya).T
        print("Si entro Matrix aumentada ")
    except:
        print("Matrix aumentada no valida")
        copya = A.copy()
        copya = Matrix(copya).T
    return A, compo,copya

def tamanosv (secuencia,tamanos) :
    acumulado = secuencia+1
    vectores  = tamanos[0]
    tamano    = tamanos[1]
    if secuencia > tamanos[0]:
        print("Es mayor el numero de vectores es menor: Secuencia: ",acumulado, " vectores ", vectores)
    if secuencia > tamanos[1]:
        print("Es mayor el numero de tamano  es menor : Secuencia: ",acumulado, "tamano:  ", tamano)

def validar_matrix(matrix_eva,punto1, punto2):
    try:
        valor = matrix_eva[punto1,punto2]
        print('Valor valido :' , valor)
        v_entrar='no'
    except IndexError:
        print('Valor invalido :' , 0)
        valor = 0
        v_entrar='si'
    except KeyError:
        print('Valor invalido :' , 0)
        valor = 0
        v_entrar='si'
    return valor,v_entrar


def matrix_aumentada(tipo,p_filas ,array_aumento):
    if tipo == 'ceros':
        if p_filas == 1:
            array_aumento = Matrix([['0']])
        if p_filas == 2:
            array_aumento = Matrix([['0'],['0']])
        if p_filas == 3:
            array_aumento = Matrix([['0'],['0'],['0']])
        if p_filas == 4:
            array_aumento = Matrix([['0'],['0'],['0'],['0']])
    elif tipo=='letras' :
        abc = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        array_aumento = Matrix(abc[-p_filas:])
    return array_aumento

def fun_max_tam_o_vec(p_dimenciones):
    if (p_dimenciones[0] == p_dimenciones[1]):
        return p_dimenciones[0],False,True
    elif (p_dimenciones[0] > p_dimenciones[1]):
        return p_dimenciones[1] , True,False
    elif (p_dimenciones[1] > p_dimenciones[0]):
        return p_dimenciones[0], False,True

def func_gauss(Matri,P_aumentada,metodo,arr_ceros):
    Mat_temp = Matrix(Matri)
    mtr_temp = Mat_temp.copy()
    Shape = mtr_temp.shape
    a_array = arr_ceros
    a_array_2 = a_array.copy()
    numero_linea = 0

    limite_menor = fun_max_tam_o_vec(Shape)
    mtx_no_cuad = limite_menor[1]
    # obtener ultmas letras dependiendo la diimension dela Matrix
    filas = Shape[0]
    if (limite_menor[1] == True):
        filas = limite_menor[0]
    columnas = Shape[1]
    conjunto = False
    print('filas: ', Shape[0], ',columnas: ', Shape[1])
    print("____________________________________________________________ ")
    mtr = Mat_temp
    Res = P_aumentada

    # Evaluar uno solo por medio de numero de vectores
    print("Permutacion de filas")
    for j in range(filas):
        # reinicio de valores de verificacion
        filas_2_arr = a_array_2.shape
        for ran in range(filas_2_arr[0]):
            a_array_2[ran] = 0
        validos_punto = 0

        if mtr[j, j] == 0:
            print("Posición: ", j + 1, ":", j + 1, " Es igual a cero requiere cambio")
            for i in range(Shape[0]):
                print(" Buscando lineas con el valor 1 en  fila: ", i)
                pprint(a_array[i])
                if mtr[i, j] != 0 and a_array[i] != 1:
                    print("Se puede cambiar la fila", j + 1, "por la fila", i + 1)
                    # Se incrementa en 1 cuando aplica para cambio
                    validos_punto += 1
                    # Se asigna 1 cuando aplica para cambio
                    a_array_2[i] = 1
                    numero_linea = i
                else:
                    print("No aplico para cambio")
            print("Vectores disponibles a cambio ", validos_punto)

            #evaluar si ay disponibles puntos para cambio de filas
            if (validos_punto == 1):
                # Verificar si esta disponible
                Res.row_swap(j, numero_linea)
                mtr.row_swap(j, numero_linea)
                dato_1 = "Se cambia la fila "+ str(j + 1)+" por la fila "+ str(numero_linea + 1)
                Datos.dinamicSetvalue(dato_1, array_to_LaTeX(mtr));
                pprint(mtr)
                print("")
                a_array[j] = 1
                # pprint(Res)
            #Evaluar si hay mas de dos puntos para cambio
            elif(validos_punto > 1):
                print("Tiene varias opciones :________ Posición: ", j + 1, ":", j + 1)
                in_vector = "n"
                num_vector=0
                for i in range(Shape[0]):
                    if a_array_2[i] == 1 and a_array[i] != 1 and  in_vector == "n":
                        num_vector=i
                        in_vector="s"
                        #for x in range(filas):
                        #    print("Las filas posbles para otras filas")
                        #    pprint(mtr[i, :])
                Res.row_swap(j, num_vector)
                mtr.row_swap(j, num_vector)
                dato_1 = "Se cambia la fila "+ str(j + 1)+" por la fila "+ str(num_vector + 1)
                Datos.dinamicSetvalue(dato_1, array_to_LaTeX(mtr) );
                a_array[j]=1
        else:
            a_array[j] = 1
            print("No se requeiere mover row :____________________ Posición: ", j + 1, ":", j + 1)
            # END  IF 1
        Res[j, :] = Res[j, :] * 1 / mtr[j, j]
        mtr[j, :] = mtr[j, :] * 1 / mtr[j, j]

        if mtr[j, j] != 1:  # IF 2
            print("2- Convertir el elemento", j + 1, ",", j + 1, "en 1")
            mat1 = str(j + 1)
            dato_1 = "Convertir el elemento " + mat1 +"   ,   "     + mat1 + " en 1 :"
            Res[j, :] = Res[j, :] * 1 / mtr[j, j]
            mtr[j, :] = mtr[j, :] * 1 / mtr[j, j]
            pprint(mtr)
            Datos.dinamicSetvalue(dato_1,array_to_LaTeX(mtr) );
            print("")
            pprint(Res)
            Datos.dinamicSetvalue("Columna agregada:", array_to_LaTeX(Res) );
        else:
            mat1 = j +1
            print("3- El elemento", j + 1, ",", j + 1, "ya es 1")
            dato_1 = "El elemento " + str(mat1) +", " + str(mat1) + " ya es 1"
            Datos.dinamicSetvalue(dato_1, "");
        # END  IF 2

        # if ((j +1 ) > Shape[1]):
        #   tamanosv(j,Shape)
        #   print('punto log 4 :Validacion de tamaños de secuencia ')
        # else:
        tamanosv(j, Shape)
        for i in range(j + 1, filas):  # Cambio por diferencia de dimenciones
            # for i in range(j + 1, Shape[1]):  # cambio de pruebas
            print("Punto log 4 :  j:", j, " i :", i)
            if mtr[i, j] != 0:
                print("4- Convertir el elemento", i + 1, ",", j + 1, "en 0")
                mat1 = str(i + 1)
                mat2 = str(j + 1)
                dato_1 = "Convertir el elemento " + mat1 +" , " + mat2 + " en 0"
                Datos.dinamicSetvalue(dato_1, "");
                Res[i, :] = Res[i, :] - (Res[j, :] * mtr[i, j])
                mtr[i, :] = mtr[i, :] - (mtr[j, :] * mtr[i, j])
                pprint(mtr)
                print("")
                pprint(Res)
            else:
                print("5- El elemento", i + 1, ",", j + 1, " ya es 0")
                mat1 = str(i + 1)
                mat2 = str(j + 1)
                dato_1 = "El elemento " + mat1 +"   ,   "     + mat2 + " ya es 0"
                Datos.dinamicSetvalue(dato_1, "");
    # END FOR 1
    #INICIO FOR 2
    # Evaluar uno solo por medio de numero de tamaño
    for j in range(Shape[0] - 1, -1, -1):  #cambio shape JR
        print("Punto log:  6")
        tamanosv(j,Shape)
        print("matrix")
        pprint(mtr)
        print("respuesta")
        pprint(Res)
        print("___-___-____-____")
        for i in range(j - 1, -1, -1):
            valor_mult = validar_matrix(mtr, i, j)
            if valor_mult[0] != 0 or valor_mult[1] == 'si' :
                print("6- Convertir el elemento", i + 1, ",", j + 1, "en 0")
                print("")
                mat1 = str(i + 1)
                mat2 = str(j + 1)
                dato_1 = "Convertir el elemento " + mat1 +"   ,   "     + mat2 + " en 0"
                Datos.dinamicSetvalue(dato_1, "");
                #Res[i, :] = Res[i, :] - (Res[j, :] * mtr[i, j])
                #mtr[i, :] = mtr[i, :] - (mtr[j, :] * mtr[i, j])
                Res[i, :] = Res[i, :] - (Res[j, :] * valor_mult[0])
                mtr[i, :] = mtr[i, :] - (mtr[j, :] * valor_mult[0])
                pprint(mtr)
                print("")
                pprint(Res)
                Datos.dinamicSetvalue("",array_to_LaTeX(mtr) );
                Datos.dinamicSetvalue("",array_to_LaTeX(Res) );
            else:
                print("7- El elemento", i + 1, ",", j + 1, "ya es 0")
                mat1 = str(i + 1)
                mat2 = str(j + 1)
                dato_1 = "El elemento " + mat1 +"   ,   "     + mat2 + " ya es 0"
                Datos.dinamicSetvalue(dato_1, "");
    #END FOR 2

    a = []
    #INICIO FOR 3
    for i in range(Shape[0]):
        a.append((symbols(f"a{i + 1}"), Res[i]))
        #END FOR 3
        #Resultados
    print("Resultados (Soluciones):")
    Datos.dinamicSetvalue("Resultados (Soluciones):", "");
    for i in range(Shape[0]):
        print("Iterando: ",i)
        a[i] = Eq(a[i][0], a[i][1])
        pprint(a[i])
        dato_1 = array_to_LaTeX(a[i])
        Datos.dinamicSetvalue("", dato_1);
    matrizcomparacion = Matrix.eye(filas)
    print("Matrix (identidad):")
    pprint(Matrix( [Matrix([matrizcomparacion])]))
    print("Comparar con")
    pprint(Matrix( [Matrix([mtr[:filas,:filas]]) ] ))
    print("")
    # Setear Ceros filar sobrantes (vectores sobrantes)
    if (limite_menor[1] == True):
        for i in range(limite_menor[1]+1, Shape[0], 1):
            mtr[i, :] = mtr[filas, :] + ( mtr[filas, :]* (-1))
    # Setear Ceros columnas sobrantes (vectores sobrantes)
    elif (Shape[1]>Shape[0] and limite_menor[1] == False ):
        for i in range(limite_menor[1]+2, Shape[1], 1):
            print("Secuencia de seteo de columnas: ",i)
            pprint(mtr[:, i])
            mtr[:, i] = mtr[:, filas] + ( mtr[:, filas]* (-1))
    dato_1="Matrix resultado:"
    Datos.dinamicSetvalue(dato_1,array_to_LaTeX(mtr) );
    # Validaciones de generador
    if (metodo == "GEN"):
        if (limite_menor[1] == True):
            conjunto = False
            Datos.valida_base =0
            print("El conjunto generador NO genera base")
            dato_1 = "El conjunto de vectores NO genera a R" + str( Datos.tamano_vector)
            Datos.dinamicSetvalue(dato_1,"" );
        else:
            if mtr[:filas, :filas] == matrizcomparacion:
                conjunto = True
                Datos.valida_base =1
                print("El conjunto generador SI genera base R",filas)
                dato_1 = "El conjunto de vectores si genera a R" + str( Datos.tamano_vector)
                Datos.dinamicSetvalue(dato_1,"" );
            else:
                conjunto = False
                Datos.valida_base =0
                print("El conjunto generador NO genera base")
                dato_1 = "El conjunto de vectores NO genera a R" + str( Datos.tamano_vector)
                Datos.dinamicSetvalue(dato_1,"" );
    else:
        #Cuando evalua determinante
        if mtr[:filas,:filas] == matrizcomparacion:
            conjunto = True
            print("Es linealmente independiente" )
            dato_1 = "Es linealmente independiente"
            Datos.dinamicSetvalue(dato_1,"" );
        else:
            conjunto = False
            print("Es linealmente dependiente")
            dato_1 = "Es linealmente dependiente"
            Datos.dinamicSetvalue(dato_1,"" );
    return mtr, Res, a, conjunto, mtx_no_cuad

def llamada_determinante(Matric):
    Mat_temp = Matrix(Matric)
    Shape = Mat_temp.shape
    filas = Shape[0]
    print("matrix entrada")
    pprint(Mat_temp)
    B =[]
    B = matrix_aumentada('ceros',filas,B)
    C =[]
    C = matrix_aumentada('ceros',filas,C)
    print("_______________________-______   llamada Determinante _______-___________________________")
    gener = func_gauss(Matric,B,"DET",C)
    print("___________________________-______   Parámetro 0   _______-______________________________")
    pprint(gener[0])
    return gener[3],gener[4]

def llamada_generador(Matric):
    Mat_temp = Matrix(Matric)
    Shape = Mat_temp.shape
    filas = Shape[0]
    print("matrix entrada")
    pprint(Mat_temp)
    B =[]
    B = matrix_aumentada('letras',filas,B)
    C =[]
    C = matrix_aumentada('ceros',filas,C)
    print("_______________________-______   llamada Generador _______-___________________________")
    gener = func_gauss(Matric,B,"GEN",C)
    print("___________________________-______   Parámetro 0   _______-______________________________")
    pprint(gener[0])


def lineal_dependiente():
    try:
        Datos.itera_vector =0
        Datos.secuencia = 0
        matr2,tam,mat_aum = Matriz2("DETERMINANTE")
        nm =Matrix(matr2).T
        Datos.dinamicSetvalue("Matrix :",array_to_LaTeX(Matrix(mat_aum)) );

        matr3,tam2,mat_aum2 = Matriz2("GENERADOR")
        nm2 =Matrix(matr2).T

        print("Iniciar validaciòn")
        pprint(nm)
        try:
            dato_1 = "    Iniciar Determinante"
            Datos.dinamicSetvalue(dato_1,"" );
            resultado=llamada_determinante(nm)
        except:
            print('Ocurrio un error en función de determinante ')
            dato_1 = "Ocurrio un error en función de determinante"
            Datos.dinamicSetvalue(dato_1,"" );
            Datos.valida_base =0
        if  resultado[0] == True and resultado[1] == False :
            try:
                dato_1 = "    Iniciar Generador"
                Datos.dinamicSetvalue(dato_1,"" );
                Datos.dinamicSetvalue("Matrix :",array_to_LaTeX(Matrix(mat_aum2)) );
                llamada_generador(nm2)
            except:
                print('Ocurrio un error en función de generador ')
                dato_1 = "Ocurrio un error en función de generador"
                Datos.dinamicSetvalue(dato_1,"" );
                Datos.valida_base =0
        else:
            dato_1 = "   Iniciar Generador"
            Datos.dinamicSetvalue(dato_1,"" );
            if resultado[1] == True:
                print("El numero de vectores es mayor que el tamaño  del conjunto generador")
                dato_1 = "La relaciòn de # Vectores y con el tamaño de vectores es invalida"
                Datos.dinamicSetvalue(dato_1,"" );
            print("El conjunto generador NO genera base")
            dato_1 = "El conjunto generador NO genera base"
            Datos.dinamicSetvalue(dato_1,"" );
            Datos.valida_base =0
    except:
        print('Ocurrio un evento con el manejo de vectores ')
        dato_1 = "Ocurrio un evento con el manejo de vectores "
        Datos.dinamicSetvalue(dato_1,"" );
        Datos.valida_base =0


#solo en pycharm se usa
#respuesta = lineal_dependiente()