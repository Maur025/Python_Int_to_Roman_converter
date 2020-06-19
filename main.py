import Ent_rom
import Rom_ent

valor = input("ingresa un numero: ")

try:
    valor = int(valor)
    print("es un numero")
    Ent_rom.Enteros(valor)
except:
    print("es un string")
    Rom_ent.Letras(valor)