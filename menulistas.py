def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza

def mostrar(cabeza):
    if cabeza is None:
        print("La lista está vacía.")
        return
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]
    print("None")

def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0
    while actual is not None:
        if actual["dato"] == dato:
            return posicion
        actual = actual["siguiente"]
        posicion += 1
    return -1

def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False
    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True
    anterior = cabeza
    actual = cabeza["siguiente"]
    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True
        anterior = actual
        actual = actual["siguiente"]
    return cabeza, False

def contar(cabeza):
    total = 0
    actual = cabeza
    while actual is not None:
        total += 1
        actual = actual["siguiente"]
    return total

def menu():
    cabeza = None
    
    while True:
        print("\n--- MENÚ LISTA ENLAZADA ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Eliminar elemento")
        print("6. Contar elementos")
        print("7. Salir")
        
        opcion = input("Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            dato = input("Ingresa el elemento a insertar al inicio: ")
            cabeza = insertar_inicio(cabeza, dato)
            print(f"'{dato}' insertado al inicio.")
            
        elif opcion == "2":
            dato = input("Ingresa el elemento a insertar al final: ")
            cabeza = insertar_final(cabeza, dato)
            print(f"'{dato}' insertado al final.")
            
        elif opcion == "3":
            print("\nLista actual:")
            mostrar(cabeza)
            
        elif opcion == "4":
            dato = input("Ingresa el elemento a buscar: ")
            pos = buscar(cabeza, dato)
            if pos != -1:
                print(f"'{dato}' se encuentra en la posición (índice): {pos}")
            else:
                print(f"'{dato}' no se encontró en la lista.")
                
        elif opcion == "5":
            dato = input("Ingresa el elemento a eliminar: ")
            cabeza, eliminado = eliminar(cabeza, dato)
            if eliminado:
                print(f"'{dato}' ha sido eliminado exitosamente.")
            else:
                print(f"No se encontró '{dato}' para eliminar.")
                
        elif opcion == "6":
            print(f"Total de elementos en la lista: {contar(cabeza)}")
            
        elif opcion == "7":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Intenta de nuevo.")
            
menu()