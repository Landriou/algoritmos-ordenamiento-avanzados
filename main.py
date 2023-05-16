from linkedlist import *
from algo1 import *
from random import randint

def Quicksort(L):
    large = length(L)
    QuicksortWrapper(L,0,large - 1)

def QuicksortWrapper(L,inicio,fin):
    if inicio > fin:
        return
    pivote = getpivote(L,inicio,fin) #Busco el pivote entre 3 opciones
    initnode = accesposition(L,inicio)
    pivotevalue = pivote.value #Me guardo el value del pivote para el proximo switch
    switchvalues(initnode,pivote) #cambio el valor del pivote
    delimitador = initnode #Inicio un puntero que va avanzando para ordenar la lista con los menores a la izquierda
    currentnode = initnode
    inicioposicion = inicio
    for n in range(inicio, fin + 1):
        if currentnode.value < pivotevalue:
            delimitador = delimitador.nextNode #avanzo el delimitador para cambiarlo
            switchvalues(delimitador,currentnode)
            inicioposicion = inicioposicion +1
        currentnode = currentnode.nextNode
    switchvalues(initnode,delimitador)
        
    QuicksortWrapper(L,inicio, inicioposicion-1)
    QuicksortWrapper(L,inicioposicion+1,fin)
def switchvalues(nodeA,nodeB):
    value1 = nodeA.value
    value2 = nodeB.value
    nodeA.value = value2
    nodeB.value = value1
    #Obtiene el pivote de la lista comparando el inicio, el fin y la mitad
def getpivote(L,inicio, fin):
    mid = (inicio + fin)//2
    pivotenodefin = accesposition(L,fin)
    pivotenodemid = accesposition(L,mid)
    pivotenodeinicio = accesposition(L,inicio)
    pivotenode = pivotenodefin
    if pivotenodeinicio.value < pivotenodefin.value:
        if pivotenodeinicio.value > pivotenodemid.value:
            pivotenode = pivotenodeinicio
    if pivotenodeinicio.value < pivotenodemid.value:
        if pivotenodeinicio.value > pivotenodefin.value:
            pivotenode = pivotenodeinicio
    if pivotenodemid.value > pivotenodefin.value:
        if pivotenodemid.value < pivotenodeinicio.value:
            pivotenode = pivotenodemid
    if pivotenodemid.value < pivotenodeinicio.value:
        if pivotenodemid.value > pivotenodefin.value:
            pivotenode = pivotenodemid
    if pivotenodefin.value < pivotenodeinicio.value:
        if pivotenodefin.value > pivotenodemid.value:
            pivotenode = pivotenodefin
    if pivotenodefin.value > pivotenodeinicio.value:
        if pivotenodefin.value < pivotenodemid.value:
            pivotenode = pivotenodefin
    return pivotenode


def MergeSort(L):
    large = length(L)
    if large == 1:
        return L #Si la lista es de lenght 1, retorno la lista para el merge
    mid = int(large/2)
    Le = LinkedList() #Creo la lista izquierda
    currentnode = L.head
    for n in range(0,mid): #Paso los elementos hasta la mitad
        add(Le,currentnode.value)
        currentnode = currentnode.nextNode
    R = LinkedList() #Creo la lista derecha
    for u in range(mid+1,large +1 ): #Lo mismo
        add(R,currentnode.value)
        currentnode = currentnode.nextNode
    Left = MergeSort(Le) #Llamo a la recursividad del lado izquierdo y lo guardo
    Right = MergeSort(R) #LLamo a la recursividad del lado derecho y lo guardo
    return gitmerge(Left,Right) #Merge a los resultados
#Funcion que mergea 2 listas en 1  y los ordena
def gitmerge(L,R):
    Lfinal = LinkedList()
    largeL = length(L)
    largeR = length(R)
    i = j = 0
    nodeleft = L.head
    noderight = R.head
    for k in range (0, largeL+largeR): #Comparo los values de las listas y los voy agregando ordenados
        if nodeleft == None:
            add(Lfinal,noderight.value)
            noderight = noderight.nextNode
            continue
        if noderight == None:
            add(Lfinal,nodeleft.value)
            nodeleft = nodeleft.nextNode
            continue
        if nodeleft.value <= noderight.value:
            add(Lfinal,nodeleft.value)
            nodeleft = nodeleft.nextNode
        else:
            add(Lfinal, noderight.value)
            noderight = noderight.nextNode
    Lfinal = inverse(Lfinal) #le doy inverse para que queden ordenados de menor a mayor
    return Lfinal

L = LinkedList()
add(L,20)
add(L,3)
add(L,3)
add(L,1)
add(L,2)
add(L,6)
add(L,3)
add(L,41)
add(L,17)
print("Lista normal")
imprimirlista(L)
print("\nQuicksort")
Quicksort(L)
imprimirlista(L)
L2 = LinkedList()
add(L2,20)
add(L2,3)
add(L2,3)
add(L2,1)
add(L2,2)
add(L2,6)
add(L2,3)
add(L2,41)
add(L2,17)
print("\nLista normal again")
imprimirlista(L2)
print("\nMergesort")
L2 = MergeSort(L2)
imprimirlista(L2)

