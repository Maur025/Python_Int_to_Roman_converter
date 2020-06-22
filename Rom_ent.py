class Letras:
    def __init__(self,palabra):
        self.word = palabra

    def convertir(self):
        #14 = XIV --> 10 1 5  si el numero de la izquierda es menor se resta
        #3 = III --> 1 1 1 
        resul1 = 0
        resto = 0
        rec = self.word
        val_ant = 0

        #print(rec.find('V'))

        if rec.startswith('V') and (rec.find('X') > 0 or rec.find('L') > 0 or rec.find('C') > 0 or rec.find('D') > 0 or rec.find('M') > 0):
            print('El numero que ingresaste tiene un error, vuelve a intentarlo')
        else:
            if rec.startswith('L') and (rec.find('C') > 0 or rec.find('D') > 0 or rec.find('M') > 0):
                print('El numero que ingresaste tiene un error, vuelve a intentarlo')
            else:
                if rec.startswith('D') and rec.find('M') > 0:
                    print('El numero que ingresaste tiene un error, vuelve a intentarlo')
                else:
                    if rec.startswith('I') and rec.count('I') >= 1 and ( rec.find('V')> 1 or rec.find('X') > 1 or rec.find('C') > 0 or rec.find('L')> 0 or rec.find('D') > 0 or rec.find('M') > 0 ):
                        print("El numero que ingresaste tiene un error, vuelve a intentarlo")
                    else:
                        if rec.startswith('X') and rec.count('X') >= 1 and (rec.find('C') > 1 or rec.find('L')> 1 or rec.find('D') > 0 or rec.find('M') > 0 ):
                            print("El numero que ingresaste tiene un error, vuelve a intentarlo")
                        else:
                            if rec.count('V') > 1 or rec.count('D') > 1 or rec.count('L') > 1 or rec.count('I') > 3 or rec.count('C')> 3 or rec.count('X') > 3 or rec.count("M") > 3:
                                print("El numero que ingresaste tiene un error, vuelve a intentarlo")
                            else:
                                for i in reversed(range(0,len(rec))):
                                    resul1= self.convertir_dicc(rec[i])
                                    #print(val_ant)
                                    if resul1 >= val_ant:
                                        resto = resul1 + resto
                                        #print('resto')
                                    else:
                                        resto = resto - resul1
                                        #print('sumo')

                                    val_ant = resul1
                                    print(resto)
                                print(resto)

                                # xcix = 99
                                # x = 10 - 0
                                # c = 100 - 10


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
