import pygame
import game_objects as g_obj


class Disk:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw_disk(self):
        pygame.draw.rect(g_obj.screen, self.color, (self.x, self.y, self.width, self.height))


def is_above_disk():
    if g_obj.disk2.y < g_obj.disk1.y and g_obj.disk2.x + g_obj.disk2.width >= g_obj.disk1.x:
        if g_obj.disk2.x <= g_obj.disk1.x + g_obj.disk1.width / 2:
            return True
    else:
        return False
    if g_obj.disk2.y < g_obj.disk1.y and g_obj.disk2.x <= g_obj.disk1.x + g_obj.disk1.width:
        if g_obj.disk2.x >= g_obj.disk1.x + g_obj.disk1.width / 2:
            return True
    else:
        return False

    if g_obj.disk3.y < g_obj.disk1.y and g_obj.disk3.x <= g_obj.disk1.x:
        if g_obj.disk3.x >= g_obj.disk1.x + g_obj.disk1.width / 2:
            return True
    else:
        return False
    if g_obj.disk3.y < g_obj.disk1.y and g_obj.disk3.x + g_obj.disk3.width >= g_obj.disk1.x:
        if g_obj.disk3.x <= g_obj.disk1.x + g_obj.disk1.width / 2:
            return True
    else:
        return False

    if g_obj.disk3.y < g_obj.disk2.y and g_obj.disk3.x <= g_obj.disk2.x:
        if g_obj.disk3.x >= g_obj.disk2.x + g_obj.disk2.width / 2:
            return True
    else:
        return False
    if g_obj.disk3.y < g_obj.disk2.y and g_obj.disk3.x + g_obj.disk3.width >= g_obj.disk2.x:
        if g_obj.disk3.x <= g_obj.disk2.x + g_obj.disk2.width / 2:
            return True
    else:
        return False
