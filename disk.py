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

    def disk1_above_disk2(self):
        if self.y < g_obj.disk2.y and self.x + self.width >= g_obj.disk2.x:
            if self.x <= g_obj.disk2_x + g_obj.disk2_width / 2:
                return True
        if self.y < g_obj.disk2.y and self.x <= g_obj.disk2_x + g_obj.disk2_width:
            if self.x >= g_obj.disk2_x + g_obj.disk2_width / 2:
                return True

        return False

    def disk1_above_disk3(self):
        if self.y < g_obj.disk3.y and self.x + self.width >= g_obj.disk3.x:
            if self.x <= g_obj.disk3_x + g_obj.disk3_width / 2:
                return True
        if self.y < g_obj.disk3.y and self.x <= g_obj.disk3_x + g_obj.disk3_width:
            if self.x >= g_obj.disk3_x + g_obj.disk3_width / 2:
                return True

        return False

    def disk2_above_disk3(self):
        if self.y < g_obj.disk3.y and self.x + self.width >= g_obj.disk3.x:
            if g_obj.disk2.x <= g_obj.disk3_x + g_obj.disk3_width / 2:
                return True
        if self.y < g_obj.disk3.y and self.x <= g_obj.disk3_x + g_obj.disk3_width:
            if self.x >= g_obj.disk3_x + g_obj.disk3_width / 2:
                return True

        return False
