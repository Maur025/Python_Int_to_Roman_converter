import Ent_rom
import Rom_ent

valor = input("ingresa un numero: ")

try:
    valor = int(valor)
    a = Ent_rom.Enteros(valor)
    print(a.convertir_Rom())

except:
    print("es un string")
    Rom_ent.Letras(valor)