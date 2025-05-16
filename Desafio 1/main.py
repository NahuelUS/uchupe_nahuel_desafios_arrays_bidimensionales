from Paquete.Funciones import *


x=int(input("Ingrese usted la cantidad de filas (recuerde que es un cuadrado): "))
y=int(input("Ingrese usted la cantidad de columnas (recuerde que es un cuadrado): "))
while y!=x:
    x=int(input("\nERROR: NO Ingreso filas y columnas iguales, vuelva a intentarlo, filas (recuerde que es un cuadrado): "))
    y=int(input("columnas: "))

matriz=inicializar_matriz(x,y)

z=int(input("\nElija una opcion: ¿Quiere generar usted la matriz (1) o que se genere aleatoriamente (0)?: "))

while z!=1 and z!=0:
    z=int(input("ERROR: Ingrese una opcion valida: "))

if z==1:
    cuadrado=ingresar_valores_matriz(matriz,x)
    band=validar_matriz(cuadrado,x)
    if band:
        mostrar_matriz(cuadrado)
        print(f"\n\nLa matriz es de {x}x{x} y ES UN CUADRADO PERFECTO\n\n")
    else:
         mostrar_matriz(cuadrado)
         print(f"\n\nLa matriz es de {x}x{x} y NO es un cuadrado perfecto\n\n")
else:
    cuadrado=generar_aleatorio(matriz,x)
    band=validar_matriz(cuadrado,x)
    if band:
        mostrar_matriz(cuadrado)
        print(f"\n\nLa matriz es de {x}x{x} y ES UN CUADRADO PERFECTO\n\n")
    else:
         mostrar_matriz(cuadrado)
         print(f"\n\nLa matriz es de {x}x{x} y NO es un cuadrado perfecto\n\n")