import numpy as np

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

def calcul1(a,e,i,RT,mu,la,lon):
    ra = a * (1 + e)
    rp = a * (1 - e)
    za = ra - RT
    zp = rp - RT
    T = 2*np.pi*np.sqrt(a**3 / mu)
    n = np.sqrt(mu / a**3)
    Vp = np.sqrt(2*(-mu / (2*a)) + 2*(mu / rp))
    Va = np.sqrt(2*(-mu / (2*a)) + 2*(mu / ra))
    vpva = Vp / Va
    Vc = np.arccos(-e)
    print(n)
calcul1(40708,0.8320,61,6378,398600,0,120)


def correction (vc,v,):
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
            c = 2* np.pi
            u = 1
        else :
            c = -2 * np.pi
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

    elif v > (2*np.pi + vc):
        if i < 90:
            c = 2 * np.pi
            u = 1
        else :
            c = -2 * np.pi
            u = 1

    return (c,u)

def radtodeg(r):
    r = r * (180 / np.pi)
    print(r)
    return r

def degtorad(d):
    d = d * (np.pi / 180)
    print(d)
    return d

def correction2 (omega,v,):
    if v <= (-omega -90):
        c1 = -np.pi
        u1 = -1
    elif v >= (-omega -90) and v <= (-omega + 90):
        c1 = 0
        u1 = 1
    elif v >= (-omega + 90):
        c1 = np.pi
        u1 = -1
    return (c1,u1)
def calcult(a,mu,v,e,c,u,omega):
    List = [-210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210]
    v = - degtorad(omega)
    tp = -(np.sqrt((a**3) / mu) * (c + u * np.arcsin((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))- e * ((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))))
    print (tp)
    Tsec = []
    for j in List : 
        v = degtorad(j)
        t = (np.sqrt((a**3) / mu) * (c + u * np.arcsin((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v)))- e * ((np.sqrt(1 - e**2) * np.sin(v)) / (1 + e * np.cos(v))))) + tp
        print(t)
        Tsec.append(t)
    

def  calcullat(c,u,la,i):
    LA = np.arcsin(np.sin(omega + v) * sin i)
    L0 = c+u*np.arcsin((np.tan(la)/np.tan(i)))

