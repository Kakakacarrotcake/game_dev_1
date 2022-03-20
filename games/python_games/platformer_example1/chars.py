from asyncio.windows_events import NULL
from turtle import position


class character():

    health_points = NULL
    mana_points = NULL
    position_x = 0
    position_y = 0

    def __init__(self,pos_x,pos_y):
        self.position_x = pos_x
        self.position_y = pos_y

class main_char(character):
    special_left = False
    special_right = False
    special_up = False
    special_down = False

    def __init__(self):
        super()