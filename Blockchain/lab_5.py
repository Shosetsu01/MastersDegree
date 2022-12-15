import random
import time
import hashlib
from math import pow

n = 'FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141'.replace(' ','')
n = int(n, base=16)
Gx = '79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798'.replace(' ','')
Gx = int(Gx, base=16)
Gy = '483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8'.replace(' ','')
Gy = int(Gy, base=16)
a = 0
b = 7
q = 'FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F'.replace(' ','')
q = int(q, base=16)


def extgcd (a, b):
    if a < b :
        b,a = a,b
    U = (a, 1, 0)
    V = (b, 0, 1)
    while(V[0] != 0):
        n = U[0] // V[0]
        T = (U[0] % V[0], U[1] - n * V[1], U[2] - n * V[2])
        U = V
        V = T
    return U[2]



class Point: 
    def __init__(self, x, y,):
        self.x = x 
        self.y = y 

    def __eq__(self, other):
        return self.x == other.x  and self.y == other.y

    def __str__(self):
        return "x= {0}, y = {1}".format(self.x, self.y)
P = Point(Gx, Gy, )

def sum_points(val1, val2, a):
    global q
    if val1.x == 0 and val1.y == 0:
        return val2
    if val1 == val2: 
        if val1.y:
            if 2 * val1.y < 0:
                tmp = extgcd((-2 * val1.y) % q, q) % q
                l = (-(3 * val1.x ** 2  + a) * tmp) % q
            else:
                tmp = extgcd((2 * val1.y) % q, q) % q
                l = ((3 * val1.x ** 2  + a) * tmp) % q
            x = (l ** 2 - 2 * val1.x) % q
            y = (l * (val1.x - x ) - val1.y) % q
            return Point(x, y,)
        else :
            return None
    else:
        if val1.x == val2.x:
            return None
        else:
            if val2.x - val1.x < 0:
                tmp = extgcd( (-(val2.x - val1.x)) % q  , q) % q
                l = (-(val2.y - val1.y ) * tmp )% q
            else:
                tmp = extgcd((val2.x - val1.x) % q  , q) % q
                l = ((val2.y - val1.y ) * tmp )% q            
            x = (l ** 2 - val1.x - val2.x) % q
            y = (l * (val1.x - x ) - val1.y) % q
            return Point(x, y ,)


def multiplication_point(p, k, a):
    answer = Point(0, 0)
    D = p
    for i in range(k.bit_length()):
        if k >> i & 1:
            answer = sum_points(answer, D, a)
        D = sum_points(D, D, a)
    return answer




def generate_keys():
    global n
    global P
    global a
    random.seed(time.time(), version=2)
    d = random.randint(1, n-1)
    Q = multiplication_point(P, d, a)
    return (d, Q)

def generate_sign(d, m):
    global n
    global P
    global a
    r = None
    s = None
    while s is None or s == 0: 
        while r is None or  r == 0:
            k = random.randint(1, n-1)
            x = multiplication_point(P, k, a).x
            r = x % n 
            if r != 0:
                break
        
        h = hashlib.sha256(m.encode())
        e = int.from_bytes(h.digest(), byteorder='big') % n
        k = extgcd(k, n) % n
        s = (k * (e + (d * r)) % n)
        if s != 0:
            break
    return (r, s)

def verifivtion_sign(r, s, m, Q):
    
    h = hashlib.sha256(m.encode())
    e = int.from_bytes(h.digest(), byteorder='big') % n
    w = extgcd(s, n) % n
    U1 = (w * e) % n
    U2 = (r * w) % n
    tmval1 = multiplication_point(P, U1, a)
    tmval2 = multiplication_point(Q, U2, a)
    X = sum_points(tmval1,  tmval2, a)
    if X is None:
        return 'no'
    v = X.x % n
    if v == r: 
        return 'yes'
    else: 
        return 'no'

d, Q = generate_keys()    
print(d, Q)
r, s = generate_sign(d, ';l;lk;ll;jjf')
print(verifivtion_sign(r, s, ';l;lk;ll;jjf', Q))