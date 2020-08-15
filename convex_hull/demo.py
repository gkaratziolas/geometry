from tkinter import *
import time
import random

from convex_hull import *

width  = 1000
height = 1000

def draw_point(canvas, p, radius=3, colour="red"):
    x0 = p.x - radius
    y0 = p.y - radius
    x1 = p.x + radius
    y1 = p.y + radius
    canvas.create_oval(x0, y0, x1, y1, fill=colour, outline=colour)

def draw_line(canvas, p1, p2, width=1, colour="red"):
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=colour, width=width)

def fill_canvas(canvas, colour="white"):
    canvas.create_rectangle(0, 0, width+1, height+1, fill=colour)

def draw_lines(canvas, L):
    for i in range(0, len(L) - 1):
        draw_point(w, L[i], colour="green")
        draw_line(w, L[i], L[i+1], 3, "green")
    draw_point(w, L[-1], colour="green")

def draw_x_line(canvas, p):
    canvas.create_line(p.x, 0, p.x, height, width=2, fill="blue")

def convex_hull_demo(canvas, P):
    canvas.delete("all")
    ## Sort P lexograpically, by x ascending and then by y ascending.
    P.sort(key = lambda p : (p.x, p.y))

    L = [P[0], P[1]]
    L_end = 1

    ## Find the upper hull
    for i in range(2, len(P)):
        canvas.delete("all")
        fill_canvas(w)
        for p in P:
            draw_point(canvas, p)
        L.append(P[i])
        draw_x_line(canvas, P[i])
        L_end += 1
        draw_lines(canvas, L)
        canvas.update()
        time.sleep(0.01)
        while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
            L.pop(L_end - 1)
            L_end -= 1

    P.reverse()
    L.append(P[1])
    L_end += 1
    for i in range(2, len(P)):
        canvas.delete("all")
        fill_canvas(w)
        for p in P:
            draw_point(canvas, p)
        L.append(P[i])
        draw_x_line(canvas, P[i])
        L_end += 1
        draw_lines(canvas, L)
        canvas.update()
        time.sleep(0.01)
        while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
            L.pop(L_end - 1)
            L_end -= 1
            
    while L_end > 1 and not right_handed(L[L_end - 2], L[L_end - 1], L[L_end]):
        L.pop(L_end - 1)
        L_end -= 1
    fill_canvas(w)
    for p in P:
        draw_point(canvas, p)
    draw_lines(canvas, L)
    canvas.update()

    return L

master = Tk()
w = Canvas(master, width=width, height=height)
w.pack()

fill_canvas(w)

P = []
for i in range(0, 100):
    theta = random.uniform(0, 2 * math.pi)
    radius = random.uniform(0, 0.9)
    x = width  * (radius * math.cos(theta) / 2 + 0.5)
    y = height * (radius * math.sin(theta) / 2 + 0.5)
    P.append(Vec2(x, y))

while True:
    P = []
    for i in range(0, 100):
        x = random.randint(100, width  -100)
        y = random.randint(100, height -100)
        P.append(Vec2(x, y))

    convex_hull_demo(w, P)
    x = input()

mainloop()
