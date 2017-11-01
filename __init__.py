import random as rd

class Maze:
    def __init__(self):
        self.left = 'left'
        self.right = 'right'
        self.forward = 'forward'
        self.backward = 'backward'
        self.moves = [self.left, self.right, self.forward, self.backward]
        self.maze_moves = {}
        self.move_time = 0

    def make_maze(self):
        self.maze_moves = {}
        x = rd.choice(range(10, 20))
        y = 0
        for i in range(1, x, 1):
            re = rd.choice(self.moves)
            self.maze_moves[y] = re
            y += 1


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def make_end_goal(self):
        moves = Hexamaze.maze_moves
        x = 0
        for i in moves:
            if moves[int(x)] == 'left':
                self.x -= 1
            elif moves[int(x)] == 'right':
                self.x += 1
            elif moves[int(x)] == 'forward':
                self.y += 1
            elif moves[int(x)] == 'backward':
                self.y -= 1
            x += 1
        return [self.x, self.y]

    def regulate(self):
        check = [self.x, self.y]
        for i in check:
            if i > 20:
                i -= 2
        for i in Player1.position:
            if i > 20:
                i -= 1
                print("Woah there buddy! You can't go farther than that!")


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = [0, 0]

    def move_player(self, move):
        if move == 'left':
            self.x -= 1
        elif move == 'right':
            self.x += 1
        elif move == 'forward':
            self.y += 1
        elif move == 'backward':
            self.y -= 1
        elif move is None:
            pass
        playerPos = [self.x, self.y]
        self.position = playerPos
        return playerPos


Hexamaze = Maze()
Player1 = Player()
Pos = Position()