
import autoit as ai
from shutil import ExecError
from functionsB.login import *
import service.API as api 
from functionsB.ventanas import *




def main():
    
    # login = api.authenticate('10.251.58.11', 'SKY\\usrconfbot', 'MJG_37465ftg')
        
        
    # print(login)
    # return
    while True == True:
        
        
        
        
        datosAPI = api.CuentaNueva()
        
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬LOGIN▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        '''Falta agregarle 3 intentos'''
        try:
            Login('USRREP2','Prueba_sky09082022pre?')
            print('Inició sesión con exito')
        except Exception as e:
            print('ERROR EN LOGIN',e)
            exit()
            
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬PAISES▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        '''Falta agregarle 3 intentos'''
        flag_pais = 0
        intentos = 0
        while flag_pais ==0:
            try: 
                flag_pais = CambiarPais(datosAPI[2])
                print('Se cambió país')
            except Exception as e:
                print('ERROR EN CAMBIAR EL PAIS',e)
                intentos +=1
                print('Intentos de PAIS: ',intentos)
                if intentos == 3:
                    print('Se alcanzó el maximo de intentos deingreso de la cuenta')
                    return 400
            
            
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬CUENTA▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        flag_cuentaIngresada = 0
        intentosCuenta = 0
        while flag_cuentaIngresada == 0:
            try:
                global detallesCuenta
                detallesCuenta,  flag_cuentaIngresada = ingresarCuenta(datosAPI[0])
                print('Cuenta ingresada. \n Detalles: ', detallesCuenta)
                intentosCuenta +=1
            except Exception as e:
                print('ERROR AL INGRESAR CUENTA: \n',e)
                intentosCuenta +=1
                print('Intentos de Cuenta: ',intentosCuenta)
                if intentosCuenta == 3:
                    print('Se alcanzó el maximo de intentos deingreso de la cuenta')
                    return 400

    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ORDEN Y CANCELACION▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

        flag_ordenIngresada = 0
        intentosOrden = 0 
        while flag_ordenIngresada == 0:
            try:
                flag_ordenIngresada = ingresarOrden(datosAPI[1]) #Ingresa Orden de Servicio
                crearCancelacion() #Crea cancelacion
                
                print('Orden Ingresada')
                intentosOrden +=1
            except Exception as e:
                print('ERROR AL INGRESAR NO ORDEN: \n',e)
                
                intentosOrden +=1
                
                print('Intentos de Orden: ',intentosOrden)
                if intentosOrden == 3:
                    print('Se alcanzó el maximo de intentos de la Orden: ',datosAPI[1]) 
                    return 400

            
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬EQUIPOS CANCELADOS▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        intentos = 0
        errorCancelar = 0
        while errorCancelar==0:
            try:
                cancelarEquipos()
                errorCancelar = 1
                # print('Flag cancelar equipos:',errorCancelar)
            except Exception as e:
                print('ERROR AL CANCELAR EQUIPOS: \n',e)
                intentos =+1
                click(co.barraPantallas['solicitudes'],2)
                sleep(2)
                if intentos == 3:
                    print('Se alcanzó el maximo de intentos de cancelarEquipos') 
                    return 400         

    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬FECHA DE CANCELACION▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        fechaCorte = detallesCuenta["fecha_corte"] #API
        print('Fecha de corte: ',fechaCorte)
        intentos = 0
        fechaCambiada =0
        while fechaCambiada == 0 :
            try:
                cambioFechas(fechaCorte)
                fechaCambiada =1
            except Exception as e:
                print('ERROR AL ESCRIBIR FECHA DE CORTE \n',e)
                intentos +=1
                if intentos ==3:
                    print('Se alcanzó el maximo de intentos de cambioFechas') 
                    return 400 
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬Envio de orden cacneladad ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        intentos = 0
        enviado = 0
        while enviado == 0 :
            try:
                print('Enviar')
                enviado = botonEnviar()
                if enviado == 1:
                    print('Envio exitoso')
                    sleep(400)
            except Exception as e:
                print('ERROR AL ENVIAR ORDEN \n',e)
                intentos +=1
                
                if intentos ==3:
                    print('Se alcanzó el maximo de intentos de al enviar la orden') 
                    return 400 
    #▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬creacion de solicitud▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        intentos = 0
        flag_solicitud = 0
        while flag_solicitud ==0 :
            try:
                printBox('Solicitud de Retencion')
                flag_solicitud = solicitud()
                printBox('Solicitud envidad')
            except Exception as e:
                print('ERROR AL ENVIAR SOLICITUD \n',e)
                intentos +=1        
                if intentos ==3:
                    print('Se alcanzó el maximo de intentos de al enviar SOLCITUD') 
                    return 400 

'''█████████████████ M  A I N ████████████'''



def reinicio(count):
    count +=1
    estado = main()
    if estado == 400:
        reinicio(count)

reinicio(0)