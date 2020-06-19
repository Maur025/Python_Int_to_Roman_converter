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
        self.res = 0
        self.ret = ""
        self.listnum = list(range(0,len(str(self.number))))#declaracion de la lista
        #podria ser innecesario pero lo dejare por un tiempo 

    def conver_Romanos(self):
        c = 0
        ann = 1
        while self.number > 0: #while para desarmar el numero
            self.res = self.number % 10 #obteniendo el residuo del numero 
            self.listnum[c] = self.res#lo añado a una lista, podria ser innecesario
            self.number = self.number // 10#divido el valor para no quedar en un loop infinito
            c = c + 1#contador para la lista, podria ser innecesario
            self.convertir_dic(self.res * ann)#envia un valor para comparacion a la funcion
            #para evitar errores en cada iteracion se le multiplica por diez ej.
            # si el valor es 521 primero enviara el 1 a comparar, luego se enviara 20 a comparar
            #y por ultimo el valor de 500
            self.ret =self.rom + self.ret #arma el resultado de derecha a izquierda           
            ann = ann * 10 #multiplicador  para obtener valores como 10 o 500 etc


        print(self.ret)
        print(self.listnum)




    def convertir_dic(self,xnum):   
        tal =0  
        if xnum == 0:
            self.rom = ""   
        if xnum >= 1 and xnum <= 3:
            self.rom = "I"*xnum
        else: 
            if xnum == 4:
                self.rom = "IV"
        if xnum >= 5 and xnum <= 8:
            tal=xnum - 5
            self.rom = "V" + "I"*tal
        else:
            if xnum == 9:
                self.rom = "IX"
        if xnum >= 10 and xnum<=30 :
            tal = xnum // 10
            self.rom = "X" * tal
        else:
            if xnum == 40:
                self.rom ="XL"
        if xnum >= 50 and xnum <= 80:
            tal = xnum - 50
            tal = tal // 10
            self.rom = "L" + "X" * tal
        else:
            if xnum ==90:
                self.rom = "XC"
        if xnum >= 100 and xnum <=300:
            tal = xnum //100
            self.rom = "C" * tal
        else:
            if xnum == 400:
                self.rom = "CD"
        if xnum >= 500 and xnum <= 800:
            tal = xnum - 500
            tal = tal // 100
            self.rom = "D" + "C" * tal
        else:
            if xnum == 900:
                self.rom = "CM"
        if xnum >= 1000 and xnum <= 3000:
            tal =xnum // 1000
            self.rom = "M" * tal
        
        return self.rom
        
