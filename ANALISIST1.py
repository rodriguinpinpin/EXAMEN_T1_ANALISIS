class Puesto:
    def __init__(self, cod, desc, area, plaz, suel):
        self.codigo = int(cod)  # Ensure codigo is always an int
        self.descripcion = desc
        self.areaSolicitante = int(area)  # Ensure areaSolicitante is always an int
        self.plazasRequeridas = plaz
        self.sueldo = suel

    def __str__(self):
        # Map int back to string for display (optional, for readability)
        area_names = {1: "SISTEMAS", 2: "ANALISIS", 3: "GESTION", 4: "MARKETING", 5: "SEGURIDAD", 6: "DISEÑO"}
        area_str = area_names.get(self.areaSolicitante, "DESCONOCIDO")
        return f"{self.codigo} - {self.descripcion} ({area_str}) | Plazas: {self.plazasRequeridas} | S/ {self.sueldo}"

def buscaPuesto(lst, cod, desc, area):
    for p in lst:
        if p.codigo == int(cod) or p.areaSolicitante == int(area):  # Convert area to int for comparison
            return True
    return False

def buscarPuestoPorCodigo(lst, cod):
    for p in lst:
        if p.codigo == int(cod):  
            return p
    return False

def buscarSueldo(lst):
    for i in range(1, len(lst)):
        aux = lst[i]
        j = i - 1

        while j >= 0 and lst[j].sueldo < aux.sueldo:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = aux

def ordSeleccion(lst):
    n = len(lst)
    for mano in range(n - 1):
        posMayor = mano
        for ver in range(mano + 1, n):
            total_ver = lst[ver].plazasRequeridas * lst[ver].sueldo
            total_mayor = lst[posMayor].plazasRequeridas * lst[posMayor].sueldo
            if total_ver > total_mayor:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]

lista = []

# Updated to use int for areaSolicitante (example codes: 1=SISTEMAS, 2=ANALISIS, etc.)
puesto1 = Puesto(1, "Analista de Datos", 1, 3, 5000)
puesto2 = Puesto(2, "Desarrollador Web", 2, 5, 4500)
puesto3 = Puesto(3, "Gerente de Proyectos", 3, 2, 7000)
puesto4 = Puesto(4, "Especialista en Marketing", 4, 4, 4000)
puesto5 = Puesto(5, "Analista de Seguridad", 5, 1, 6000)
puesto6 = Puesto(6, "Diseñador Gráfico", 6, 3, 3500)

lista.append(puesto1)
lista.append(puesto2)
lista.append(puesto3)
lista.append(puesto4)
lista.append(puesto5)
lista.append(puesto6)

while True:
    print("\nMenú de opciones:")
    print("1. Agregar puesto")
    print("2. Mostrar puestos")
    print("3. Borrar puesto")
    print("4. Buscar Sueldo")
    print("5. Puestos por Area")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cod = int(input("Ingrese el código del puesto (número entero): "))  
        desc = input("Ingrese la descripción del puesto: ")
        area = int(input("Ingrese el código del área solicitante (número entero, e.g., 1=SISTEMAS): "))  # Convert to int
        if buscaPuesto(lista, cod, desc, area):
            print("Puesto encontrado.")
        else:
            print("Puesto no encontrado.")
    elif opcion == "2":
        print("\nPuestos disponibles:")
        for p in lista:
            print(p)    
    elif opcion == "3":
        cod = int(input("Ingrese el código del puesto a borrar (número entero): "))  
        for p in lista:
            if p.codigo == cod:
                lista.remove(p)
                print("Puesto borrado.")
                break   
    elif opcion == "4":
        cod = int(input("Ingrese el código del puesto para buscar su sueldo (número entero): "))  
        for p in lista:
            if p.codigo == cod:
                print(f"Sueldo del puesto {p.descripcion}: S/ {p.sueldo}")
                break
    elif opcion == "5":
        area = int(input("Ingrese el código del área para mostrar sus puestos (número entero): "))  # Convert to int
        print(f"\nPuestos en el área {area}:")
        for p in lista:
            if p.areaSolicitante == area:
                print(p)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("OPCION INVALIDA, INTENTE DE NUEVO.")








