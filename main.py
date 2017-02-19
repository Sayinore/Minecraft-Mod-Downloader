import webbrowser

import module.get_link as get
import module.install as inst
import module.log as log
import module.screen as screen
import module.search as search
import module.lang


# Array
cmd = ["get"]
cmd_h = [_("try getting download link of the mod from this link")]

# user guide
screen.cls()
print(_("Welcome Use Minecraft Mod Downloader by Sayinore!").center(80, "-"))
print()

m_name = ""
while m_name == "":
    log.inp(_("Mod name"))
    m_name = input()
    if m_name == "":
        log.error(_("Invalid mod name"))
print()

log.inp(_("Game version"))
g_version = input()
print()

log.inp(_("Max page number"))
log.user(_("The program will get that page(s) of search result."))
m_page = input()
print()

screen.cls()

log.user(_("Mod name: %s") % m_name)
log.user(_("Game version: %s") % g_version)
log.user(_("Max page number: %s") % m_page)

# search
print()
page = 1
mcbbs_text = []
mcbbs_link = []

while page <= int(m_page):
    log.pro(_("Processing page %s of the search result") % str(page))
    text, link = search.mcbbs(m_name, g_version, page)
    for i in link:
        mcbbs_link.append(i)

    for i in text:
        mcbbs_text.append(i)

    page += 1

log.pro(_("Finished searching"))
screen.cls()
log.menu(_("Thread to download the mod from"))
user_command, user_number = screen.menu(mcbbs_text, cmd, cmd_h)
if user_command == "get":
    screen.cls()
    link = get.mcbbs(mcbbs_link[int(user_number) - 1])
    if link:
        log.pro(_("Getting download link succeeded"))
        log.info(_("Going downloading"))
        webbrowser.open(link)

    else:
        log.warn(_("Getting download link failed"))
        log.info(_("Going reading the thread"))
        webbrowser.open(mcbbs_link[int(user_number)])

    log.user(_("If you have finished downloading, please press Enter to continue."))
    input()

    inst.inst(g_version, m_name)
