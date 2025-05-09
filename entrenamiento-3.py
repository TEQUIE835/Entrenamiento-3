import sys
#definimos una funcion para agregar productos
def agregar(inv, nom, prec, cant):
    for prod in inv:
        if prod["nombre"].lower().strip() == nom.lower().strip():
            print(f"Producto {nom} esta en el inventario")
    inv.append({"nombre": nom, "precio": prec, "cantidad" : cant})
    print(f"\nEl producto '{nom}' ha sido agregado\n")
    return inv

#Definimos una funcion para consultar o buscar un producto
def buscar(inv, nom):
    for prod in inv:
        if prod["nombre"].lower() == nom.lower():
            return prod
    print(f"\nProducto {nom} no encontrado")
    return None

#Creamos una funcion para actualizar el precio
def actprec(inv,nom,precn):
    for prod in inv:
        if prod["nombre"].lower() == nom.lower():
            prod["precio"] = precn
            print(f"Precio de '{nom} actualizado a '{precn}'\n")
            return
    print(f"\nProducto '{nom}' no encontrado")
        
#Creamos una funcion para actualizar la cantidad
def actcant(inv, nom,cantn):
    for prod in inv:
        if prod["nombre"].lower() == nom.lower():
            prod["cantidad"] = cantn
            print(f"\nCantidad de '{nom}' ha sido actualizada")
            return
        print(f"\nProducto '{nom}' ha sido actualizado")

#Creamos una funcion para limpiar el inventario
def limp(inv):
    inv.clear()
    print("El inventario ha sido limpiado\n")
    return

#Creamos una funcion para eliminar producctos
def elim(inv,nom):
    for i,prod in enumerate(inv):
        if prod["nombre"].lower() == nom.lower():
            del inv[i]
            print(f"\nproducto {nom} eliminado exitosamente")
            return
    print(f"\nproducto {nom} no encontrado")


#Creamos una funcion para calcular el valor total con un lambda
def tot(inv):
    total= sum(map(lambda x: x["precio"] * x["cantidad"], inv))
    return total

#Creare una funcion para leer el inventario completo
def most(inv):
    if not inv:
        print("\nNo hay productos")
        return
    print("\nEl inventario es: ")
    for prod in inv:
        print(f"\nNombre: {prod['nombre']}\nPrecio: {prod['precio']}\nCantidad: {prod['cantidad']}")

def salir():
    print("Hasta pronto...")
    sys.exit()


def menu():
    print("""
          ------------------------------------
          Seleccione una opcion porfavor: 
          1. Agregar producto
          2. Buscar producto
          3. Actualizar precio
          4. Actualizar cantidad
          5. Eliminar producto
          6. Eliminar inventario
          7. Calcular valor del inventario
          8. Mostrar productos
          9. Salir
          ------------------------------------""")
    while True:
        try:
            opc = int(input("\nIngrese su opcion: "))
            if 0<opc<=9:
                return opc
            else: print("\nIngrese una de las opciones validas")
        except ValueError:
            print("\nIngrese una opcion valida")

    
print("-" * 40)
print("                 Bienvenido")
print("-" *40)

inv=[]

while True:
    opc = menu()
    match opc:

        #Caso de agregar producto
        case 1:
            #Agregar nombre del producto
            nom = str(input("\nIngrese el nombre de su producto: "))

            #Agregar precio del producto
            while True:
                try:
                    prec= float(input("Ingrese un precio: "))
                    if prec>0:
                        break
                    else:
                        print("Ingrese un precio valido")
                except ValueError: print("Ingrese un precio valido")

            #Agregar cantidad del producto
            while True:
                try:
                    cant= int (input("Ingrese la cantidad de su producto: "))
                    if cant>0:
                        break
                    else:
                        print("Ingrese una cantidad valida")
                except: 
                    ("Ingrese una cantidad valida")
            inv = agregar(inv, nom, prec, cant)
        #Caso de buscar producto
        case 2:
            nom = str(input("\nIngrese nombre del producto a buscar: "))
            prod = buscar(inv, nom)
            if prod:
                print(f"""\nProducto encontrado: 
                      Producto: {prod['nombre']} 
                      Precio: ${prod['precio']: ,.2f} 
                      Cantidad: {prod['cantidad']}\n""")
        #Caso actualizar precio
        case 3:
            nom =str(input("\nIngrese el nombre del producto a actualizar: "))
            
            #Ingreso precio nuevo
            while True:
                try:
                    precn = float(input("Ingrese el precio nuevo: "))
                    if precn>0:
                        break
                    else:
                        print("Ingrese un precio valido")
                except ValueError:
                    print("\nIngrese un precio valido\n")
            actprec(inv, nom, precn)

        #Caso actualizar cantidad
        case 4:
            nom = str (input("\nIngrese el nombe del producto a actualizar: "))

            #Ingreso cantidad nueva
            while True:
                try:
                    cantn = int(input("Ingrese una cantidad: "))
                    if cantn>0:
                        break
                    else:
                        print("Ingrese una cantidad valida")
                except ValueError:
                    print("\nIngrese una cantidad valida")
            actcant(inv, nom, cantn)
        
        #Caso eliminar producto
        case 5:
            nom = str(input("\nIngrese el producto a eliminar: "))
            elim(inv,nom)

        #Caso borrar inventario
        case 6:
            limp(inv)
        
        #Caso calcular valor total
        case 7: 
            total = tot(inv)
            print(f"\nEl valor total del inventario es {total:,.2f}\n")

        #caso motrar inventario
        case 8:
            most(inv)
        
        #Salir
        case 9:
            salir()