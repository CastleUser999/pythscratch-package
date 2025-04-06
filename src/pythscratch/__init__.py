# SCRIPT-START
import random as r
import time as t
class Sprite:
  class Motion:
    # MOTION-START
    x = 0
    y = 0
    direction = 0
    def move_steps(steps: int) -> None:
      global x
      x += int(steps)
    def turn_right(degrees: int) -> None:
      global direction
      direction += int(degrees)
    def turn_left(degrees: int) -> None:
      global direction
      direction -= int(degrees)
    def random_pos() -> None:
      global x
      global y
      x = r.randint(0, 272)
      y = r.randint(0, 215)
    def goto_pos(x_pos: int, y_pos: int) -> None:
      global x
      global y
      x = x_pos
      y = y_pos
    def glide_random_pos(seconds: int) -> None:
      global x
      global y
      for sec in range(seconds):
        t.sleep(1)
        x = r.randint(0, 272)
        y = r.randnt(0, 215)
    def glide_pos(seconds: int, x_pos: int, y_pos: int) -> None:
      global x
      global y
      for sec in range(seconds):
        t.sleep(1)
        x = x_pos
        y = y_pos
    def point_direction(degree: int) -> None:
      global direction
      direction = degree
    def point_random() -> None:
      global direction
      direction = r.randint(0, 360)
    def change_x(x_pos: int) -> None:
      global x
      x += x_pos
    def set_x(x_pos: int) -> None:
      global x
      x = x_pos
    def change_y(y_pos: int) -> None:
      global y
      y += y_pos
    def set_y(y_pos: int) -> None:
      global y
      y = y_pos
    def reporter_x() -> int:
      global x
      return x
    def reporter_y() -> int:
      global y
      return y
  # MOTION-END
  

