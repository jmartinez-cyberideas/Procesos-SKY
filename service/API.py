#import ldap

def CuentaNueva():
    '''PETICION A LA BASE
    retunr: [0]cuenta, [1]orden, [2]pais'''
    noCuenta = '501135967542'
    ordenServicio = '81-143696540540'
    
    HN = ['501183469854','81-143696540540','HN']
    SV = ['501135967542','81-143696943835', 'SV']
    MX = ['501182736337','81-143696540535', 'MX']
    PN = ['501054797284','', '']
    CR = ['501182684834','', '']
    PA = ['501054797284','81-143696540549', 'PA'] #PANAMA
    RD = ['501040054105','', '']
    return PA


#def authenticate(address, username, password):
    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    return conn.simple_bind_s(username, password)