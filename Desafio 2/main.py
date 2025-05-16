from Paquetes.funciones2 import *

fir_st=True

while True:
    desplegar_menu()
    x=int(input("\nIngrese la opcion a elegir: "))
    while x<1 or x>6:
        x=int(input("\nERROR: Ingrese una opcion valida: "))
    if x==6:
        print("\n\nGRACIAS: SALIENDO DEL PROGRAMA.....")
        break  
    if x!=1 and fir_st==True:
        print("ERROR: DEBE CARGAR LA PLANILLA DE RECAUDACIONES PRIMERO ANTES DE ELEGIR OTRA OPCION.")
        continue
    if x==1:
        num=int(input("\nIngrese su numero de legajo: "))
        cart=validar_legajo(num)
        if cart:
            if fir_st:
                print("\nLegajo VALIDO: INGRESANDO.....\n")
                matriz_plan=inicializar_planilla()
                fir_st=False
            cargar_planilla(matriz_plan)
            continue
        else:
            print("\nLegajo INVALIDO.")
            continue   
    if x==2:
        mostrar_cada_coche_linea(matriz_plan)
        continue
    if x==3:
        calcular_mostrar_linea(matriz_plan)
        continue
    if x==4:
        calcular_mostrar_coche(matriz_plan)
        continue
    if x==5:
        mostrar_total(matriz_plan)
        continue
