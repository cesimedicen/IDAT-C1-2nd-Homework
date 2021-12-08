##PROBLEMAS DE ESTRUCTURA REPETITIVA
# A)

n=10
pares = list()
while(len(pares)<25):
    pares.append(n) 
    n=n+2
for par in pares:
    print(par)
suma_pares = sum(pares)
print(suma_pares)

# B)

n = int(input("ingrese la cantidad de notas: "))
suma=0
i=1
while(i <= n):
    print("ingrese la nota número: ",i)
    nota = float(input())
    suma=suma+nota
    i+=1
prom = suma / n
print("el promedio es: ",prom)


# C)

from ast import Num
from os import stat_result
import random
alumnos = 1

while alumnos <= 150:
    parcial = random.randint(0,20)
    practica = random.randint(0,20)
    nota_final = (parcial + practica) / 2 
    print(f"Alumno N: {alumnos} obtuvo: {nota_final}")
    alumnos = alumnos + 1

# D) 

neutros=0
positivos=0
negativos=0

for i in range (5):
        print("ingrese un numero")
        numero=int(input())
        if numero == 0:
            neutros=neutros+1
        elif numero < 0:
            negativos=negativos+1
        elif numero > 0:
            positivos=positivos+1
print("los numeros neutros son ", neutros)
print("los numeros positivos son:", positivos)
print("los numeros negativos son:", negativos)

# E)

neutros=0
positivos=0
negativos=0
pares=0
impares=0

for i in range (10):
    print("ingrese un numero:")
    numero=int(input())
    if numero ==0:
        neutros=neutros+1
    elif numero <0:
        negativos=negativos+1
    elif numero >0:
        positivos=positivos+1
    elif numero%2==0:
        pares=pares+1
    elif numero%2!=0:
        impares=impares+1
print("los numeros neutros son:",neutros)
print("los numeros positivos son:",positivos)
print("los numeros negativos son:",negativos)
print("los numeros pares son:",pares)
print("los numeros impares son:",impares)

# F)

edad= 0
infancia=0
adolescencia=0
juventud=0
adultez=0
vejez=0

for i in range (10):
    print("ingrese su edad")
    edad=int(input())
    if edad>0 and edad < 12:
        infancia=infancia+1
    if edad>12 and edad < 18:
        adolescencia=adolescencia+1
    if edad>18 and edad <25:
        juventud=juventud+1
    if edad>25 and edad <65:
        adultez=adultez+1
    if edad>65 and edad <150:
        vejez=vejez+1

print("el numero de infantes es:",infancia)
print("el numero de adolescentes es:",adolescencia)
print("el numero de jovenes es:",juventud)
print("el numero de adultos es:",adultez)
print("el numero de ancianos es:",vejez)

# G)

sueldoM=2500
sueldoV=3000
marketing=0
ventas=0

for i in range(10):
    print("ingresa tu profesión")
    profesion=input()
    if profesion =="marketing":
        marketing=marketing+1
    elif profesion=="ventas":
        ventas=ventas+1
print(f"el numero de trabajadores en el area de marketing es {marketing} y su sueldo es:S/ {sueldoM} ")
print(f"el numero de trabajadores en el area de ventas y compras es {ventas} y su sueldo es:S/ {sueldoV} ")

# H)

pares=0
numero = int(input("Ingrese en numero:"))
tmbnumero=numero
dig=0
suma=0
while(tmbnumero!=0):
    dig=int(tmbnumero % 10)
    suma+=dig
    tmbnumero=int(tmbnumero/10)
    if tmbnumero%2==0:
        pares=pares+1
print("la suma de los digitos de ",numero," es ",suma)
print("fueron pares:",pares)

# I)

    for i in range(0,3):
        pares=0
        numero = int(input("Ingrese en numero [%i]:"% i))
        tmbnumero=numero
        dig=0
        suma=0
        while(tmbnumero!=0):
            dig=int(tmbnumero % 10)
            suma+=dig
            tmbnumero=int(tmbnumero/10)
            if tmbnumero%2==0:
                pares=pares+1
    print("la suma de los digitos de ",numero," es ",suma)
    print("fueron pares:",pares)

# J)

print(sum(range(1, 51,2))-sum(range(2,51,2)))


# L)

c=0
Num=0
Ac=7
while(c<5000):
    c=c+1
    Num=Num+10
    Ac=Ac+Num
    print(Num,end=",")
    NF=Ac+7
print("la suma es:",Ac)

# M) 

edad=0
E_senso=0
E_pre=0
E_con=0
E_For=0
for i in range (5):
    print("ingrese su edad")
    edad=int(input())
    if edad>0 and edad <2:
        E_senso=E_senso+1
    if edad>2 and edad <7:
        E_pre=E_pre+1
    if edad>7 and edad <11:
        E_con=E_con+1
    if edad>11 and edad <15:
        E_For=E_For+1
print("personas en etapa sensomotora:",E_senso)
print("personas en etapa preoperacional:", E_pre)
print("personas en etapa Op. concretas:", E_con)
print("personas en etapa Op. formales:", E_For)
    
# N)

print(sum(range(1, 51,2))-sum(range(2,51,2)))

# P)

sueldoM=2500
sueldoV=3000
marketing=0
ventas=0

for i in range(10):
    print("ingresa tu profesión")
    profesion=input()
    if profesion =="marketing":
        marketing=marketing+1
    elif profesion=="ventas":
        ventas=ventas+1
print(f"el numero de trabajadores en el area de marketing es {marketing} y su sueldo es:S/ {sueldoM} ")
print(f"el numero de trabajadores en el area de ventas y compras es {ventas} y su sueldo es:S/ {sueldoV} ")

# Q)

# R)



# S)

numeros50_100 = []
numeros100 = []
print("ingrese un numero positivo. \n(Ingrese cero para finalizar el programa")

while True:
    numero = int(input("numero: "))
    if numero == 0:
        break
    if numero > 50 and numero < 100:
        numeros50_100.append(numero)
    if numero > 100:
        numeros100.append(numero)

print("numeros entre 50 y 100:")
for i in numeros50_100:
    print(i , end= ' ')

print("\n numero mayores a 100:")
for i in numeros100:
    print(i , end=' ')

# T)

# U)

n=20
pares = list()
while(len(pares)<380):
    pares.append(n) 
    n=n+2
for par in pares:
    print(par)
suma_pares = sum(pares)
print(suma_pares)
print("la suma de los extremos es:")
print(20+778)

# V) 

import random

mayor=0
menor=0
maximo=500
for i in range(maximo):
    if i>mayor:
        mayor=i
    print(random.randrange(5,500,4))
print("el numero mayor es:")
print(mayor)
print("el numero menor es:")
print(menor)


    