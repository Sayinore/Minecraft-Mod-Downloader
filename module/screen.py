import os
import platform
import time

from colorama import init, Fore, Style

import module.log as log
import module.lang

init(autoreset=True)


def cls():
    if platform.system() == "Windows":
        os.system("cls")

    if platform.system() == "Linux":
        os.system("clear")


def menu(lst, cmd, cmd_h):
    lest = str(len(lst)) + "        "
    space = len(lest) - 4
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + _("Order") + " " * space + _("Item"))
    for i in lst:
        num = lst.index(i) + 1
        txt = Style.BRIGHT + str(num) + "        " + Style.NORMAL + i
        while len(txt[:-len(i) - 1]) < len(lest):
            txt = "  ".join(txt.split(" ", 1))
        print(txt)

    print()
    log.user(_("Usage: %s(command) (number)") % Style.BRIGHT)
    log.user(_("Command list:"))
    lens = list(map(len, cmd))
    lest = cmd[lens.index(max(lens))] + "----"
    for (k, t) in zip(cmd, cmd_h):
        txt = k + "----" + t
        while len(txt[:txt.rfind("-") + 1]) < len(lest):
            txt = "--".join(txt.split("-", 1))
        print(Style.BRIGHT + txt)

    print()
    log.inp(_("Command"))
    user_ipt = input()

    if user_ipt.find(" "):
        user_cmd, user_ord = user_ipt.split(" ")
    else:
        user_cmd, user_ord = "", ""

    if user_cmd in cmd:
        return user_cmd, user_ord

    log.error(_("Invalid command"))
    time.sleep(2)
    cls()
    menu(lst, cmd, cmd_h)
