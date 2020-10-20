white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
brown = [118, 83, 42]

screen_width = 1000
screen_height = 600

fps = 60

peg_width = 10
peg_height = 400

peg_y = 200

left_peg_x = 200
middle_peg_x = 500
right_peg_x = 800

peg_hitbox_y = 0

lt_peg_hb_x = 0
mid_peg_hb_x = 333
rt_peg_hb_x = 667

peg_hitbox_width = 334

lt_peg_hb_wid = 333

number_of_disks = 3

disk_height = 30

disk1_width = 50
disk2_width = 100
disk3_width = 150

disk1_x = left_peg_x - disk1_width / 2 + peg_width / 2
disk1_y = screen_height - disk_height - disk_height * (number_of_disks - 1)

disk2_x = left_peg_x - disk2_width / 2 + peg_width / 2
disk2_y = screen_height - disk_height - disk_height * (number_of_disks - 2)

disk3_x = left_peg_x - disk3_width / 2 + peg_width / 2
disk3_y = screen_height - disk_height

disk1_color = red
disk2_color = green
disk3_color = blue
