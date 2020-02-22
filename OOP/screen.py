#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

 

SCREEN_DIM = (800, 600)


class Vec2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def fromPoint(cls, p):
        return cls(p[0], p[1])

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
        return Vec2d(self.x * k, self.y * k)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

    def int_pair(self):
        return (self.x, self.y)

    def __str__(self):
        return str(self.x) + str(self.y)

    def __repr__(self):
        return str(self.x) + " " + str(self.y)


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



class Polyline():
    def __init__(self):
        self.points = []
        self.speeds = []

    def __add__(self, p):
        self.speeds.append([random.random() * 2, random.random() * 2])
        self.points.append(p)
        return self

    def __repr__(self):
        return f"points {self.points} \n"

    def __str__(self):
        return f"points {self.points} \n"


    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""

        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.points[p_n][0]),
                                  int(self.points[p_n][1])),
                                 (int(self.points[p_n + 1][0]),
                                  int(self.points[p_n + 1][1])), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    def set_points(self, alter_speed=0):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            if alter_speed > 0:
                self.points[p] = Vec2d.fromPoint(self.points[p]) +\
                Vec2d.fromPoint(self.speeds[p])*alter_speed
            else:

                self.points[p] = Vec2d.fromPoint(self.points[p]) +\
                Vec2d.fromPoint(self.speeds[p])
          
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])


class Knot(Polyline):

    def __init__(self, count):
        self.count = count
        self.points = []
        self.speeds = []

    def __add__(self, p):
        self.speeds.append([random.random() * 2, random.random() * 2])
        self.points.append(p)
        return self

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""

        res = self.get_knot(self.count)

        if style == "line":
            for p_n in range(-1, len(res) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(res[p_n][0]), int(res[p_n][1])),
                                 (int(res[p_n + 1][0]), int(res[p_n + 1][1])),
                                 width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []

        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn, count))
        return res

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []

        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, points, alpha, deg=None):

        if deg is None:
            deg = len(points) - 1

        if deg == 0:
            return points[0]

        return Vec2d.fromPoint(points[deg]) * alpha + Vec2d.fromPoint(
            self.get_point(points, alpha, deg - 1)) * (1 - alpha)


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
    data.append(["i", "increase speed"])
    data.append(["d", "decrease speed"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))



if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    k = Knot(steps)
    x=0
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_i:
                    x+=1
                if event.key == pygame.K_d:
                    x-=1
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                k = k + Vec2d.fromPoint(event.pos)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        k.draw_points()
        k.draw_points("line", 3, color)


        if not pause:
            k.set_points(x)
        if show_help:
            draw_help()
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
