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
            rgb: 1, 0, 0
        Ellipse:
            size: self.size
            pos: self.pos

<SnakeGame>:
    Food:
        id:food

""")

SIZE = 30
SPEED = 7


class SnakeBody(Widget):
    size = (SIZE, SIZE)


class Food(Widget):
    size = (SIZE, SIZE)

    def move(self):
        self.x = (SIZE * randint(1, Window.width // SIZE)) - SIZE
        self.y = (SIZE * randint(1, Window.height // SIZE)) - SIZE


class SnakeGame(Widget):
    direction = (SIZE, 0)
    snake_body = []
    snake_trail = [(0, 0)]

    def add_body(self):
        body = SnakeBody()
        if len(self.snake_body) == 0:
            body.pos = (0, 0)
        else:
            body.pos = self.snake_trail[-2]
        self.add_widget(body)
        self.snake_body.append(body)

    def new_game(self):
        for body_parts in self.snake_body:
            self.remove_widget(body_parts)

        self.snake_trail = []
        self.snake_body = []
        self.direction = (SIZE, 0)
        self.ids.food.move()
        self.add_body()

    def on_touch_up(self, touch):
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
        head = self.snake_body[0]
        head.pos[0] += self.direction[0]
        head.pos[1] += self.direction[1]

        new_pos = (head.pos[0], head.pos[1])
        self.snake_trail.append(new_pos)
        while len(self.snake_trail) > len(self.snake_body) + 1:
            del self.snake_trail[0]

        for i, body in enumerate(self.snake_body):
            if body is head:
                continue
            body.pos = self.snake_trail[i]

        if len(self.snake_trail) > 1 and len(self.snake_body) < 4:
            self.add_body()

        if head.pos == self.ids.food.pos:
            self.ids.food.move()
            self.add_body()

        for body in self.snake_body:
            if body is not head and head.pos == body.pos:
                self.new_game()

        if not (0 <= head.pos[0] < Window.width) or \
                not (0 <= head.pos[1] < Window.height):
            self.new_game()


class MainApp(App):
    def on_start(self):
        self.root.new_game()
        Clock.schedule_interval(self.root.refresh, 1 / SPEED)

    def build(self):
        return SnakeGame()


if __name__ == "__main__":
    MainApp().run()
