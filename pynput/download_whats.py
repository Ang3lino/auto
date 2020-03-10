from pynput.mouse import Button, Controller
import time

def click_position(position, button, delay=0.5):
    time.sleep(delay)
    mouse.position = position
    mouse.click(button, 1)

print('Downloading... ')
time.sleep(2)

mouse = Controller()
print(mouse.position)

center_position = (694, 424)
step = 30
save_as_position = (center_position[0] + step, center_position[1] + step)
save_position = (1195, 625)
next_position =(1336, 416)  # (1314, 411)

for _ in range(20):
    click_position(center_position, Button.right)
    click_position(save_as_position, Button.left)
    click_position(save_position, Button.left, delay=1)
    click_position(next_position, Button.left)

