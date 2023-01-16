import numpy as np
import sympy as sp
import webbrowser
#récupération données
def donnees ():
    a = float(input('valeur a  '))
    e = float(input("valeur e"))
    i = float(input("valeur i en degrès "))
    RT = float(input("valeur RT"))
    mu = float(input("valeur mu T"))
    la = float(input("valeur latitude"))
    lon = float(input("valeur longitude"))
    omega = float(input("valeur oméga"))
webbrowser.open('https://www.youtube.com/watch?v=jqJAn39umHs')

def calcul1(a,e,i,RT,mu,la,lon):
    ra = a * (1 + e)
    print( "ra =",ra,"km")
    
    rp = a * (1 - e)
    print("rp = ",rp,"km")
    
    za = ra - RT
    print("za = ", za,"km")
    
    zp = rp - RT
    print("zp = ",zp,"km")
    
    T = 2*np.pi*np.sqrt(a**3 / mu)
    print("T = ", T,"sec")
    
    n = np.sqrt(mu / a**3)
    print("n= ",n,"rad.sec-1")
    
    Vp = np.sqrt(2*(-mu / (2*a)) + 2*(mu / rp))
    print("Vp = ",Vp,"km.sec-1")
    
    Va = np.sqrt(2*(-mu / (2*a)) + 2*(mu / ra))
    print("Va = ",Va,"km.sec-1")
    
    vpva = Vp / Va
    print("Vp/Va = ", vpva)
    
    Vc = np.arccos(-e)
    print("Vc =",Vc,"rad")
    return(Vc)

def correction (vc,v,i):
    v = degtorad(v)
    if v <= (-2 * np.pi -vc):
        if i < 90:
            c = -3* np.pi
            u = -1
        else :
            c = 3 * np.pi
            u = -1
    elif v >= (-2 * np.pi - vc) and v <= (-2*np.pi + vc):
        if i < 90:
            c = -2* np.pi
            u = 1
        else :
            c = 2 * np.pi
            u = 1
    elif v >= (-2 * np.pi + vc) and v <= (-vc):
        if i < 90:
            c = -np.pi
            u = -1
        else :
            c = np.pi
            u = -1

    elif v >= (-vc) and v <= (vc):
        if i < 90:
            c = 0
            u = 1
        else :
            c = 0
            u = 1

    elif v >= (vc) and v <= (2*np.pi - vc):
        if i < 90:
            c = np.pi
            u = -1
        else :
            c = -np.pi
            u = -1

    elif v >= (2 * np.pi - vc) and v <= (-2*np.pi + vc):
        if i < 90:
            c = 2 * np.pi
            u = 1
        else :
            c = -2 * np.pi
            u = 1

    else:
        if i < 90:
            c = 3 * np.pi
            u = -1
        else :
            c = -3 * np.pi
            u = -1
    return(c,u)

def radtodeg(r):
    r = r * (180 / np.pi)
    return r

def degtorad(d):
    d = d * (np.pi / 180)
    return d

def correction2 (omega,v):
    webbrowser.open('https://www.youtube.com/watch?v=jqJAn39umHs')
    if v <= (-omega -90) and v>=(-omega -180):
        c1 = -np.pi
        u1 = -1
    elif v >= (-omega -90) and v <= (-omega + 90):
        c1 = 0
        u1 = 1
    elif v >= (-omega + 90) and v<= (-omega +90 +180):
        c1 = np.pi
        u1 = -1
    elif v >= (-omega + 90 + 180) and v<= (-omega +90 +270):
        c1 = 2 * np.pi
        u1 = -1
    else :
        c1 = 3 * np.pi
        u1 = -1
    return(c1,u1)


def calcult(a,mu,e,omega,lon,i,vc):
    Vt = [-210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210]
    u = correction(vc,-omega,i)[1]
    c = correction(vc,-omega,i)[0]
    v = -omega
    v = degtorad(v)
    tp = -(np.sqrt((a**3) / mu) * (c + u * np.arcsin((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))- e * ((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))))
    print ("tp = ",tp)
    Tsec = []
    LAS = []
    LOS  = []
    LSS = []
    for j in Vt :
        u = correction(vc,j,i)[1]
        c = correction(vc,j,i)[0]
        v = degtorad(j)
        t = (np.sqrt((a**3) / mu) * (c + u * np.arcsin((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))- e * ((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v))))) + tp
        Tsec.append(t)
        
        u1 = correction2(omega,radtodeg(v))[1]
        c1 = correction2(omega,radtodeg(v))[0]
        
        LA = radtodeg(np.arcsin(np.sin(degtorad(omega) + v) * np.sin(degtorad(i))))
        LAS.append(LA)
        
        LO = radtodeg(c1+u1*np.arcsin((np.tan(degtorad(LA))/np.tan(degtorad(i)))))
        LOS.append(LO)
        
        LS = lon + LO - (360 / 86164) * (t)
        LSS.append(LS)
    Vt.insert(0,"v")
    Tsec.insert(0,"t")
    LAS.insert(0,"lat")
    LOS.insert(0,"lon")
    LSS.insert(0,"L")
    Tablefin = sp.Matrix([Vt,Tsec,LAS,LOS,LSS])
    sp.pprint( Tablefin)
    
    return Tablefin

def resolution ():
    a = float(input('valeur a  '))
    e = float(input("valeur e"))
    i = float(input("valeur i en degrès "))
    RT = float(input("valeur RT"))
    mu = float(input("valeur mu T"))
    la = float(input("valeur latitude"))
    lon = float(input("valeur longitude"))
    omega = float(input("valeur oméga"))
    calcul1(a,e,i,RT,mu,la,lon)
    calcult(a,mu,e,omega,lon,i,calcul1(a,e,i,RT,mu,la,lon))
    
    
def resolution2 ():
    calcul1(40708,0.8320,61,6378,398600,0,120)
    calcult(40708,398600,0.8320,270,120,61,calcul1(40708,0.8320,61,6378,398600,0,120))
resolution()


