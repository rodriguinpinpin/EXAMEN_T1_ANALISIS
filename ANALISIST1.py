class Puesto:
    def __init__(self, cod, desc, area, plaz, suel):
        self.codigo = cod
        self.descripcion = desc
        self.areaSolicitante = area
        self.plazasRequeridas = plaz
        self.sueldo = suel

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} ({self.areaSolicitante}) | Plazas: {self.plazasRequeridas} | S/ {self.sueldo}"

def buscaPuesto(lst, cod, desc, area):
    for p in lst:
        if p.codigo == cod:
            return True
    return False

def buscarPuestoPorCodigo(lst, cod):
    for p in lst:
        if p.codigo == cod:
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

puesto1 = Puesto("P001", "Analista de Datos", "SISTEMAS", 3, 5000)
puesto2 = Puesto("P002", "Desarrollador Web", "ANALISIS", 5, 4500)
puesto3 = Puesto("P003", "Gerente de Proyectos", "GESTION", 2, 7000)
puesto4 = Puesto("P004", "Especialista en Marketing", "MARKETING", 4, 4000)
puesto5 = Puesto("P005", "Analista de Seguridad", "SEGURIDAD", 1, 6000)
puesto6 = Puesto("P006", "Diseñador Gráfico", "DISEÑO", 3, 3500)

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
        cod = input("Ingrese el codigo del puesto: ")
        desc = input("Ingrese la descripcion del puesto: ")
        area = input("Ingrese el área solicitante: ")
        if buscaPuesto(lista, cod, desc, area):
            print("Puesto encontrado.")
        else:
            print("Puesto no encontrado.")
    elif opcion == "2":
        print("\nPuestos disponibles:")
        for p in lista:
            print(p)    
    elif opcion == "3":
        cod = input("Ingrese el codigo del puesto a borrar: ")
        for p in lista:
            if p.codigo == cod:
                lista.remove(p)
                print("Puesto borrado.")
                break   
    elif opcion == "4":
        cod = input("Ingrese el codigo del puesto para buscar su sueldo: ")
        for p in lista:
            if p.codigo == cod:
                print(f"Sueldo del puesto {p.descripcion}: S/ {p.sueldo}")
                break
    elif opcion == "5":
        area = input("Ingrese el area para mostrar sus puestos: ")
        print(f"\nPuestos en el area {area}:")
        for p in lista:
            if p.areaSolicitante == area:
                print(p)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("OPCION INVALIDA, INTENTE DE NUEVO.")
        
        
        





