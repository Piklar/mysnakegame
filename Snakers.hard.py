from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from random import randint

Builder.load_string("""
#:import random random

<Snakebody>:
    canvas:
        Color:
            rgb: [random.random() for i in range(3)]        
        Rectangle:
            size: self.size
            pos: self.pos
            
<Food>:
    canvas:
        Color:
            rgb: [random.random() for i in range(3)]
        Ellipse:
            size: self.size
            pos: self.pos
        
<Obstacle>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle2>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle3>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle4>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle5>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle6>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle7>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle8>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle9>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            
<Obstacle10>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos                                                                                                

<SnakeGame>:
    Food:
        id: food
        
    Obstacle:
        id: obstacle
        
    Obstacle2:
        id: obstacle2
        
    Obstacle3:
        id: obstacle3
        
    Obstacle4:
        id: obstacle4
        
    Obstacle5:
        id: obstacle5

    Obstacle6:
        id: obstacle6
        
    Obstacle7:
        id: obstacle7
        
    Obstacle8:
        id: obstacle8
        
    Obstacle9:
        id: obstacle9
        
    Obstacle10:
        id: obstacle10
                    
""")

SIZE = 30
SPEED = 9


class SnakeBody(Widget):
    size = (SIZE, SIZE)


class Food(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle2(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle3(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle4(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle5(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle6(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle7(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle8(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle9(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class Obstacle10(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class SnakeGame(Widget):
    direction = (SIZE, 0)
    snake_body = []
    snake_trail = [(0, 0)]

    def add_body(self):
        # Pang dagdag body parts nung snake
        body = SnakeBody()
        if len(self.snake_body) == 0:
            body.pos = (0, 0)
        else:
            body.pos = self.snake_trail[-2]
        self.add_widget(body)
        self.snake_body.append(body)

    def new_game(self):
        # Start o Restart function
        # Kinalbo natin lahat nung variables para reset
        for body_parts in self.snake_body:
            self.remove_widget(body_parts)

        self.snake_trail = []
        self.snake_body = []
        self.direction = (SIZE, 0)
        self.ids.food.move()
        self.add_body()
        self.ids.obstacle.move()
        self.ids.obstacle2.move()
        self.ids.obstacle3.move()
        self.ids.obstacle4.move()
        self.ids.obstacle5.move()
        self.ids.obstacle6.move()
        self.ids.obstacle7.move()
        self.ids.obstacle8.move()
        self.ids.obstacle9.move()
        self.ids.obstacle10.move()

    def on_touch_up(self, touch):
        # Touch Controls
        mx = touch.x - touch.opos[0]
        my = touch.y - touch.opos[1]

        if abs(mx) > abs(my) and mx > 0 and self.direction != [-SIZE, 0]:
            self.direction = [SIZE, 0]

        elif abs(mx) > abs(my) and mx < 0 and self.direction != [SIZE, 0]:
            self.direction = [-SIZE, 0]

        elif abs(mx) < abs(my) and my > 0 and self.direction != [0, -SIZE]:
            self.direction = [0, SIZE]

        elif abs(mx) < abs(my) and my < 0 and self.direction != [0, SIZE]:
            self.direction = [0, -SIZE]

    def refresh(self, aa):
        # Update nung laro kada 1/SPEED sec
        head = self.snake_body[0]
        head.pos[0] += self.direction[0]
        head.pos[1] += self.direction[1]
        # pang record kung nasaan na yung position nung ulo
        new_pos = (head.pos[0], head.pos[1])
        self.snake_trail.append(new_pos)
        while len(self.snake_trail) > len(self.snake_body) + 1:
            del self.snake_trail[0]
        # pangalaw sa katawan
        for i, body in enumerate(self.snake_body):
            if body is head:
                continue
            body.pos = self.snake_trail[i]
        # para tatlo yung katawan agad
        if len(self.snake_trail) > 1 and len(self.snake_body) < 3:
            self.add_body()
        # Pag na detect na yung pagkain
        if head.pos == self.ids.food.pos:
            self.ids.food.move()
            self.add_body()
            self.ids.obstacle.move()
            self.ids.obstacle2.move()
            self.ids.obstacle3.move()
            self.ids.obstacle4.move()
            self.ids.obstacle5.move()
            self.ids.obstacle6.move()
            self.ids.obstacle7.move()
            self.ids.obstacle8.move()
            self.ids.obstacle9.move()
            self.ids.obstacle10.move()
        # Pag nauntog yung head sa body
        for body in self.snake_body:
            if body is not head and head.pos == body.pos:
                self.new_game()
        # Kung na untog sa pader
        if not (0 <= head.pos[0] < Window.width) or \
                not (0 <= head.pos[1] < Window.height):
            self.new_game()

        if head.pos == self.ids.obstacle.pos:
            self.new_game()

        if head.pos == self.ids.obstacle.pos:
            self.new_game()

        if head.pos == self.ids.obstacle2.pos:
            self.new_game()

        if head.pos == self.ids.obstacle3.pos:
            self.new_game()

        if head.pos == self.ids.obstacle4.pos:
            self.new_game()

        if head.pos == self.ids.obstacle5.pos:
            self.new_game()

        if head.pos == self.ids.obstacle6.pos:
            self.new_game()

        if head.pos == self.ids.obstacle7.pos:
            self.new_game()

        if head.pos == self.ids.obstacle8.pos:
            self.new_game()

        if head.pos == self.ids.obstacle9.pos:
            self.new_game()

        if head.pos == self.ids.obstacle10.pos:
            self.new_game()


class MainApp(App):
    def on_start(self):
        self.root.new_game()
        Clock.schedule_interval(self.root.refresh, 1 / SPEED)

    def build(self):
        return SnakeGame()


if __name__ == "__main__":
    MainApp().run()
