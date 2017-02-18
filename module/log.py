import time

from colorama import Fore, Style, init

init(autoreset=True)


def __time():
    return time.strftime("[%Y-%m-%d %H:%M:%S]")


def info(msg):
    txt_m = Fore.GREEN + "[INFO]" + Fore.WHITE + msg
    print(txt_m + __time())


def pro(msg):
    txt_m = Fore.CYAN + "[PROGRESS]" + Fore.CYAN + Style.BRIGHT + msg
    print(txt_m + __time())


def inp(msg):
    txt_m = Fore.MAGENTA + "[INPUT]" + Fore.WHITE + Style.BRIGHT + msg
    print(txt_m)


def error(msg):
    txt_m = Fore.RED + "[ERROR]" + Fore.WHITE + Style.BRIGHT + msg
    print(txt_m)


def menu(msg):
    txt_m = Fore.MAGENTA + "[MENU]" + Fore.WHITE + Style.BRIGHT + msg
    print(txt_m)


def warn(msg):
    txt_m = Fore.YELLOW + "[WARNING]" + Fore.WHITE + Style.BRIGHT + msg
    print(txt_m)


def user(msg):
    txt_m = Fore.MAGENTA + "[USER]" + Fore.WHITE + Style.BRIGHT + msg
    print(txt_m)
