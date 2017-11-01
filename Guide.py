from __init__ import Hexamaze, Player1
import random

class Guide:
    def __init__(self, end):
        self.pos = Player1.position
        self.end = end
        self.distance = 0
        self.maze_moves = Hexamaze.maze_moves

    def dis_init(self):
        self.pos = Player1.position
        my_x = self.pos[0]
        my_y = self.pos[1]
        its_x = self.end[0]
        its_y = self.end[1]
        rotations_x = 0
        rotations_y = 0
        if my_x > its_x:
            while True:
                rotations_x += 1
                its_x += 1
                if my_x == its_x:
                    break
        elif my_x < its_x:
            while True:
                rotations_x += 1
                my_x += 1
                if my_x == its_x:
                    break
        if my_y > its_y:
            while True:
                rotations_y += 1
                its_y += 1
                if my_y == its_y:
                    break
        elif my_y < its_y:
            while True:
                rotations_y += 1
                my_y += 1
                if my_y == its_y:
                    break

        self.distance = rotations_x + rotations_y

    def close_by(self):
        self.dis_init()
        so_list = ['so', 'so', 'very', 'extremely']
        if self.distance == 1:
            pass
        elif self.distance == 2 or self.distance == 3:
            so_list.remove(so_list[3])
        elif self.distance == 4 or self.distance == 5:
            so_list.remove(so_list[3])
            so_list.remove(so_list[2])
        elif self.distance == 6:
            so_list.remove(so_list[3])
            so_list.remove(so_list[2])
            so_list.remove(so_list[1])
        elif self.distance > 6:
            so_list.remove(so_list[3])
            so_list.remove(so_list[2])
            so_list.remove(so_list[1])
            so_list.remove(so_list[0])

        so = ' '.join(so_list)
        return "You are " + str(so) + " close! Only " + str(self.distance) + " moves away!"

    def hear(self):
        self.dis_init()
        if self.pos[0] < self.end[0]:
            xish = 'right'
        elif self.pos[0] > self.end[0]:
            xish = 'left'
        elif self.pos[0] == self.end[0]:
            xish = 'what i must be dreaming. I am leading you on the right path anyways...'
        else:
            xish = 'never mind you heard nothing'
        return "You hear a faint but recognizable scream to the " + xish

    def far_away(self):
        self.dis_init()
        return "You are far away! You are " + str(self.distance) + " moves away from your target!"

    def this_direction(self):
        self.dis_init()
        if self.pos[0] < self.end[0]:
            xish = 'right'
        elif self.pos[0] > self.end[0]:
            xish = 'left'
        elif self.pos[0] == self.end[0]:
            xish = 'nowhere horizontally'
        else:
            xish = 'give me all your money'
        if self.pos[1] < self.end[1]:
            yish = 'forward'
        elif self.pos[1] > self.end[1]:
            yish = 'backward'
        elif self.pos[1] == self.end[1]:
            yish = 'nowhere vertically'
        else:
            yish = 'die in a hole'
        return "You're doing it wrong! You need to go " + xish + " and " + yish

    def choose(self):
        self.dis_init()
        choices = [self.this_direction(), self.hear()]
        if self.distance <= 5:
            choices.append(self.close_by())
        if self.distance > 6:
            choices.append(self.far_away())
        choice = random.choice(choices)
        return choice
