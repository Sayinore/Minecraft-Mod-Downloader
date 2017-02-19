import json
import os
import platform
import time

import module.log as log
import module.lang

u_cfg = open("config.json", "w")
game_p = "Cannot auto scan"
download_p = "Cannot auto scan"

if platform.system() == "Windows":
    game_p = os.path.join(os.environ.get("appdata"), ".minecraft")
    download_p = os.path.join(os.environ.get("userprofile"), "downloads")

if platform.system() == "Linux":
    game_p = os.path.join(os.environ.get("home"), ".minecraft")
    download_p = os.path.join(os.environ.get("home"), "downloads")

log.user(_("Is your game path this? \"%s\" If so, please press Enter; or input it.") % game_p)
log.inp(_("Game path"))
ipt_game_p = input()
if ipt_game_p == "":
    game_p = os.path.abspath(game_p)
else:
    game_p = os.path.abspath(ipt_game_p)
print()

log.user(_("Is your download path this? \"%s\" If so, please press Enter; or input it.") % download_p)
log.inp(_("Download path"))
ipt_download_p = input()
if ipt_download_p == "":
    download_p = os.path.abspath(download_p)
else:
    download_p = os.path.abspath(ipt_download_p)
    print()

cfg = {
    "game_p": game_p,
    "download_p": download_p
}
u_cfg.write(json.dumps(cfg, indent=4))

log.user(_("Finished!"))
time.sleep(2)
