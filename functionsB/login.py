#import os 
import autoit as ai
from time import sleep
import functionsB.os_functions  as of

def Login(user, password):
    '''
    Requiere:
    user: USUARIO
    password: CONTRASEÑA'''
    
    #Cierra Siebel si es que existe
    print('✺'*60)
    of.printBox('INICIO EN SIEBEL')
    of.kill('siebel.exe')
    of.kill('siebel.exe')
    
    #Ruta de SIebel
    
    rutaSiebel = "C:\sea\client\BIN\siebel.exe /c 'c:\sea\client\\bin\scomm_hj_preprod.cfg'"
    
    #Inicia Siebel
    ai.run(rutaSiebel)
    
    #Espera que Siebel aparezca
    sleep(3)
    
    #Obtener el titulo de la venatan
    ventanaSiebel = 'Siebel eCommunications' 
    print('Ingreso de credenciales')
    '''Ingreso de contraseñas'''
    ai.control_send(ventanaSiebel,'[CLASS:Edit; INSTANCE:1]', user)
    sleep(1)
    ai.control_send(ventanaSiebel,'[CLASS:Edit; INSTANCE:2]', password)
    
    '''Seleeción de tipo de conexión'''
    ai.control_click(ventanaSiebel,'[CLASS:ComboBox; INSTANCE:1]') #seleccion del menu
    ai.control_send(ventanaSiebel,'[CLASS:ComboBox; INSTANCE:1]', 'server') #ingreso de opcion
    ai.send('{ENTER}')#aceptacion de la opción 
    sleep(1)
    '''Ingreso '''
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:1]')
    sleep(1)
    ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:1]')  #Clic en "OK"
    
    #Maximizar ventana
    sleep(3)
    ai.win_set_state(ventanaSiebel,3)
    print('Maximizar venatana')
    print('✺'*60)