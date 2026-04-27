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

