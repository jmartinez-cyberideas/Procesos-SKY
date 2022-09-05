import os
import autoit as ai
from time import sleep
import win32clipboard as cp
import functionsB.botones as bt
import autoit as ai

def kill(name):
    '''
    name: nombre del programa a cerrar
    '''
    
    print('⋆'*50)
    print('Cerrando {0}...'.format(name))
    os.system("taskkill /f /im {0}".format(name))
    print('⋆'*50)
    
def printBox(string):
    '''
    string: cadena a imprimir en una caja
    '''
    print('-'*(len(string)+4))
    print('| {} |'.format(string))
    print('-'*(len(string)+4))



'''FUNCIONES MODIFCADAS DE AUTOIT'''
def click(coordenadas,numClics=1, button ='left'):
    '''tupla x,y
    numCLics: opcional
    + 1 sleep'''
    
    x, y = coordenadas
    ai.mouse_click(button,x,y,numClics)
    sleep(1)

def copyPaste():
    sleep(2)
    ai.send(bt.btnCopiar)
    cp.OpenClipboard() 
    aux = cp.GetClipboardData()
    cp.EmptyClipboard()
    cp.CloseClipboard()
    sleep(2)
    return aux

def cleanField():
    '''Limpia el campo sobre el que se va escribir'''
    sleep(2)
    ai.send(bt.btnSeleccion)
    ai.send('{BS}')
    


#printBox('PEDRO JUAN CARAL ERIK')
#kill('siebel.exe')