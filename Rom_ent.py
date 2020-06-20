class Letras:
    def __init__(self,palabra):
        self.word = palabra

    def convertir(self):
        #14 = XIV --> 10 1 5  si el numero de la izquierda es menor se resta
        #3 = III --> 1 1 1 
        resul = 0
        rec = self.word
        resul= self.convertir_dicc(rec)
        print(resul)


    def convertir_dicc(self,pal1):
        res = 0
        if pal1 == "I":
            res = 1
        if pal1 == "V":
            res = 5
        if pal1 == "X":
            res = 10
        if pal1 == "L":
            res = 50
        if pal1 == "C":
            res = 100
        if pal1 == "D":
            res = 500
        if pal1 == "M":
            res = 1000

        return res
