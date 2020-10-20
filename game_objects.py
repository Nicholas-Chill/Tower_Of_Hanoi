import pygame
from settings import *
from game import Game
from peg import Peg
from disk import Disk

game = Game(fps)
screen = pygame.display.set_mode((screen_width, screen_height))

left_peg = Peg(left_peg_x, peg_y, peg_width, peg_height, brown)
middle_peg = Peg(middle_peg_x, peg_y, peg_width, peg_height, brown)
right_peg = Peg(right_peg_x, peg_y, peg_width, peg_height, brown)

left_peg_hitbox = pygame.rect.Rect(lt_peg_hb_x, peg_hitbox_y, lt_peg_hb_wid, screen_height)
middle_peg_hitbox = pygame.rect.Rect(mid_peg_hb_x, peg_hitbox_y, peg_hitbox_width, screen_height)
right_peg_hitbox = pygame.rect.Rect(rt_peg_hb_x, peg_hitbox_y, peg_hitbox_width, screen_height)

disk1 = Disk(disk1_x, disk1_y, disk1_width, disk_height, disk1_color)
disk2 = Disk(disk2_x, disk2_y, disk2_width, disk_height, disk2_color)
disk3 = Disk(disk3_x, disk3_y, disk3_width, disk_height, disk3_color)

disk1_dragbox = pygame.rect.Rect(disk1_x, disk1_y, disk1_width, disk_height)
disk2_dragbox = pygame.rect.Rect(disk2_x, disk2_y, disk2_width, disk_height)
disk3_dragbox = pygame.rect.Rect(disk3_x, disk3_y, disk3_width, disk_height)

disk1_right_edge = disk1_x + disk1_width
disk2_right_edge = disk2_x + disk2_width
disk3_right_edge = disk3_x + disk3_width
