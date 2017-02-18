import json
import os
import platform

import module.log as log

u_cfg = open("config.json", "w")
game_p = "Cannot auto scan"
download_p = "Cannot auto scan"

if platform.system() == "Windows":
    game_p = os.path.join(os.environ.get("appdata"), ".minecraft")
    download_p = os.path.join(os.environ.get("userprofile"), "downloads")

if platform.system() == "Linux":
    game_p = os.path.join(os.environ.get("home"), ".minecraft")
    download_p = os.path.join(os.environ.get("home"), "downloads")

log.user("Is your game path this? \"" + game_p + "\" If so, press Enter, or input it.")
log.inp("Game path")
ipt_game_p = input()
if ipt_game_p == "":
    game_p = os.path.abspath(game_p)
else:
    game_p = os.path.abspath(ipt_game_p)
print()

log.user("Is your game path this? \"" + download_p + "\" If so, press Enter, or input it.")
log.inp("Download path")
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

print("Finished!")
