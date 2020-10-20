import pygame
import game_objects as g_obj
import settings as sett
from peg import Peg
from disk import Disk
from disk import is_above_disk


class Game:
    def __init__(self, fps):
        self.fps = fps

    def run(self):
        pygame.init()
        running = True

        dragging_disk1 = False
        dragging_disk2 = False
        dragging_disk3 = False

        disk1_above_disk2 = False
        disk1_above_disk3 = False
        disk2_above_disk3 = False

        disk2_above_disk1 = False
        disk3_above_disk1 = False
        disk3_above_disk2 = False

        disk1_dragged = False
        disk2_dragged = False
        disk3_dragged = False

        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        d1_prev_x = g_obj.disk1.x
                        d1_prev_y = g_obj.disk1.y

                        d2_prev_x = g_obj.disk2.x
                        d2_prev_y = g_obj.disk2.y

                        d3_prev_x = g_obj.disk3.x
                        d3_prev_y = g_obj.disk3.y

                        if g_obj.disk1_dragbox.collidepoint(event.pos):
                            dragging_disk1 = True
                            mouse_x, mouse_y = event.pos
                            disk1_offset_x = g_obj.disk1_dragbox.x - mouse_x
                            disk1_offset_y = g_obj.disk1_dragbox.y - mouse_y

                        if not disk1_above_disk2:
                            if g_obj.disk2_dragbox.collidepoint(event.pos):
                                dragging_disk2 = True
                                mouse_x, mouse_y = event.pos
                                disk2_offset_x = g_obj.disk2_dragbox.x - mouse_x
                                disk2_offset_y = g_obj.disk2_dragbox.y - mouse_y

                        if not disk1_above_disk3 and not disk2_above_disk3:
                            if g_obj.disk3_dragbox.collidepoint(event.pos):
                                dragging_disk3 = True
                                mouse_x, mouse_y = event.pos
                                disk3_offset_x = g_obj.disk3_dragbox.x - mouse_x
                                disk3_offset_y = g_obj.disk3_dragbox.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if g_obj.disk1.y < g_obj.disk2.y and g_obj.disk1.x + g_obj.disk1.width >= g_obj.disk2.x:
                            if g_obj.disk1.x <= g_obj.disk2.x + g_obj.disk2.width / 2:
                                disk1_above_disk2 = True
                        else:
                            disk1_above_disk2 = False
                        if g_obj.disk1.y < g_obj.disk2.y and g_obj.disk1.x <= g_obj.disk2.x + g_obj.disk2.width:
                            if g_obj.disk1.x >= g_obj.disk2.x + g_obj.disk2.width / 2:
                                disk1_above_disk2 = True
                        else:
                            disk1_above_disk2 = False

                        if g_obj.disk1.y < g_obj.disk3.y and g_obj.disk1.x + g_obj.disk1.width >= g_obj.disk3.x:
                            if g_obj.disk1.x <= g_obj.disk3.x + g_obj.disk3.width / 2:
                                disk1_above_disk3 = True
                        else:
                            disk1_above_disk3 = False
                        if g_obj.disk1.y < g_obj.disk3.y and g_obj.disk1.x <= g_obj.disk3.x + g_obj.disk3.width:
                            if g_obj.disk1.x >= g_obj.disk3.x + g_obj.disk3.width / 2:
                                disk1_above_disk3 = True
                        else:
                            disk1_above_disk3 = False

                        if g_obj.disk2.y < g_obj.disk3.y and g_obj.disk2.x + g_obj.disk2.width >= g_obj.disk3.x:
                            if g_obj.disk2.x <= g_obj.disk3.x + g_obj.disk3.width / 2:
                                disk2_above_disk3 = True
                        else:
                            disk2_above_disk3 = False
                        if g_obj.disk2.y < g_obj.disk3.y and g_obj.disk2.x <= g_obj.disk3.x + g_obj.disk3.width:
                            if g_obj.disk2.x >= g_obj.disk3.x + g_obj.disk3.width / 2:
                                disk2_above_disk3 = True
                        else:
                            disk2_above_disk3 = False

                        if g_obj.disk2.y < g_obj.disk1.y and g_obj.disk2.x + g_obj.disk2.width >= g_obj.disk1.x:
                            if g_obj.disk2.x <= g_obj.disk1.x + g_obj.disk1.width / 2:
                                disk2_above_disk1 = True
                        else:
                            disk2_above_disk1 = False
                        if g_obj.disk2.y < g_obj.disk1.y and g_obj.disk2.x <= g_obj.disk1.x + g_obj.disk1.width:
                            if g_obj.disk2.x >= g_obj.disk1.x + g_obj.disk1.width / 2:
                                disk2_above_disk1 = True
                        else:
                            disk2_above_disk1 = False

                        if g_obj.disk3.y < g_obj.disk1.y and g_obj.disk3.x <= g_obj.disk1.x:
                            if g_obj.disk3.x >= g_obj.disk1.x + g_obj.disk1.width / 2:
                                disk3_above_disk1 = True
                        else:
                            disk3_above_disk1 = False
                        if g_obj.disk3.y < g_obj.disk1.y and g_obj.disk3.x + g_obj.disk3.width >= g_obj.disk1.x:
                            if g_obj.disk3.x <= g_obj.disk1.x + g_obj.disk1.width / 2:
                                disk3_above_disk1 = True
                        else:
                            disk3_above_disk1 = False

                        if g_obj.disk3.y < g_obj.disk2.y and g_obj.disk3.x <= g_obj.disk2.x:
                            if g_obj.disk3.x >= g_obj.disk2.x + g_obj.disk2.width / 2:
                                disk3_above_disk2 = True
                        else:
                            disk3_above_disk2 = False
                        if g_obj.disk3.y < g_obj.disk2.y and g_obj.disk3.x + g_obj.disk3.width >= g_obj.disk2.x:
                            if g_obj.disk3.x <= g_obj.disk2.x + g_obj.disk2.width / 2:
                                disk3_above_disk2 = True
                        else:
                            disk3_above_disk2 = False

                        dragging_disk1 = False
                        dragging_disk2 = False
                        dragging_disk3 = False
                        if g_obj.disk1.x < d1_prev_x or g_obj.disk1.x > d1_prev_x or g_obj.disk1.y < d1_prev_y or \
                                g_obj.disk1.y > d1_prev_y:
                            disk1_dragged = True
                        else:
                            disk1_dragged = False

                        if disk1_dragged:
                            if g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                                if g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                    and g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.disk1_x, sett.disk1_x
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.disk1_y, sett.disk1_y
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
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.disk1_y, sett.disk1_y
                                elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                                           sett.screen_height - sett.disk_height * 2
                                elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox) \
                                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                                           sett.screen_height - sett.disk_height * 2
                                elif not g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                    and not g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.middle_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height, \
                                                                           sett.screen_height - sett.disk_height

                            elif g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox):
                                if g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                        and g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.disk1_y, sett.disk1_y
                                elif g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                        and not g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                                           sett.screen_height - sett.disk_height * 2
                                elif g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox) \
                                        and not g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height * 2, \
                                                                           sett.screen_height - sett.disk_height * 2
                                elif not g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox) \
                                        and not g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                    g_obj.disk1.x, g_obj.disk1_dragbox.x = sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2, \
                                                                           sett.right_peg_x - sett.disk1_width / 2 \
                                                                           + sett.peg_width / 2
                                    g_obj.disk1.y, g_obj.disk1_dragbox.y = sett.screen_height - sett.disk_height, \
                                                                           sett.screen_height - sett.disk_height

                        if g_obj.disk2.x < d2_prev_x or g_obj.disk2.x > d2_prev_x or g_obj.disk2.y < d2_prev_y or \
                                g_obj.disk2.y > d2_prev_y:
                            disk2_dragged = True
                        else:
                            disk2_dragged = False

                        if disk2_dragged:
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

                                if disk2_above_disk1:
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

                                if disk2_above_disk1:
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

                                if disk2_above_disk1:
                                    g_obj.disk2.x, g_obj.disk2_dragbox.x = d2_prev_x, d2_prev_x
                                    g_obj.disk2.y, g_obj.disk2_dragbox.y = d2_prev_y, d2_prev_y

                        if g_obj.disk3.x < d3_prev_x or g_obj.disk3.x > d3_prev_x or g_obj.disk3.y < d3_prev_y or \
                                g_obj.disk3.y > d3_prev_y:
                            disk3_dragged = True
                        else:
                            disk3_dragged = False

                        if disk3_dragged:
                            if disk3_above_disk1 or disk3_above_disk2:
                                g_obj.disk3.x, g_obj.disk3_dragbox.x = d3_prev_x, d3_prev_x
                                g_obj.disk3.y, g_obj.disk3_dragbox.y = d3_prev_y, d3_prev_y

                            if g_obj.left_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                if not g_obj.left_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                                    g_obj.left_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                                    g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.disk3_x, sett.disk3_x
                                    g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                                           sett.screen_height - sett.disk_height

                            elif g_obj.middle_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                if not g_obj.middle_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                                        g_obj.middle_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                                    g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.middle_peg_x - sett.disk3_width / 2 \
                                                                            + sett.peg_width / 2, \
                                                                            sett.middle_peg_x - sett.disk3_width / 2 \
                                                                            + sett.peg_width / 2
                                    g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                                            sett.screen_height - sett.disk_height

                            elif g_obj.right_peg_hitbox.colliderect(g_obj.disk3_dragbox):
                                if not g_obj.right_peg_hitbox.colliderect(g_obj.disk1_dragbox) and not \
                                        g_obj.right_peg_hitbox.colliderect(g_obj.disk2_dragbox):
                                    g_obj.disk3.x, g_obj.disk3_dragbox.x = sett.right_peg_x - sett.disk3_width / 2 \
                                                                            + sett.peg_width / 2, \
                                                                            sett.right_peg_x - sett.disk3_width / 2 \
                                                                            + sett.peg_width / 2
                                    g_obj.disk3.y, g_obj.disk3_dragbox.y = sett.screen_height - sett.disk_height, \
                                                                            sett.screen_height - sett.disk_height

                elif event.type == pygame.MOUSEMOTION:
                    if dragging_disk1:
                        mouse_x, mouse_y = event.pos
                        g_obj.disk1_dragbox.x = mouse_x + disk1_offset_x
                        g_obj.disk1_dragbox.y = mouse_y + disk1_offset_y
                        g_obj.disk1.x = g_obj.disk1_dragbox.x
                        g_obj.disk1.y = g_obj.disk1_dragbox.y

                    elif dragging_disk2:
                        mouse_x, mouse_y = event.pos
                        g_obj.disk2_dragbox.x = mouse_x + disk2_offset_x
                        g_obj.disk2_dragbox.y = mouse_y + disk2_offset_y
                        g_obj.disk2.x = g_obj.disk2_dragbox.x
                        g_obj.disk2.y = g_obj.disk2_dragbox.y

                    elif dragging_disk3:
                        mouse_x, mouse_y = event.pos
                        g_obj.disk3_dragbox.x = mouse_x + disk3_offset_x
                        g_obj.disk3_dragbox.y = mouse_y + disk3_offset_y
                        g_obj.disk3.x = g_obj.disk3_dragbox.x
                        g_obj.disk3.y = g_obj.disk3_dragbox.y

            g_obj.screen.fill(sett.white)

            Peg.draw_peg(g_obj.left_peg)
            Peg.draw_peg(g_obj.middle_peg)
            Peg.draw_peg(g_obj.right_peg)

            Disk.draw_disk(g_obj.disk1)
            Disk.draw_disk(g_obj.disk2)
            Disk.draw_disk(g_obj.disk3)

            pygame.display.update()
            clock.tick(self.fps)
