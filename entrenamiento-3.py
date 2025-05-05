import sys
#definimos una funcion para agregar productos
def agregar(inv, nom, prec, cant):
    inv.append({"nombre": nom, "precio": prec, "cantidad" : cant})
    print(f"\nEl producto '{nom}' ha sido agregado")
    return inv

#Definimos una funcion para consultar o buscar un producto
def buscar(inv, nom):
    for prod in inv:
        if prod["nombre"].lower() == nom.lower():
            return prod["nombre"], prod["precio"], prod["cantidad"]
    print(f"\nProducto {nom} no encontrado")
    return None

#Creamos una funcion para actualizar el precio
def actprec(inv,nom,precn):
    for prod in inv:
        if prod["nombre"].lower() == nom.lower():
            prod["precio"] == precn
            print(f"\nPrecio de '{nom} actualizado a '{precn}'")
            return
        print(f"\nProducto '{nom}' no encontrado")
        

#Creamos una funcion para eliminar producctos
def elim(inv,nom):
    for i, prod in inv:
        if prod["nombre"].lower == nom.lower():
            del inv[i]
            print(f"\nproducto {nom} eliminado exitosamente")
            return
        print(f"\nproducto {nom} no encontrado")


#Creamos una funcion para calcular el valor total con un lambda
def tot(inv):
    total= sum(map(lambda x: x["precio" * x["cantidad"], inv]))
    return total

#Creare una funcion para leer el inventario completo
def most(inv):
    if not inv:
        print("\nNo hay productos")
        return
    print("\nEl inventario es: ")
    for prod in inv:
        print(f"Nombre: {prod['nombre']}\nPrecio: {prod['precio']}\nCantidad: {prod['cantidad']}")



print("-" * 40)
print("                 Bienvenido")
print("-" *40)