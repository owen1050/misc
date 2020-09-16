import math

_D = 0
_L = 2

_MP = (10,0)

_MP1 = (_MP[0]-_D/2, _MP[1])
_MP2 = (_MP[0]+_D/2, _MP[1])


def getCoord(theta):
    global _D, _L, _MP1, _MP2



def getL(theta, L1):
    global _D, _L, _MP1, _MP2
    thetaI = math.pi - theta
    dx = math.cos(thetaI) * L1
    dy = math.sin(thetaI) * L1
    xp = _MP1[0] + dx
    yp = _MP1[1] + dy

    point = (xp, yp)
    return dist(point, _MP1) + dist(point, _MP2), point

def dist(p1, p2):
    dx = abs(p1[0]-p2[0])
    dy = abs(p1[1]-p2[1])
    return math.sqrt(dx*dx+dy*dy)

def abRatToDL(abRatio):
    global _L, _D
    b = 1
    a = abRatio * b

    _L = 2 * a
    _D = 2 * math.sqrt((a*a) - (b*b))


abRatToDL(2)
print(_L, _D)
thetaI = 0
dT = 0.01
points = []

while(thetaI < math.pi):

    tryL = 0
    dL = 0.01
    Lcalc = 0
    while(Lcalc < _L):
        tryL = tryL + dL
        Lcalc = getL(thetaI, tryL)[0]

    points.append(getL(thetaI, tryL)[1])
    thetaI = thetaI + dT

num = len(points)
i = 0
per = 0
while(i < num - 1):
    print(points[i])
    per = per + dist(points[i], points[i+1])
    i = i + 1
print(_MP, _MP1, _MP2)
print(per * 2) 