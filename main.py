WIDTH = 1000
HEIGHT = 600

game_state = "MENU"

music_on = True

class Player:
    def __init__(self):

        self.ninja = Actor("ninja_idle_1", center=(100, 500))

        self.velocity_y = 0
        self.gravity = 0.5
        self.ground_level = 480

        self.speed = 4

        self.idle_frames = ["ninja_idle_1", "ninja_idle_2"]
        self.run_frames = ["ninja_run_1", "ninja_run_2"]

        self.frame_index = 0
        self.animation_timer = 0
        self.state = "idle"

    def move(self):
        
        moving = False

        if keyboard.left:
            self.ninja.x -= self.speed
            moving = True

        if keyboard.right:
            self.ninja.x += self.speed
            moving = True

        if keyboard.space and self.ninja.y == self.ground_level:
            self.velocity_y = -10
            sounds.jump.play()
        
        if moving:
            self.state = "run"
        else:
            self.state = "idle"

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.ninja.y += self.velocity_y

        if self.ninja.y > self.ground_level:
            self.ninja.y = self.ground_level
            self.velocity_y = 0

    def animate(self):
        self.animation_timer += 1

        if self.animation_timer > 10:
            self.animation_timer = 0
            self.frame_index += 1

            if self.state == "idle":
                frames = self.idle_frames
            else:
                frames = self.run_frames

            if self.frame_index >= len(frames):
                self.frame_index = 0
            
            self.ninja.image = frames[self.frame_index]

    
    def draw(self):
        self.ninja.draw()

    def update(self):
        self.move()
        self.apply_gravity()
        self.animate()

class Slime:
    def __init__(self):

        self.slime = Actor("slime_idle_1", center=(600, 500))

        self.frames = ["slime_idle_1", "slime_idle_2"]

        self.frame_index = 0
        self.timer = 0

        self.speed = 2
        self.direction = 1

        self.left_boundary = 200
        self.right_boundary = 750

    def animate(self):

        self.timer += 1

        if self.timer > 15:

            self.timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

            self.slime.image = self.frames[self.frame_index]

    def update(self):
        self.slime.x += self.speed * self.direction

        if self.slime.x >= self.right_boundary:
            self.direction = -1

        if self.slime.x <= self.left_boundary:
            self.direction = 1

        self.animate()

    def draw(self):
        self.slime.draw()

class Bat:

    def __init__(self):
        self.bat = Actor("bat_idle_1", center=(750, 250))

        self.frames = ["bat_idle_1", "bat_idle_2"]

        self.frame_index = 0
        self.timer = 0

        self.speed = 2
        self.direction = 1

        self.top = 150
        self.bottom = 450

    def animate(self):
        
        self.timer += 1
        
        if self.timer > 12:

            self.timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            
            self.bat.image = self.frames[self.frame_index]

    def update(self):

        self.bat.y += self.speed * self.direction

        if self.bat.y >= self.bottom:
            self.direction = -1

        if self.bat.y <= self.top:
            self.direction = 1

        self.animate()

    def draw(self):
        self.bat.draw()

class Treasure:
    def __init__(self):
        self.treasure = Actor("treasure", center=(900, 500))
    
    def draw(self):
        self.treasure.draw()

player = Player()
slime = Slime()
bat = Bat()
treasure = Treasure()

def draw():

    screen.clear()

    if game_state == "MENU":

        screen.blit("background", (0,0))

        screen.draw.text("NINJA TREASURE", center=(500, 200), fontsize=70)
        screen.draw.text("CLICK TO START", center=(500, 350), fontsize=40)
        screen.draw.text("Press M to toggle music", center=(500, 450), fontsize=30)

    elif game_state == "PLAYING":

        screen.blit("background", (0, 0))

        player.draw()
        slime.draw()
        bat.draw()
        treasure.draw()
    
    elif game_state == "GAME_OVER":

        screen.blit("background", (0, 0))
    
        screen.draw.text("GAME OVER", center=(500, 250), fontsize=80)
        screen.draw.text("Press R to Restart", center=(500, 350), fontsize=40)

    elif game_state == "WIN":

        screen.blit("background", (0, 0))
        
        screen.draw.text("YOU WIN", center=(500, 250), fontsize=80)
        screen.draw.text("Press R to Restart", center=(500, 350), fontsize=40)

def update():
    global game_state
    if game_state == "PLAYING":
        player.update()
        slime.update()
        bat.update()

        if player.ninja.colliderect(slime.slime):
            sounds.hit.play()
            game_state = "GAME_OVER"

        if player.ninja.colliderect(treasure.treasure):
            sounds.coin.play()
            game_state = "WIN"

        if player.ninja.colliderect(bat.bat):
            sounds.hit.play()
            game_state = "GAME_OVER"

def on_mouse_down(pos):

    global game_state

    if game_state == "MENU":
        game_state = "PLAYING"

        if music_on:
            music.play("music")
            music.set_volume(0.4)

def on_key_down(key):

    global game_state
    global music_on

    if key == keys.R:

        if game_state == "GAME_OVER" or game_state == "WIN":
            reset_game()

    if key == keys.M:

        music_on = not music_on

        if music_on:
            music.play("music")
        else:
            music.stop()

def reset_game():

    global player, slime, bat, treasure, game_state

    player = Player()
    slime = Slime()
    bat = Bat()
    treasure = Treasure()
    game_state = "PLAYING"