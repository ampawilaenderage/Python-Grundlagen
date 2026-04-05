import random


uhrzeit = 23
# bedingte Anweisung
if uhrzeit >= 10:
 print('das ist aber früh')
# einfache Verzweigung
if uhrzeit < 12:
 print('Guten Morgen')
else:
 print('Guten Tag')
# mehrfache Verzweigung
if uhrzeit < 12:
 print('Guten Morgen')
elif uhrzeit < 17:
 print('Guten Tag')
elif uhrzeit < 22:
 print('Guten Abend')
else:
 print('Gute Nacht')

ampel = 'gsrün'
match ampel:
  case 'rot':
    print('STOP')
  case 'gelb':
    print('Achtung')
  case 'grün':
    print('Fahren')
  case _:
    print('Ampel defekt') 


i = 10
while i > 0:
 i -=  1
 if(i==5):
  break
 print(i)


fun1 = lambda x: x*10
fun2 = lambda y:y+5*y

print(fun1(5) + fun2(3))