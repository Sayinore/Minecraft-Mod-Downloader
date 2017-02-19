import json
import os
import shutil
import time

import module.log as log
import module.screen as screen
import module.lang

log.info(_("Loading configs"))
with open("config.json") as cfg_f:
    cfg = json.load(cfg_f)
    game_p = cfg["game_p"]
    download_p = cfg["download_p"]


def inst(g_version, m_name):
    file = []
    cmd = ["slc"]
    cmd_h = [_("select the file as the mod")]

    log.info(_("Scanning files"))
    for i in os.scandir(download_p):
        name, ext = os.path.splitext(i.name)

        if ext == ".jar":
            file.append(i.path)
        if ext == ".zip":
            file.append(i.path)
        if ext == ".litemod":
            file.append(i.path)

        for j in file:
            c_time = os.stat(j).st_ctime
            if not c_time > time.time() - 600:
                file.remove(j)

    if len(file) == 0:
        log.warn(_("Scanned 0 file"))
        log.user(_("Drag the mod file here, or input the path of it."))
        inst_file = os.path.abspath(input()[1:-1])

    if len(file) == 1:
        inst_file = file.pop()

    if len(file) >= 1:
        log.menu(_("Mod file"))
        user_command, user_number = screen.menu(file, cmd, cmd_h)
        if user_command == "slc":
            inst_file = file[int(user_number) - 1]

    m_f_name = "[" + g_version + "]" + m_name + os.path.splitext(inst_file)[1]

    shutil.copy(inst_file, os.path.join(game_p, "mods", m_f_name))
    log.pro(_("Installation succeeded"))
    log.user(_("Thanks for using!"))

    time.sleep(2)
