import time
import gettext

from colorama import Fore, Style, init

import module.lang

init(autoreset=True)


def __time():
    return time.strftime("[%Y-%m-%d %H:%M:%S]")


def info(msg):
    txt_m = _("{g}[INFO]{w}").format(g=Fore.GREEN, w=Fore.WHITE)
    print(_(__time() + txt_m + msg))


def pro(msg):
    txt_m = _("{c}[PROGRESS]{b}").format(c=Fore.CYAN, b=Style.BRIGHT)
    print(_(__time() + txt_m + msg))


def inp(msg):
    txt_m = _("{m}[INPUT]{w}{b}").format(m=Fore.MAGENTA, w=Fore.WHITE, b=Style.BRIGHT)
    print(txt_m + msg)


def error(msg):
    txt_m = _("{r}[ERROR]{w}{b}").format(r=Fore.RED, w=Fore.WHITE, b=Style.BRIGHT)
    print(txt_m + msg)


def menu(msg):
    txt_m = _("{m}[MENU]{w}{b}").format(m=Fore.MAGENTA, w=Fore.WHITE, b=Style.BRIGHT)
    print(txt_m + msg)


def warn(msg):
    txt_m = _("{y}[WARNING]{w}{b}").format(y=Fore.YELLOW, w=Fore.WHITE, b=Style.BRIGHT)
    print(txt_m + msg)


def user(msg):
    txt_m = _("{m}[USER]{w}{b}").format(m=Fore.MAGENTA, w=Fore.WHITE, b=Style.BRIGHT)
    print(txt_m + msg)
