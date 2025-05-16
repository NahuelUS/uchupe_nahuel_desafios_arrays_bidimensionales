
def desplegar_menu ()->None:
    print("----------Bienvenido al menu interactivo de secuencias:----------\n\n")
    print("-Tiene diferentes opciones para elegir:\n\n"
          "1)Ingreso de la matriz.\n"
          "2)Verificar la existencia de secuencias de números consecutivos pares.\n"
          "3)Determinar la cantidad de ocurrencias.\n"
          "4)Identificar la secuencia más corta.\n"
          "5)Identificar la secuencia más larga.\n"
          "6)SALIR DEL PROGRAMA.\n\n")  

def inicializar_matriz (filas:int,colum:int)->list:
    matriz=[]
    for i in range(filas):
        fil=[0]*colum
        matriz+=[fil]
    return matriz     

def cargar_matriz (matriz:list)->None:
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz[i][j]=int(input(f"\nIngrese el valor para la fila {i+1} columna {j+1}: "))


def verificar_pares(matriz: list) -> bool:
    for i in range(len(matriz)):
        for j in range(len(matriz[i]) - 1):
            if matriz[i][j] % 2 == 0 and matriz[i][j + 1] % 2 == 0:
                return True
    return False          

def contar_pares (matriz:list)->int:
    tot_sec=0
    for i in range(len(matriz)):
        j=0
        while j<len(matriz[i])-1:
            if (matriz[i][j]%2==0) and (matriz[i][j+1]%2==0):
                inicio=j
                j+=2
                while j<(len(matriz[i])) and (matriz[i][j]%2==0):
                    j+=1
                fin=j
                cant=fin-inicio
                if cant>=2:
                    tot_sec+=1
            else:
                j+=1        
    return tot_sec

def identificar_mas_corto (matriz:list)->list:
    aux=[0]*15
    band=True
    min_lar=0
    for i in range(len(matriz)):
        j=0
        while j<len(matriz[i])-1:
            if (matriz[i][j]%2==0) and (matriz[i][j+1]%2==0):
                inicio=j
                j+=2
                while j<(len(matriz[i])) and (matriz[i][j]%2==0):
                    j+=1
                fin=j
                cant=fin-inicio
                if band:
                    for k in range(cant):
                        aux[k]=matriz[i][inicio+k]
                    min_lar=cant
                    band=False
                elif min_lar>cant:
                    for k in range(cant):
                        aux[k]=matriz[i][inicio+k]
                    min_lar=cant

            else:
                j+=1        
    return aux[:min_lar]

def identificar_mas_largo (matriz:list)->list:
    aux=[0]*20
    band=True
    max_lar=0
    for i in range(len(matriz)):
        j=0
        while j<len(matriz[i])-1:
            if (matriz[i][j]%2==0) and (matriz[i][j+1]%2==0):
                inicio=j
                j+=2
                while j<(len(matriz[i])) and (matriz[i][j]%2==0):
                    j+=1
                fin=j
                cant=fin-inicio
                if band:
                    for k in range(cant):
                        aux[k]=matriz[i][inicio+k]
                    max_lar=cant
                    band=False
                elif max_lar<cant:
                    for k in range(cant):
                        aux[k]=matriz[i][inicio+k]
                    max_lar=cant

            else:
                j+=1        
    return aux[:max_lar]









