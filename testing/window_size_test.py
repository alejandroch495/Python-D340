from ezgraphics import *
import keyboard
user_options = [0]
user_window_pref : int = 0
window_sizes ={
    "default" : [800,600],
    "1080p" : [1920,1080],
    "900p" : [1600,900],
    "720p" : [1280,720],
    "600p" : [800,600]
    }

def create_win(size) -> GraphicsWindow:
    win = GraphicsWindow(size[0],size[1])
    return win  

def get_canvas(win):
    canvas = win.canvas()
    return canvas

def get_user_window_pref() -> int:
    try:
        user_input = int(input("select a window size by entering the number value on the left \n Selection : "))    
    except Exception as e:
        print(e)

    return user_input

def display_window_size_options() -> None:
    generic_counter : int = 0
    print(f"sel.    res.    size.")
    for sizes in window_sizes:
        print(f"{generic_counter}. {sizes} = {window_sizes[sizes]}")
        generic_counter = generic_counter + 1

def set_resolution(window_sizes = window_sizes, selection = int) -> str:
    test_list : list = []
    for i in window_sizes:
        test_list.append([window_sizes[i]])
    temp = test_list[selection]
    return temp[0]

def draw_rectangle_center(canvas, resolution: list = [], size : list =[]):
    canvas.drawRectangle(resolution[0]/2-size[0]/2,resolution[1]/2-size[1]/2,size[0],size[1])
    
def get_key_pressed():
    key = None
    prevKey = None
    if key == None:
        key = keyboard.get_hotkey_name()
    elif key != None and key != prevKey :
        if key !='':
            return key
        prevKey = key   
    else:
        key = None

size : list = [100,100]
display_window_size_options()
user_window_pref = get_user_window_pref()
resolution_selected = set_resolution(selection=user_window_pref)
print(set_resolution(selection=user_window_pref))
test_win = create_win(resolution_selected)
canvas = get_canvas(test_win)
test_square = draw_rectangle_center(canvas,resolution_selected,size)

test_win.wait()
isRunning = True
while isRunning:
    print(get_key_pressed()) 