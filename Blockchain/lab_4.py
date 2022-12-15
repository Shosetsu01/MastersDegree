
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x  and self.y == other.y

    def __str__(self):
        return "x= {0}, y = {1}".format(self.x, self.y)


def sum_points(val1, val2, a):
    if val1 == val2: 
        if val1.y:
            l = (3 * val1.x ** 2  * a) / (2 * val1.y)
            x = l ** 2 - 2 * val1.x
            y = l * (val1.x - x) - val1.y
            return Point(x, y)
        else :
            return 0
    else:
        if val1.x == val2.x:
            return 0
        else:
            l = (val2.y - val1.y) / (val2.x - val1.x)
            x = l ** 2 - val1.x - val2.x
            y = l * (val1.x - x) - val1.y
            return Point(x, y)


def multiplication_point(p, k, a):
    answer = Point(0, 0)
    D = p
    for i in range(k.bit_length()):
        if k >> i & 1:
            answer = sum_points(answer, D, a)
        D = sum_points(D, D, a)
    return answer



val1 = Point(1, 1)
val2 = Point(4, 3)
print(sum_points(val1, val2, 4)) 
print(multiplication_point(val1, 3, 4)) 

              
