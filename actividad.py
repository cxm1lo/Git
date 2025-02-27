import math

def area_triangulo(s1: float, s2: float, s3: float)-> float:
    s = (s1 + s2 + s3)/2
    area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))
    return area

s1 = float(input("Ingrese el primer lado del triangulo: "))
s2 = float(input("Ingrese el segundo lado del triangulo: "))
s3 = float(input("Ingrese el tercer lado del triangulo: "))

areaT = area_triangulo(s1, s2, s3)
area_tri = round(areaT)
print ("El area del triangulo es de: "+str(area_tri))