#I = 1
#V = 5
#X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# 1. Si a la derecha de una cifra romana se escribe otra igual o menor,
#  el valor de esta se suma a la anterior
# XXI = 21
# 2. La cifra I colocada antes de la V o X les resta una unidad
# La X precediendo a la L o a la C les resta 10 unidades
# La C precediendo a la D o la M les resta 100 unidades
#XL = 40
#3. En ningun numero se puede poner una misma letra mas de 3 veces seguidas
#XIV = 14
#4. La V la L y la D no pueden duplicarse porque hay otras letras X , C, M que 
# representan su valor duplicado
# 10 = X no 10 = VV
class Enteros:
    def __init__(self,numero):
        self.number=numero
        self.rom = ""

    def convertir_Rom(self):        
        if self.number == 1:
            self.rom = "I"
        if self.number == 5:
            self.rom = "V"
        if self.number == 10:
            self.rom = "X"
        if self.number == 50:
            self.rom = "L"
        if self.number == 100:
            self.rom = "C"
        if self.number == 500:
            self.rom = "D"
        if self.number == 1000:
            self.rom = "M"
        
        return self.rom
        
