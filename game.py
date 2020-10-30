import pygame
import game_objects as g_obj
import settings as sett
from peg import Peg
from disk import Disk


class Game:
    def __init__(self, fps):
        self.fps = fps

    def run(self):
        pygame.init()
        running = True
        clock = pygame.time.Clock()
        dragging_disk1 = False
        dragging_disk2 = False
        dragging_disk3 = False

        disk1_dragged = False
        disk2_dragged = False
        disk3_dragged = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        disk1_above_disk2 = Disk.disk1_above_disk2(g_obj.disk1)
                        disk1_above_disk3 = Disk.disk1_above_disk3(g_obj.disk1)
                        disk2_above_disk3 = Disk.disk2_above_disk3(g_obj.disk2)

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

                        dragging_disk1 = False
                        dragging_disk2 = False
                        dragging_disk3 = False

                        if g_obj.disk1.x < d1_prev_x or g_obj.disk1.x > d1_prev_x or g_obj.disk1.y < d1_prev_y \
                                or g_obj.disk1.y > d1_prev_y:
                            disk1_dragged = True

                        if disk1_dragged:
                            Peg.disk1_collide_peg()

                        if g_obj.disk2.x < d2_prev_x or g_obj.disk2.x > d2_prev_x or g_obj.disk2.y < d2_prev_y or \
                                g_obj.disk2.y > d2_prev_y:
                            disk2_dragged = True

                        if disk2_dragged:
                            Peg.disk2_collide_peg(d2_prev_x, d2_prev_y)

                        if g_obj.disk3.x < d3_prev_x or g_obj.disk3.x > d3_prev_x or g_obj.disk3.y < d3_prev_y or \
                                g_obj.disk3.y > d3_prev_y:
                            disk3_dragged = True

                        if disk3_dragged:
                            Peg.disk3_collide_peg(d3_prev_x, d3_prev_y)

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
