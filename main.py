import time
import keyboard

WIDTH = 600
HEIGHT = 400
FIGHTER_WIDTH = 30

'''
    1) Each movement goes +/- 10 horizontally
    2) Hit range: dx <= 70
    3) Minimun distance between fighters: 50
    4) Step time: 200ms
'''

def main():
    start()

def start():
    '''
        Starts the infinite loop with the timer
        and handles keyboard actions.
    '''
    time_step = 0
    while True:
        handle_actions(time_step)
        time.sleep(0.2) # handle new actions every 200ms
        time_step += 1

def handle_actions(time_step):
    '''
        Hanldes keyboard actions,
        the final implementation will handle
        agent actions.
    '''
    keyboard.on_press(on_key_pressed, suppress=False)
    # if keyboard.is_pressed('a'):
    #     print('You Pressed q Key! on step {}'.format(time_step))

def on_key_pressed(e):
    print('invokes callback with argument: {}'.format(e))

if __name__ == '__main__':
    main()
