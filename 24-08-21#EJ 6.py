import collections
SEPARADOR = ("*"*20) + "\n"

pila_con_lista = list()
for i in range(5):
    pila_con_lista.append(input('dime el nombre a agregar: '))
    
while pila_con_lista:
    print(pila_con_lista.pop())
print(SEPARADOR)