import random

def inicializar_matriz (filas:int,colum:int,inicial:any=0)->list:
    """
    """
    matriz= []
    
    
    for i in range (filas):
        fila=[inicial]*colum
        matriz+= [fila]

    return matriz





def ingresar_valores_matriz (matriz:list,num:int)->list:
    total=num*num
    rep=[0]*total
    rep_cont=0
    
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            y=int(input(f"\nIngrese un valor para la fila {i} columna {j} (acuerdese que tiene que ingresar valores NO repetidos" 
                                   f"desde el 1 hasta el {total}): "))
            while y<1 or y>total or y in rep:
                print("\nERROR: Numero fuera de rango o repetido...")
                y=int(input(f"Ingrese nuevamente un valor para la fila {i} columna {j} (acuerdese que tiene que ingresar valores NO repetidos" 
                                   f"desde el 1 hasta el {total}): "))
            matriz[i][j]=y     
            rep[rep_cont]=y
            rep_cont+=1

    return matriz


def generar_aleatorio (matriz:list,num:int)->list:
    total=num*num
    array=[0]*total
    cont=0

    while cont<total:
        x=random.randint(1,total)
        band=False
        for i in range (cont):
            if array[i]==x:
                band=True
                break
        if not band:
            array[cont]=x
            cont+=1

    k=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=array[k]
            k+=1

    return matriz                    


def validar_matriz (matriz:list,num:int)->bool:
    cons=(num*((num*num)+1))//2
    #filas
    for i in range(num):
        sumar_filas=0
        for j in range(num):
            sumar_filas+=matriz[i][j]
        if sumar_filas!=cons:
            return False
    #columnas
    for i in range(num):
        sumar_col=0
        for j in range(num):
            sumar_col+=matriz[j][i]
        if sumar_col!=cons:
            return False         
    #diagonal principal
    sumar_diag=0
    for i in range(num):
        sumar_diag+=matriz[i][i]
    if sumar_diag!=cons:
        return False    


    #diagonal secundaria
    sumar_sec=0
    for i in range(num):
        sumar_sec+=matriz[i][num-i-1]
    if sumar_sec!=cons:
        return False

    return True        


def mostrar_matriz (matriz:list)->any:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x=matriz[i][j]
            print(x,end=" ")