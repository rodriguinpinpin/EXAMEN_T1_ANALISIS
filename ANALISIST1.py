"""
Cree un proyecto Python para almacenar y administrar una lista de Puestos de trabajo disponibles en una empresa. Cada Puesto de trabajo se representará con una clase que tendrá los siguientes atributos: codigo (int), descripcion (string), areaSolicitante (string), plazasRequeridas (int), y sueldo (float). Cree una lista de Puestos de trabajo, y haga un aplicativo que tenga el siguiente menú repetitivo:
•	1 – AgregaPuesto(): Registrar un nuevo Puesto de trabajo, para lo cual buscará linealmente tal que debe validar que no haya otro Puesto de trabajo con el mismo código, descripcion o areaSolicitante e insertará el nuevo Puesto de trabajo. Valide que los datos string tengan por lo menos 3 letras y los datos numéricos sean mayor a cero.
•	2 – MostrarTodo(): mostrará todos los Puesto de trabajo creados sin ordenar
•	3 – BorraPuesto(): Pedirá un codigo, luego ordenará por método de burbuja usando el código de más a menos y mediante búsqueda lineal buscará el Puesto de trabajo cuyos codigos coincidan y los eliminará de la lista.
•	4 – BuscaSueldo(): Ordenará la lista por sueldo usando método de inserción de más a menos. Luego preguntará un sueldo a buscar, y usando la búsqueda binaria encontrará todos los Puesto de trabajo con ese sueldo. Recuerde que como esta ordenado si hubieran varios Puesto de trabajo con el mismo sueldo van a estar justo antes o después. Use la menor cantidad de operaciones a la lista para mostrar lo solicitado
•	5 – PuestosAContratar(): Preguntará cuánto dinero en total se invertirá en salarios de puestos nuevos y mostrará la lista de puestos que podrían contratarse hasta cubrir el monto. Nótese que cada puesto tiene asociada una cantidad plazasRequeridas y, multiplicado por el sueldo de cada plaza, se obtiene el total requerido en dinero para ese puesto de trabajo. Ordene la lista de Puesto de trabajo con el método de selección según de más a menos según el total requerido en dinero y muestre los puestos que se cubrirán hasta cubrir el monto que se invertirá en salarios.
•	6 – Salir: Termina el programa

Tras terminar el código agregue 6 Puesto de trabajo con los datos que considere y ejecute cada función creada. Asegúrese de que su proyecto este en un repositorio público de su cuenta de github.


DEBE USAR NECESARIAMENTE LAS INSTRUCCIONES APRENDIDAS EN CLASE, SI USA OTRAS MAS AVANZADAS SE INTERPRETARÁ COMO QUE USO IA Y SE DESCARTARA SU RESPUESTA.
"""
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
        if p.codigo == cod or p.descripcion == desc or p.areaSolicitante == area:
            return True
    return False

def ordBurbuja(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j].codigo < lst[j + 1].codigo:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

def ordInsercion(lst):
    for i in range(1, len(lst)):
        aux = lst[i]
        j = i - 1
        while j >= 0 and aux.sueldo > lst[j].sueldo:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = aux

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

# Carga inicial de 6 puestos (como pide la guía)
lista.append(Puesto(10, "Analista", "Sistemas", 2, 2500.0))
lista.append(Puesto(50, "Contador", "Finanzas", 1, 4200.0))
lista.append(Puesto(20, "Developer", "Sistemas", 3, 3800.0))
lista.append(Puesto(80, "Gerente", "RRHH", 1, 9000.0))
lista.append(Puesto(30, "Asistente", "Ventas", 4, 1800.0))
lista.append(Puesto(40, "Secretaria", "Gerencia", 1, 2200.0))

while True:
    print("\n--- MENU DE PUESTOS ---")
    print("1-AgregaPuesto, 2-MostrarTodo, 3-BorraPuesto, 4-BuscaSueldo, 5-PuestosAContratar, 6-Salir")
    opc = int(input("Elija opcion: "))

    if opc == 1:
        cod = int(input("Ingrese codigo: "))
        desc = input("Ingrese descripcion: ")
        area = input("Ingrese area: ")
        plaz = int(input("Ingrese plazas: "))
        suel = float(input("Ingrese sueldo: "))

        if len(desc) >= 3 and len(area) >= 3 and cod > 0 and plaz > 0 and suel > 0:
            if not buscaPuesto(lista, cod, desc, area):
                nuevo = Puesto(cod, desc, area, plaz, suel)
                lista.append(nuevo)
                print("Registrado correctamente.")
            else:
                print("Error: Codigo, Descripcion o Area ya existen.")
        else:
            print("Datos invalidos (minimo 3 letras o numeros mayor a 0).")

    elif opc == 2:
        print("\n--- TODOS LOS PUESTOS ---")
        for p in lista:
            print(p)

    elif opc == 3:
        cod_borrar = int(input("Codigo a borrar: "))
        ordBurbuja(lista) # Ordena de mas a menos por codigo
        i = 0
        eliminado = False
        while i < len(lista):
            if lista[i].codigo == cod_borrar:
                lista.pop(i)
                eliminado = True
            else:
                i += 1
        if eliminado: print("Puesto borrado.")
        else: print("No se encontro.")

    elif opc == 4:
        ordInsercion(lista) # Ordena por sueldo de mas a menos
        buscado = float(input("Sueldo a buscar: "))
        bajo = 0
        alto = len(lista) - 1
        encontrado_en = -1
        
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if lista[medio].sueldo == buscado:
                encontrado_en = medio
                break
            elif lista[medio].sueldo < buscado:
                alto = medio - 1
            else:
                bajo = medio + 1
        
        if encontrado_en != -1:
            # Buscar duplicados adyacentes
            izq = encontrado_en
            while izq > 0 and lista[izq-1].sueldo == buscado:
                izq -= 1
            der = encontrado_en
            while der < len(lista)-1 and lista[der+1].sueldo == buscado:
                der += 1
            for k in range(izq, der + 1):
                print(lista[k])
        else:
            print("No se encontro el sueldo.")

    elif opc == 5:
        monto = float(input("Dinero total a invertir: "))
        ordSeleccion(lista) # Ordena por (plazas * sueldo)
        
        print("\nPuestos que se pueden contratar:")
        suma = 0
        for p in lista:
            costo = p.plazasRequeridas * p.sueldo
            if suma + costo <= monto:
                suma += costo
                print(f"{p} | Costo Puesto: {costo}")
        print(f"Total invertido: {suma}")

    elif opc == 6:
        print("Saliendo...")
        break

    