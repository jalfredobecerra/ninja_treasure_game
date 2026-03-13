WIDTH = 1000
HEIGHT = 600

class Player:
    def __init__(self):
        self.ninja = Actor("ninja_idle_1", center=(100, 500))
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.ground_level = 500
    
    def draw(self):
        self.ninja.draw()

    def update(self):
        if keyboard.left:
            self.ninja.x -= 4

        if keyboard.right:
            self.ninja.x += 4
        
        if keyboard.space and self.ninja.y == self.ground_level:
            self.velocity_y = -10

        self.velocity_y += self.gravity

        self.ninja.y += self.velocity_y

        if self.ninja.y > self.ground_level:
            self.ninja.y = self.ground_level
            self.velocity_y = 0

player = Player()

def draw():
    screen.blit("background", (0,0))
    player.draw()

def update():
    player.update()

