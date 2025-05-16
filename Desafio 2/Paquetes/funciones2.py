

def desplegar_menu ()->None:
    print("----------Bienvenido al menu interactivo de nuestra empresa:----------\n\n")
    print("-Tiene diferentes opciones para elegir:\n\n"
          "1)Cargar planilla de recaudacion.\n"
          "2)Mostrar la recaudación de cada coche y línea.\n"
          "3)Calcular y mostrar la recaudación por línea.\n"
          "4)Calcular y mostrar la recaudación por coche.\n"
          "5)Calcular y mostrar la recaudación total.\n"
          "6)SALIR DEL PROGRAMA.\n")  


def generar_legajo ()->list:
    matriz=[[101,102,103,104,105],
            [201,202,203,204,205],
            [301,302,303,304,305]]
    
    return matriz

def validar_legajo(num:int)->bool:
    matriz_legajo=generar_legajo()
    for i in range(len(matriz_legajo)):
        for j in range(len(matriz_legajo[i])):
            if matriz_legajo[i][j]==num:
                return True
    return False      

def inicializar_planilla(filas:int=3,colum:int=5,val:int=0)->list:
    matriz=[]
    for i in range(filas):
        fila=[val]*colum
        matriz+=[fila]
    return matriz

def cargar_planilla (matriz:list)->None:
    seguir= "s"
    while seguir=="s":
        lin=int(input("\nIngrese la linea (1 al 3): "))
        while lin<1 or lin>3:
            lin=int(input("ERROR: Ingrese una linea VALIDA (1 al 3): "))
        coc=int(input("\nIngrese el coche (1 al 5): "))
        while coc<1 or coc>5:    
            coc=int(input("ERROR: Ingrese un coche VALIDO (1 al 5): "))
        rec=int(input("\nIngresar la recaudacion del viaje: $"))
        while rec<=0:
            rec=int(input("ERROR: Ingresar una recaudacion VALIDA del viaje: $"))
        matriz[lin-1][coc-1]+=rec
        seguir=input("\n\n¿DESEA CONTINUAR? (s/n): ") 
          
def mostrar_cada_coche_linea (matriz:list)->None:
    print()
    print("        C1   C2   C3   C4   C5")
    for i in range (len(matriz)):
        print(f"Linea {i+1}",end=" ")
        for j in range(len(matriz[i])):
            print(f"${matriz[i][j]}",end=" ")
        print()    
    
def calcular_mostrar_linea (matriz:list)->None:
    linea_total=0
    print("\n↓↓↓ RECAUDACION POR LINEA ↓↓↓\n")
    for i in range(len(matriz)):
        print(f"Linea {i+1}:",end=" ")
        for j in range(len(matriz[i])):
            linea_total+=matriz[i][j]
        print(f"${linea_total}")
        linea_total=0    
    print()

def calcular_mostrar_coche (matriz:list)->None:
    coche_total=0
    print("\n↓↓↓ RECAUDACION POR COCHE ↓↓↓\n")
    for i in range(len(matriz[0])):
        print(f"Coche {i+1}:",end=" ")
        for j in range(len(matriz)):
            coche_total+=matriz[j][i]
        print(f"${coche_total}")
        coche_total=0    
    print()    


def mostrar_total (matriz:list)->None:
    sumatoria_total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sumatoria_total+=matriz[i][j] 
    print("\n----------------------------------------------------------------------")        
    print(f"★ EL TOTAL GENERAL DE TODAS LAS RECAUDACIONES REGISTRADAS ES: ${sumatoria_total} ★")    
    print("----------------------------------------------------------------------\n")        