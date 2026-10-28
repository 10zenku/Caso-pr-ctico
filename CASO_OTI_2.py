#Caso rediseño
class MatriculaGeneral:
    def calcular(self):
        return 60.00


class MatriculaExtemporanea(MatriculaGeneral):
    def calcular(self):
        return super().calcular() + 15.00


class IndiceDesaprobatorio(MatriculaGeneral):
    def calcular(self):
        return super().calcular() + 15.00


class BecaViolencia(MatriculaGeneral):
    def calcular(self):
        return super().calcular() / 2


# Versión 1
class Matricula1(
    BecaViolencia,
    IndiceDesaprobatorio,
    MatriculaExtemporanea
):
    pass


# Versión 2
class Matricula2(
    IndiceDesaprobatorio,
    MatriculaExtemporanea,
    BecaViolencia
):
    pass

#Crear los objetos
a = Matricula1()
b = Matricula2()

print("Versión 1:", a.calcular())
print("Versión 2:", b.calcular())







#OTRA MANERA
# Clase padre
class MatriculaBase:
    def __init__(self):
        self.monto = 60.00
# Classe hija
class MatriculaAlumno(MatriculaBase):
    def __init__(self):
        MatriculaBase.__init__(self) 
        self.tiene_extemporanea = False
        self.tiene_desaprobado = False
        self.tiene_beca = False
        self.tipo_calculo = "beca_al_final" 

    # Método para calcular
    def calcular(self):
        # beca al inicio
        if self.tiene_beca == True:
            if self.tipo_calculo == "beca_al_inicio":
                self.monto = self.monto / 2
        
        # con recargos
        if self.tiene_extemporanea == True:
            self.monto = self.monto + 15.00
            
        if self.tiene_desaprobado == True:
            self.monto = self.monto + 15.00
            
        # beca al final
        if self.tiene_beca == True:
            if self.tipo_calculo == "beca_al_final":
                self.monto = self.monto / 2
                
        return self.monto

# pruebin
# Caso de Luis
luis = MatriculaAlumno()
luis.tiene_extemporanea = True
luis.tiene_desaprobado = True
luis.tiene_beca = True
luis.tipo_calculo = "beca_al_final"

print("Total de Luis: S/", luis.calcular())

# Caso de Rosa
rosa = MatriculaAlumno()
rosa.tiene_extemporanea = True
rosa.tiene_desaprobado = True
rosa.tiene_beca = True
rosa.tipo_calculo = "beca_al_inicio" 

print("Total de Rosa: S/", rosa.calcular())
