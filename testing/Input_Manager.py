import keyboard
def get_key_pressed():
    is_running = True
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
while is_running:
    print(get_key_pressed())