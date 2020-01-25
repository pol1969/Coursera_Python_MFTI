#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
#import pygame
import time

logging.basicConfig(filename="sample.log", level=logging.INFO)
 

SCREEN_DIM = (800, 600)
# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

def sub(x, y):
    """"возвращает разность двух векторов"""
    return x[0] - y[0], x[1] - y[1]


def add(x, y):
    """возвращает сумму двух векторов"""
    return x[0] + y[0], x[1] + y[1]


def length(x):
    """возвращает длину вектора"""
    return math.sqrt(x[0] * x[0] + x[1] * x[1])


def mul(v, k):
    """возвращает произведение вектора на число"""
    return v[0] * k, v[1] * k


def vec(x, y):
    """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
    координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
    return sub(y, x)



# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

class Vec2d():
    def __init__(self,x, y):
        self.x = x
        self.y = y

    @classmethod
    def fromPoint(cls,p):
        return cls(p[0],p[1])

    def __sub__(self, other):
        """"возвращает разность двух векторов"""
        a = self.x - other.x
        b = self.y - other.y
        return Vec2d(a, b)


    def __add__(self, other):
        """возвращает сумму двух векторов"""
        a = self.x + other.x
        b = self.y + other.y
        return Vec2d(a, b)


    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)


    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return  Vec2d(self.x * k, self.y * k)

    def __getitem__(self,key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

    def int_pair(self):
        return (self.x, self.y)

    def __str__(self):
        return str(self.x) + str(self.y)
    
    def __repr__(self):
        return str(self.x) +" "+ str(self.y)

class Polyline():
    def __init__(self):
        self.points = []
        self.speeds = []

    def __add__(self,p):
        self.speeds.append([random.random() * 2, random.random() * 2])
        self.points.append(p)
        return self

    def add(x, y):
        return list(map(lambda a, b: a + b, x, y))


    def alter_speed(self, alter):
 #       import pdb;pdb.set_trace()
        for i in self.speeds:
            i[0] = i[0] + alter
            i[1] = i[1] + alter



    def __repr__(self):
        return f"points {self.points} \nspeeds {self.speeds} \n"

    def __str__(self):
        return f"points {self.points} \nspeeds {self.speeds} \n"
    
    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""

        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.points[p_n][0]), int(self.points[p_n][1])),
                                 (int(self.points[p_n + 1][0]), int(self.points[p_n + 1][1])), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
#            import pdb; pdb.set_trace()
            self.points[p] = add(self.points[p] , self.speeds[p])
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])


class Knot(Polyline):

    def __init__(self, count):
        self.count = count
        self.points = []
        self.speeds = []
    
    def __add__(self,p):
        self.speeds.append([random.random() * 2, random.random() * 2])
#        import pdb; pdb.set_trace()
        self.points.append(p)
#        self.get_knot(self.count)
        return self


    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""

        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.points[p_n][0]), int(self.points[p_n][1])),
                                 (int(self.points[p_n + 1][0]), int(self.points[p_n + 1][1])), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)


    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        print('in k.get_knot')
        for i in range(-2, len(self.points) - 2):
            ptn = []
 #           import pdb; pdb.set_trace()
            ptn.append((Vec2d.fromPoint(self.points[i]) + Vec2d.fromPoint(self.points[i + 1])) * 0.5)
#            print(ptn)

            ptn.append(self.points[i + 1])
#            print(ptn)

            ptn.append((Vec2d.fromPoint(self.points[i + 1]) + Vec2d.fromPoint(self.points[i + 2])) * 0.5)
#            print(ptn)

            res.extend(self.get_points(ptn, count))
 #           print(f"res {res}")
        return res

   
   
    def get_points(self,base_points, count):
        alpha = 1 / count
        res = []

    #    import pdb; pdb.set_trace()
        for i in range(count):
            res.append(get_point(base_points, i * alpha))
        return res

    def get_point(self,points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
       #     import pdb; pdb.set_trace()
        
        return (points[deg] * alpha + get_point(points, alpha, deg - 1)) * (1 - alpha)



# =======================================================================================
# Функции отрисовки
# =======================================================================================
def draw_points(points, style="points", width=3, color=(255, 255, 255)):
    """функция отрисовки точек на экране"""
    if style == "line":
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(points[p_n][0]), int(points[p_n][1])),
                             (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

    elif style == "points":
        for p in points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p[0]), int(p[1])), width)


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

def set_points(points, speeds):
    """функция перерасчета координат опорных точек"""
    for p in range(len(points)):
        points[p] = add(points[p], speeds[p])
        if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
            speeds[p] = (- speeds[p][0], speeds[p][1])
        if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
            speeds[p] = (speeds[p][0], -speeds[p][1])


# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
   # import pdb; pdb.set_trace()
    
    return Vec2d.fromPoint(points[deg]) * alpha + Vec2d.fromPoint(get_point(points, alpha, deg - 1)) * (1 - alpha)

def get_points(base_points, count):
    alpha = 1 / count
    res = []

#    import pdb; pdb.set_trace()
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, count):
    if len(points) < 3:
        return []
    res = []
 #   print('In get_knote')
    for i in range(-2, len(points) - 2):
        ptn = []
    #    import pdb; pdb.set_trace()
        ptn.append((Vec2d.fromPoint(points[i]) + Vec2d.fromPoint(points[i + 1])) * 0.5)
#        print(ptn)
        ptn.append(points[i + 1])
 #       print(ptn)
        ptn.append((Vec2d.fromPoint(points[i + 1]) + Vec2d.fromPoint(points[i + 2])) * 0.5)
#        print(ptn)
 #       print(f"res {res}")
        res.extend(get_points(ptn, count))
    return res



# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":

    steps = 2
    points = []
    vecarr = []
    speeds = []

    k = Knot(steps)
    k = k + Vec2d(1,1)
    k = k + Vec2d(3,5)
    k = k + Vec2d(5,2)

    print(k)
    
    k.alter_speed(5)

    print(k)

