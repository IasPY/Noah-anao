elemento_quimico = input('Digite a sigla de um elemento químico ou o número atômico de um elemento químico : ')
elemento_quimico = elemento_quimico.lower()

lista_h = ['h','1']
lista_he = ['he','2']
lista_li = ['li','3']
lista_be = ['be','4']
lista_b = ['b','5']
lista_c = ['c','6']  
lista_n = ['n','7']
lista_o = ['o','8']
lista_f = ['f','9']
lista_ne = ['ne','10']
#-----------------------------------------------------------------------------------
atributo_h = '1,008u '
atributo_he = '4,0026u'
atributo_li = '6,94u'
atributo_be = '9,0122u'
atributo_b = '10,81u'
atributo_c = '12,011u'
atributo_n = '14,007u'
atributo_o = '15,998u'
atributo_f = '18,998u'
atributo_ne = '20,180u'

if elemento_quimico in lista_h:
  print(f'Hidrogênio\nMassa Atômica: {atributo_h}\nNúmero Atômico: 1')
if elemento_quimico in lista_he:
  print(f'Hélio\nMassa Atômica: {atributo_he}\nNúmero Atômico: 2')
if elemento_quimico in lista_li:
  print(f'Lítio\nMassa Atômica: {atributo_li}\nNúmero Atômica: 3')
if elemento_quimico in lista_be:
    print(f'Berílio\nMassa Atômica: {atributo_be}\nNúmero Atômica: 4')
if elemento_quimico in lista_b:
  print(f'Boro\nMassa Atômica: {atributo_b}\nNúmero Atômico: 5') 
if elemento_quimico in lista_c:
  print(f'Carbono\nMassa Atômica: {atributo_c}\nNúmero Atômico: 6')
if elemento_quimico in lista_n:
  print(f'Nitrogênio\nMassa Atômica: {atributo_n}\nNúmero Atômica: 7')
if elemento_quimico in lista_o:
  print(f'Oxigênio\nMassa Atômica: {atributo_o}\nNúmero Atômica: 8')
if elemento_quimico in lista_f:
  print(f'Flúor\nMassa Atômica: {atributo_f}\nNúmero Atômica: 9')
if elemento_quimico in lista_ne:
  print(f'Neônio\nMassa Atômica: {atributo_ne}\nNúmero Atômica: 10')
#feito por isaias 2B