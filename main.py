WIDTH = 1000
HEIGHT = 600
game_over = False
game_result = None

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

class Slime:
    def __init__(self):
        self.slime = Actor("slime_idle_1", center=(600, 500))
        self.speed = 2
        self.direction = 1
        self.left_boundary = 500
        self.right_boundary = 750

    def draw(self):
        self.slime.draw()

    def update(self):
        self.slime.x = self.slime.x + (self.speed * self.direction)

        if self.slime.x >= self.right_boundary:
            self.direction = -1

        if self.slime.x <= self.left_boundary:
            self.direction = 1

class Treasure:
    def __init__(self):
        self.treasure = Actor("treasure", center=(900, 500))
    
    def draw(self):
        self.treasure.draw()

player = Player()
slime = Slime()
treasure = Treasure()

def draw():
    screen.blit("background", (0,0))
    player.draw()
    slime.draw()
    treasure.draw()

    if game_over:
        if game_result == "lose":
            screen.draw.text("GAME OVER", center=(500, 300))

        if game_result == "win":
            screen.draw.text("YOU WIN", center=(500, 300))

def update():
    global game_over, game_result
    if game_over == False:
        player.update()
        slime.update()

        if player.ninja.colliderect(slime.slime):
            print("Game Over")
            game_over = True
            game_result = "lose"

        if player.ninja.colliderect(treasure.treasure):
            print("You Win!")
            game_over = True
            game_result = "win"