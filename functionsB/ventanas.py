
import autoit as ai
import functionsB.coordenadas as co
from time import sleep
from functionsB.os_functions import *
import win32clipboard as cp
import datetime
global detallesCuenta 

def CambiarPais(pais):
    sleep(3)
    print('Cambio de pais')
    #Da click en edicion
    click(co.barraHerramientas['edicion'])
    #Del menu desplegado, da clic en Cambiar cargo
    click(co.barraHerramientas['cambiarCargo'])
    
    #Selección de la lista 
    ventanaPaises =  'Change Position'
    ai.win_wait(ventanaPaises)
    ai.control_click(ventanaPaises,'[CLASS:SysListView32; INSTANCE:1]')
    sleep(3)
    
    # aux  = ai.control_list_view(ventanaPaises, '[CLASS:SysListView32; INSTANCE:1]', 'GetItemCount')
    # print('AUX:', aux)
    #Acomodar la ventana
    ai.win_move(ventanaPaises,239,190)
    
    #Seleccionar el primer pais
    ai.send('{UP 20}')
    #-----------------PAISES A ESCOGER-----------------------
    if pais == 'El Salvador':    
        ai.send('{DOWN 16}')
    elif pais== 'Costa Rica': 
        ai.send('{DOWN 3}') 
    elif pais == 'Panama': #Panama
        ai.send('{DOWN 8}')
    elif pais== 'Mexico': 
        ai.send('{DOWN}')    
    else:
        print('NO se encontró país')
        return 0
    #-----------------PAISES A ESCOGER-----------------------

    sleep(2)
    ai.send('{ENTER}') #confirma el pais que haya elegido
    return 1

def ingresarCuenta(cuenta):
    '''
    cuenta: numero en str
    
    regresa->        
        'clase' : claseCuenta,
        'tipo': tipoCuenta,
        'tipo_cliente': clienteCuenta,
        'fecha_corte': diadeCorte
    '''
    detallesCuenta = {
        
    }
    #Pantalla: Cuentas
    click(co.barraPantallas['cuentas'])
    sleep(2)
    
    #Vista: Resumen operativo
    click(co.barraVistas['resumenOperativo'],2)
    sleep(2)
    
    #limpieza de campos
    click(co.limpieza,2) 

    #Ingresa cuenta
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    
    '''Busco campos'''
    #NOTA: Esto deberia estar con 'control_click'
    sleep(1)
    #click(co.ingresoCuenta)
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:1]',clicks=1)
    sleep(1)
    #Ingresa la cuenta
    ai.send(cuenta)
    sleep(3)
    #Envia la cuenta
    ai.send('{ENTER}') 
    sleep(3)
    
    '''Copia campos'''
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:10]',clicks=2)
    claseCuenta = copyPaste()
    sleep(1)
    
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:11]',clicks=2)
    tipoCuenta = copyPaste()
    sleep(1)
    
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:12]',clicks=2)
    clienteCuenta = copyPaste()
    sleep(1)
    
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:14]',clicks=2)
    diadeCorte = copyPaste()
    sleep(1)
    #print(claseCuenta)
    
   
    
        
    detallesCuenta = {
        'clase' : claseCuenta,
        'tipo': tipoCuenta,
        'tipo_cliente': clienteCuenta,
        'fecha_corte': diadeCorte  #aqui, entonces llamala diferente, ponle dia de corte
    }
    
    return detallesCuenta, 1
    
    
    
def ingresarOrden(orden):
    '''Esta funcion ingresa las ordenes de servicio
    orden: cadenea str de ## digitos
    orden: no de orden
    '''
    
    #Pantalla: Solitudes de servicio
    sleep(5)
    printBox('Ingresa Orden')
    click(co.barraPantallas['solicitudes'],2)
    sleep(2)
    
    #Vista: Todas las solicitudes de servicio
    click(co.barraVistas['todasSolicitudes'],2)
    sleep(2)
    
    #limpieza de campos
    click(co.limpieza) 
    sleep(3)
    
    #Ingresa al campo de la orden
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    #ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:1]',clicks=1) #SOLUCIONARRRR!!!!!
    sleep(2)
    click(co.ingresoOrden,2)
    sleep(2)
    #Enviar orden
    ai.send(orden)
    sleep(3)
    ai.send('{ENTER}')
    # click(co.consulta,2)  #"Este es el enter"
    sleep(2)

    
    ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:1]',clicks=2)
    aux = copyPaste()

    if orden[3:] == aux:
        print('Orden ingresada correctamente')
        return 1
    else: 
        print('La orden no coincide')
        return 0
        

    
def crearCancelacion(tipoCancelacion):
    '''Esta funcion entra a actividades para crear la orden para hacer la actividad'''

    #En caso de que tenga que bajar el menu
    # click(co.barraVistas['down'],7)
    # sleep(2)
    printBox('Crea Actividad de Cancelacion')
    #Vista: Actividdes
    click(co.barraVistas['actividades'],2)
    sleep(4)
    
    #Nueva actividad
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    click([568, 555], numClics=2)
    
    ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:2]')
    sleep(3)
    #Seleecion de opcion: Programar cancelacion
    ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:1]')
    
    #CAmbio de acuerdo al tipo de proceso
    if tipoCancelacion == 'single_video':
        ai.send('p')
        sleep(2)
        ai.send('{ENTER}')
        #Campos Comentarios
        ai.send('{TAB}')
        ai.send('BAJA TOTAL')
    
    elif tipoCancelacion == 'modem_combo':
        ai.send('ccccc') #CAncelacion Equipo Secundario
        sleep(2)
        ai.send('{ENTER}')
        #Campos Comentarios
        ai.send('{TAB}')
        ai.send('BAJA BTI')
    
    else:
        ai.send('ccccc')
        sleep(2)
        ai.send('{ENTER}')
        #Campos Comentarios
        ai.send('{TAB}')
        ai.send('BAJA BTCel')
        


    #BOTON: CONTINUAR
    sleep(2)
    ret = ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:4]')
    sleep(6)
    #Validacion de que dio el clic correcto, quiza deba ser por 
    if ret == 1:
        return 1
    else:
    #Si no es, regresa 0
        return 0

def ordenarEquipos(orden='DESC'):
    '''Esta funcion ordena de forma descendente los equipos a cancelar'''
    print('---Ordena equipos---')
    sleep(5)
    click([228, 401],button='right')
    sleep(2)
    ai.send('{DOWN 6}')
    ai.send('{ENTER}')
    sleep(1)
    title = 'Sort Order'
    ai.win_move(title, 484, 340)
    ai.send('j')
    sleep(1)
    #sai.send('{ENTER}')
    sleep(1)
    ai.send('{TAB}')
    #click([676, 428]) #descending
    sleep(1)
    if orden == 'DESC':
        ai.send('{DOWN}')
        ai.send('{ENTER}')
        sleep(3)
    else:
        ai.send('{ENTER}')
        sleep(3)

    
    
    
    
def cancelacionExistente():
    sleep(2)
    click(co.barraVistas['actividades'],2)
    sleep(3)
    
    #Nueva actividad
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    click([193, 605],2)#SITUA EN ACTIVIDAD
    sleep(2)
    #AQUI JOCELYN
    click([364, 553])#NUEVO
    click([366, 602])
    ai.send('P')
    sleep(1)
    ai.send('{ENTER}')
    ai.send('{TAB}')
    ai.send('BAJA TOTAL')
    sleep(1)
    click([460, 553])
    sleep(2)
    # ret = 0
    # while ret==0:
    #     ret  = ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:3]')
    #     if ret == 0:
    #         print('No encontro el boton')
    #click([468, 562])
        
    sleep(6)
    
def cancelarEquipos(tipoCancelacion, tipoCuenta):
    '''Esta funcion desconecta todos los equipos de manera jerarquica
    fechacorte:L el dia que se aplicaran los cambios'''
    printBox('Cancelacion de equipos')
    sleep(5)
    click([444, 361]) #APLET: equipos

    if tipoCancelacion == 'single_video':
        print('Cancelacion SINGLE VIDEO')
        ordenarEquipos()
        sleep(1)
        ai.send('{TAB}') #Primer equipo en la lista
        for i in range(100):
            try:
                print('Equipo: ',i+1)
                sleep(2)
                ai.send('Disconnect')
                sleep(2)
                ai.send('{DOWN}')
                print(copyPaste())

            except Exception as e:
                print(e)
                print('Ya no hay más equipos')
                break
    elif tipoCancelacion == 'modem_combo':
        print('Cancelacion BTI')
        ordenarEquipos(orden='ASC')
        sleep(1)
        ai.send('{TAB 3}') #Primer equipo en la lista
        busqueda = 0
        while busqueda ==0:
            equipo = copyPaste()
            if equipo =='Modem (Principal)': 
                ai.send('{SHIFT}+{TAB}')
                sleep(1)
                ai.send('{SHIFT}+{TAB}')
                sleep(2)
                ai.send('Disconnect')
                sleep(1)
                ai.send('{TAB}')
                sleep(10)
                busqueda = 1
            else:
                try:
                    ai.send('{DOWN}')
                except:
                    return 0
                
        if tipoCuenta == 'HD': #NUEVA ERA
            print('Cuenta nueva era:')
            print('Lleva motivo')
            ventanaSiebel = ai.win_get_title('[ACTIVE]')
            ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:12]')
            sleep(1)
            ai.send('SKY NEW ERA')
            sleep(2)
        else:
            print('Cuenta tradicional, no lleva motivo')
    else: #CAncelacion telefonica
        print('Cancelacion BTCEL')

def confirmacionCancelacion(fechaCorte, tipoCuenta):
    printBox('Confirmacion de cancelacion')
   
    
    #Orden de Modificacion
    sleep(3)
    click(co.barraEquipos['ordenesModificacion'])
    click([96, 936])
    click(co.barraEquipos['resumenOrden'], numClics=2) #Cambiar coordenada
    
    sleep(3)
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
        
    if tipoCuenta == 'single_video':
        print('Single Video')
        ai.send('{TAB 3}')
        ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:17]') #feCHA
    
        #primero debes de saber que dia es hoy
        dt = datetime.datetime.today() 
        #le preguntamos ala clase datetime por el la fecha del dia
        #luego extraemos esl dia que deberia ser 29
        hoy = int(dt.day)
        mes = int(dt.month)
        fecha = int(fechaCorte) #aqui va fecha de la API  

        if hoy  <= fecha :
        
            print("Mismo mes, dia posterior")
        
            fecha = dt.replace(day=fecha).strftime("%d/%m/%Y")
            print(fecha)
        else:
            print("Mes siguiente, dia anterior")
            #y si nel pastel, ahora remplazamos el mes con el mismo mes en curso mas 1
            fecha = dt.replace(day=fecha,month=mes+1).strftime("%d/%m/%Y")
            print(fecha)
        sleep(3)
        ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:21]')
        sleep(2)
        cleanField()
        ai.send('BAJA TOTAL')
        
    elif tipoCuenta == 'modem_combo':
        print('MODEM EN COMBO')
        sleep(3)
        ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:21]')
        sleep(2)
        cleanField()
        ai.send('CANCELACION MODEM')
    else: 
        sleep(3)
    #     ai.control_click(ventanaSiebel,'[CLASS:Edit; INSTANCE:21]')
    #     sleep(2)
    #     cleanField()
    #     ai.send('CANCELACION BTCEL')
    
    
def botonEnviar(tipoCuenta):
    printBox('Enviar equipos')
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    sleep(2)
    ai.control_click(ventanaSiebel,'[CLASS:Button; INSTANCE:8]') #enviar
    sleep(5)
    ai.send('{ENTER}')   
    intentos = 0
    while intentos <=3:
        try:
            sleep(3)
            ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:18]')
            sleep(2)
            # ai.send(bt.btnSeleccion)
            # ai.send(bt.btnCopiar)
            # cp.OpenClipboard() 
            # estado = cp.GetClipboardData()
            # cp.EmptyClipboard()
            # cp.CloseClipboard()
            estado = 'Progress' #SI ESTO NO SE PUEDE COPIAR SE DEBE USAR TESSEREACT
            sleep(2)
            'Esperando estado....'
            if tipoCuenta == 'single_video':
                if estado == 'Future Action' or  estado =='Action' or  estado =='Future':
                    print('Solicitud en proceso, ciclo completo')
                    return 1
                else:
                    intentos +=1
                    print('Intentos',intentos)
                    
                    if intentos ==3:
                        return 0
            elif tipoCuenta =='modem_combo' or tipoCuenta == 'btcel_combo':
                if estado == 'In Progress' or  estado =='Progress':
                    print('Solicitud en proceso, ciclo completo')
                    return 1
                else:
                    intentos +=1
                    print('Esperando estado, intento: ',intentos)
                    
                    if intentos ==3:
                        print('El estado no ha cambiado, notificar a alguienssss')
                        return 0
            else: 
                print('No se encontro el tipo de cancelacion')
        except Exception as e:
            print('ERROR NO SE COMPLETO EL CICLO')
            print(e)
            
        
def solicitud(fechaCorte_completa):
    '''Rellena la solicitud
    recibe:
    super: str
    motivo: option
    padre: str (clave del ejecutivo)
    fecha vencimietno: fecha corte
    herramienta de retencion: option
    subestado: CANCELADO
    estatus: CERRADO
    '''
    sleep(5)
    
    #Tiene que buscar la pagina donde esta la cuenta
    #IMPORTANTEEEE: DEBEN VALIDAR QUE DE CLIC LAS VECES NECESARIAS PARA LLEGAR A LA PANTALLA CORRECTA
    click([124, 85])
    sleep(1)
    click([124, 85])
    sleep(1)
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    ai.control_click(ventanaSiebel, '[CLASS:Button; INSTANCE:87]') #PAra regresar por el hilo de nvegacion

    sleep(3)
    click(co.barraVistas['retencion'],numClics=2)  #Vista Solicitud de retencion
    sleep(3)
    click([58, 422]) #Aplet
    sleep(1)
    #COMIENZA RELLENADO
    ventanaSiebel = ai.win_get_title('[ACTIVE]')
    #Supervisor:
    ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:16]')
    ai.send('{BACKSPACE 10}')
    ai.send('USUARIO PRUEBA')
    sleep(0.5)
    ai.send('{TAB}')
    sleep(0.5)
    
    #Motivo
    ai.send('Programacion/ Salida de canal') #DEBE SER EL MOTIVO QUE SE USE
    sleep(1)
    sleep(1)
    #PAdre
    ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:22]')
    ai.send('{BACKSPACE 10}')
    ai.send('USUARIO PRUEBA')
    ai.send('{TAB 2}')
    sleep(1)
    
    #fecha vencimiento:
    ai.send(fechaCorte_completa)
    sleep(1)
    
    #Herramienta:
    ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:27]')
    ai.send('Promocion de Condonacion')
    sleep(1)
    
    #Subestado
    ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:21]')
    ai.send('{BACKSPACE 10}')
    ai.send('Cerrado')
    sleep(1)
    
    #Estatus
    ai.control_click(ventanaSiebel, '[CLASS:Edit; INSTANCE:20]')
    ai.send('{BACKSPACE 10}')
    ai.send('Cancealdo')
    
    
    #NO DICE SE SE DA CLICK EN EL BOTN DE ENVIAR O ALGO ASI
    

    return 1