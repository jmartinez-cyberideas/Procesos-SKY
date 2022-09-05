

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
    
    paises:
    "Mexico", "Costa Rica", "Panama", "Nicaragua", "El Salvador", " R. Dominicana", "Guatemala", "Honduras"
    '''
    #CUENTAS DE PRUEBA: cuenta, os, pais
    #SINGLE VIDEO
    PA = ['501054797284','81-143696540549', 'Panama','cve_supervisor','cve_usuario', '2022-08-03','single_video' ] #MUERTA
    HN = ['501183469854','81-143696540540','Honduras','cve_supervisor','cve_usuario', '2022-08-03','single_video']
    SV = ['501135967542','81-1436ss96943835', 'El Salvador','cve_supervisor','cve_usuario', '2022-08-03','single_video']
    MX = ['501182736337','81-143696540535', 'Mexico']
    CR = ['501069622352', '81-143696540556','Costa Rica','cve_supervisor','cve_usuario', '2022-08-03','single_video']
    
    #MODEM COMBO BTI
    MX_bti_newEra = ['501118484663','81-143696540561', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','modem_combo']
    MX_bti_standar = ['501117384377','81-143696540563', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','modem_combo']
    
    #BTCEL
    MX_btcel = ['501032165406','81', 'Mexico','cve_supervisor','cve_usuario', '2022-08-03','btcel_combo']

    
    return MX_bti_standar


#def authenticate(address, username, password):
    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    return conn.simple_bind_s(username, password)