import Ent_rom
import Rom_ent

valor = input("ingresa un numero: ")

try:
    valor = int(valor)
    a = Ent_rom.Enteros(valor)
    a.conver_Romanos()

except:
    #print("es un string")
    a = Rom_ent.Letras(valor)
    a.convertir()