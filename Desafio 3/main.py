from paquetes.funciones3 import*


fir_st=True
aleatorio=False
carg=False

while True:
    desplegar_menu()
    x=int(input("\nIngrese la opcion a elegir: "))
    while x<1 or x>6:
        x=int(input("\nERROR: Ingrese una opcion valida: "))
    if x==6:
        print("\n\nGRACIAS: SALIENDO DEL PROGRAMA.....")
        break  
    if x!=1 and fir_st==True:
        print("ERROR: DEBE CARGAR LA MATRIZ ANTES DE ELEGIR OTRA OPCION.....")
        continue    
    if x==1:
        opc=int(input("\nIngrese (1) si quiere ingresar la matriz manualmente, ingrese (2) si quiere una matriz aleatoria: "))
        while opc!=1 and opc!=2:
            opc=int(input("\nERROR, VALOR INVALIDO: Ingrese (1) matriz manualmente, ingrese (2) matriz aleatoria: "))
        match opc:
            case 1:
                fil=int(input("\nIngrese el numero de filas: "))
                col=int(input("Ingrese el numero de columnas: "))
                matriz=inicializar_matriz(fil,col)
                cargar_matriz(matriz)
                carg=True
                aleatorio=False
                fir_st=False
            case 2:
                matriz_ale=[[2,4,6,7],[68,70,345,66],[0,1,8,10]]
                aleatorio=True   
                carg=False
                fir_st=False
        continue        
    if x==2:
        if carg:
            ver=verificar_pares(matriz)
            if ver:
                print("\n\n★★★ EXISTEN NUMEROS CONSECUTIVOS PARES ★★★\n\n")
            else:
                print("\n\n↓↓↓ NO EXISTEN NUMEROS CONSECUTIVOS PARES ↓↓↓\n\n")
            continue        
        elif aleatorio:
            ver_al=verificar_pares(matriz_ale)
            if ver_al:
                print("\n\n★★★ EXISTEN NUMEROS CONSECUTIVOS PARES ★★★\n\n")
            else:
                print("\n\n↓↓↓ NO EXISTEN NUMEROS CONSECUTIVOS PARES ↓↓↓\n\n")
            continue        
    if x==3:
        if carg:
            numero_secuencias=contar_pares(matriz)
            print(f"\nHAY {numero_secuencias} DE SECUENCIAS CONTADAS\n")
            continue
        elif aleatorio:
            numero_secuencias=contar_pares(matriz_ale)
            print(f"\nHAY {numero_secuencias} DE SECUENCIAS CONTADAS\n")
            continue
    if x==4:
        if carg:
            vec_men=identificar_mas_corto(matriz)
            print(f"\n\nLa secuencia mas corta la componen {len(vec_men)} numeros.")
            print("Los numeros son: ",end="")
            for i in range(len(vec_men)):
                print(vec_men[i],end=" ")
            print()
            continue
        elif aleatorio:
            vec_men=identificar_mas_corto(matriz_ale)
            print(f"\n\nLa secuencia mas corta la componen {len(vec_men)} numeros.")
            print("Los numeros son: ",end="")
            for i in range(len(vec_men)):
                print(vec_men[i],end=" ")
            print()
            continue
    if x==5:
        if carg:
            vec_may=identificar_mas_largo(matriz)
            print(f"\n\nLa secuencia mas larga la componen {len(vec_may)} numeros.")
            print("Los numeros son: ",end="")
            for i in range(len(vec_may)):
                print(vec_may[i],end=" ")
            print()
            continue
        elif aleatorio:
            vec_may=identificar_mas_largo(matriz_ale)
            print(f"\n\nLa secuencia mas larga la componen {len(vec_may)} numeros.")
            print("Los numeros son: ",end="")
            for i in range(len(vec_may)):
                print(vec_may[i],end=" ")
            print()
            continue