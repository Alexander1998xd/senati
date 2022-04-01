# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:34:01 2022

@author: jhordan
"""

from Trabajador import Trabajador 






print("="*80)

print("                                   fERROTEXC                    ")

print("="*80)

nom=""
while not (nom in range (1,6)):
    nom = int(input("SELECCIONE EL TRABAJADOR QUE DESEA PAGAR:\n [1]JHORDAN \n [2]MELANIE \n [3]ALEXANDER \n [4]RUBI \n [5]LINDA \n\nElija su opción: "))
    if not (nom in range(1,6)):
        print("Trabajador incorrecto....")

print("="*80)

pro = ""
while not (pro in range (1, 6)):
    pro = int(input("SELLECIONE SU PUESTO DE TRABAJO:\n [1]GERENTE \n [2]ARQUITECTO \n [3]ING.CIVIL \n [4]RECURSOS HUMANOS \n [5]SUPERVISOR DE OBRA \n\nEliga la profesión: "))
   
    if not (pro in range (1, 6)):
        print("Profesión no valida")
        
    

print("="*80)

cat = ""


while not (cat == "A" or cat== "B" or cat == "C" or cat =="D" or cat == "E"):
    cat = str(input("CATEGORÍA [A / B / C/ D/ E]..: "))
    if not (cat =="A" or cat== "B" or cat == "C" or cat =="D" or cat == "E"):
            print("Categoria incorrecta....")    
            
            

          
           
            

he= float(input("HORAS EXTRAS...................: "))

tar=float(input("TARDANZAS(minutos).............: "))

alu= Trabajador(nom , cat, he,tar,pro)





print("")
print("="*70)
print("                       B O L E T A   D E    P A G O          ")

print("="*70)
print("\nNombre completo..............:",alu.Nombre())

print("DNI..........................: ",alu.DNI())

print("Profesión....................: ", alu.Profesion())
print("Sueldo basico................: ",alu.Sueldo_basico(),"Soles")
print("\nDescuento de tardanza......: ",alu.Descuento())
print("\nPago por horas extras......: ",alu.Horas_extras())
print("\nSueldo Neto................: ",alu.Sueldo_neto(),"Soles")

print("="*70)





print("\nDesea seguir pagando a sus trabajadres [SI / NO] : " )




