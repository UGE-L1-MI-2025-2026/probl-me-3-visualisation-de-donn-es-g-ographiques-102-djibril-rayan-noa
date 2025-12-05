import shapefile
import fltk as fl
import math

def init():
    francebox = []
    france = []
    sf = shapefile.Reader("departements-20180101")
    #r = sf.records()
    for i in range(len(sf)):
        departements = sf.shape(i)
        box = seine_et_marne.bbox
        points = departements.points
        francebox.append(box)
        france.append(points)
    print(box)
    #print(points)
    return france, francebox

def convertir():
    r = 2000
    france = init()
    carte = []
    cartebox = []
    for i in france:
        poly = []
        for j in i:
            coord = []
            long = j[0]
            lati = j[1]
            lon = math.radians(long)
            lat = math.radians(lati)
            x = r * lon + 850
            y = r * math.log(math.tan(math.pi / 4 + lat / 2)) - 1400
            coord.append(x)
            coord.append(hauteur - y)
            poly.append(coord)
        carte.append(poly)
    for i in francebox:
        polybox = []
        for j in i:
            coord = []
            long = j[0]
            lati = j[1]
            lon = math.radians(long)
            lat = math.radians(lati)
            x = r * lon + 850
            y = r * math.log(math.tan(math.pi / 4 + lat / 2)) - 1400
            coordbox.append(x)
            coordbox.append(hauteur - y)
            polybox.append(coord)
        carteox.append(polybox)
    #print(carte)
    return carte

def tracer():
    global longueur, hauteur
    longueur = 1920
    hauteur = 1000
    carte = convertir()
    fl.cree_fenetre(longueur, hauteur)
    for i in carte:
        for j in i:
            fl.polygone(j)

tracer()
fl.attend_fermeture()