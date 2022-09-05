

def CuentaNueva():
    '''Datos de FORMULARIO
    return:
    
    cuenta:             [0] 
    ordenServicio:      [1] 
    pais: "Costa Rica"  [2] 
    cve_supervisor:     [3]
    cve_usuario:        [4] 
    fechaCorte:         [5] 
    tipoCancelacion:    [6]
    DN:                 [7] 
    
    paises:
    "Mexico", "Costa Rica", "Panama", "Nicaragua", "El Salvador", " R. Dominicana", "Guatemala", "Honduras"
    '''
    #CUENTAS DE PRUEBA: cuenta, os, pais
    #SINGLE VIDEO
    PA_no = ['501054797284','81-143696540549', 'Panama','cve_supervisor','cve_usuario', '2022-08-03','single_video',[''] ] #MUERTA
    HN_no = ['501183469854','81-143696540540','Honduras','cve_supervisor','cve_usuario', '2022-08-03','single_video',['']]
    SV_no = ['501135967542','81-1436ss96943835', 'El Salvador','cve_supervisor','cve_usuario', '2022-08-03','single_video',['']]
    MX_no = ['501182736337','81-143696540535', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','single_video',['']]
    CR_no = ['501069622352', '81-143696540556','Costa Rica','cve_supervisor','cve_usuario', '2022-08-03','single_video',['']]
    
    RD = ['501040054105', '81-143696540551','R. Dominicana','cve_supervisor','cve_usuario', '2022-08-03','single_video',['']]
    #MODEM COMBO BTI
    MX_bti_newEra = ['501118484663','81-143696540561', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','modem_combo',['']]
    MX_bti_standar = ['501117384377','81-143696540563', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','modem_combo',['']]
    
    #BTCEL
    MX_btcel = ['501032165406','81-143696540565', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','btcel_combo',['Slave1']] #Si pueden se mas de 1

    
    return RD


#def authenticate(address, username, password):
    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    return conn.simple_bind_s(username, password)