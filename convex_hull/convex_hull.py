import math

class Vec2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    def argument(self):
        return math.atan(self.y / self.x)

def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross_product(v1, v2):
    """Return the length of the resultant vector in z"""
    return v1.x * v2.y - v1.y * v2.x

def anticlockwise_angle(v1, v2):
    """
    Returns the anticlockwise angle must you turn through to arrive at v2 from
    v1
    Return value in range -pi < theta <= pi
    """
    return math.atan2(cross_product(v1, v2), dot_product(v1, v2))

def vec_add(v1, v2):
    return Vec2(v1.x + v2.x, v1.y + v2.y)

def vec_subtract(v1, v2):
    """Return a new vector made by taking v2 from v1"""
    return Vec2(v1.x - v2.x, v1.y - v2.y)

def right_handed(p1, p2, p3):
    """
    Determines whether a line drawn from p1 to p2 has to turn right to connect
    to p3.
    """
    v1 = vec_subtract(p2, p1)
    v2 = vec_subtract(p3, p2)
    theta = anticlockwise_angle(v1, v2)
    # If theta is positive, it is a left-hand turn
    # If theta is zero, it is a straight line, considered a non-right turn 
    if theta >= 0:
        return False
    return True

def convex_hull(P):
    """
    For a set of points P ∈ ℝ², return the minial set of points of that fully
    enclose P.
    Takes a list of n points P in form P = [[x,y] * n].
    Returns a list of points L, with members selected from P.
    Points of L are liested in clockwise order and define the convex hull of P. 
    """

    ## Deal with unusual inputs
    ## Any set with 3 points or fewer is it's own convex hull when drawn in 
    ## any order.
    if len(P) < 4:
        return P

    ## Sort P lexograpically, by x ascending and then by y ascending.
    P.sort(key = lambda p : (p.x, p.y))

    L = [P[0], P[1]]
    L_end = 1

    ## Find the upper hull
    for i in range(2, len(P)):
        L.append(P[i])
        L_end += 1
        while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
            L.pop(L_end - 1)
            L_end -= 1

    P.reverse()
    L.append(P[1])
    L_end += 1
    for i in range(1, len(P)):
        L.append(P[i])
        L_end += 1
        while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
            L.pop(L_end - 1)
            L_end -= 1

    while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
        L.pop(L_end - 1)
        L_end -= 1

    canvas.update()

    return L

if __name__ == "__main__":
    #test:
    for x in range(0, 100):
        theta = math.pi * x * 2 / 100
        v0 = Vec2(1, 0)
        v1 = Vec2(math.cos(theta), math.sin(theta))
        print("{} : {}".format(theta, anticlockwise_angle(v0, v1)))
