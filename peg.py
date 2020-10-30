import pygame
import game_objects as g_obj
import settings as sett


class Peg:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw_peg(self):
        pygame.draw.rect(g_obj.screen, self.color, (self.x, self.y, self.width, self.height))

    @staticmethod
    def disk1_collide_peg():
        if g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox):
            if g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.disk1_x, sett.disk1_x
                g_obj.disk1.y, g_obj.disk1_dragbox.x = sett.disk1_y, sett.disk1_y
            elif g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.disk1_x, sett.disk1_x
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            elif g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox) \
                    and not g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.disk1_x, sett.disk1_x
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            elif not g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.disk1_x, sett.disk1_x
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

        if g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox):
            if g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.disk1_y, sett.disk1_y
            elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox) \
                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            elif not g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

        elif g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox):
            if g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.disk1_y, sett.disk1_y
            elif g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                        sett.screen_height - sett.disk_height * 2
            elif g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox) \
                    and not g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.y = sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                        sett.screen_height - sett.disk_height * 2
            elif not g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                    and not g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk1_width / 2 + sett.peg_width / 2
                g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height, sett.screen_height - sett.disk_height

        return g_obj.disk1_x, g_obj.disk1_y, g_obj.disk1_dragbox.x, g_obj.disk1_dragbox.y

    @staticmethod
    def disk2_collide_peg(d2_prev_x, d2_prev_y):
        if g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox):
            if g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox) and not \
                    g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.disk2_x, sett.disk2_x
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            elif not g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.disk2_x, sett.disk2_x
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = d2_prev_x, d2_prev_x
                g_obj.disk2.y, g_obj.disk2_dragbox.y = d2_prev_y, d2_prev_y

        if g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox):
            if g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox) and not \
                    g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.middle_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            if not g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.middle_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = d2_prev_x, d2_prev_x
                g_obj.disk2.y, g_obj.disk2_dragbox.y = d2_prev_y, d2_prev_y

        if g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox):
            if g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox) and not \
                    g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.right_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                       sett.screen_height - sett.disk_height * 2
            if not g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = sett.right_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk2_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk2.y, g_obj.disk2_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                g_obj.disk2.x, g_obj.disk2_dragbox.x = d2_prev_x, d2_prev_x
                g_obj.disk2.y, g_obj.disk2_dragbox.y = d2_prev_y, d2_prev_y

    @staticmethod
    def disk3_collide_peg(d3_prev_x, d3_prev_y):
        if g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
            if not g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.disk3_x, sett.disk3_x
                g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox) or g_obj.left_peg_hitbox.colliderect(
                    g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = d3_prev_x, d3_prev_x
                g_obj.disk3.y, g_obj.disk3_dragbox.y = d3_prev_y, d3_prev_y

        elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
            if not g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.middle_peg_x - sett.disk3_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.middle_peg_x - sett.disk3_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox) or g_obj.middle_peg_hitbox.colliderect(
                    g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = d3_prev_x, d3_prev_x
                g_obj.disk3.y, g_obj.disk3_dragbox.y = d3_prev_y, d3_prev_y

        elif g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
            if not g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                    g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.right_peg_x - sett.disk3_width / 2 \
                                                       + sett.peg_width / 2, \
                                                       sett.right_peg_x - sett.disk3_width / 2 \
                                                       + sett.peg_width / 2
                g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                       sett.screen_height - sett.disk_height

            if g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox) or g_obj.right_peg_hitbox.colliderect(
                    g_obj.disk2_dragbox):
                g_obj.disk3.x, g_obj.disk3_dragbox.x = d3_prev_x, d3_prev_x
                g_obj.disk3.y, g_obj.disk3_dragbox.y = d3_prev_y, d3_prev_y
