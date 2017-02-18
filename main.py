import webbrowser

import module.get_link as get
import module.install as inst
import module.log as log
import module.screen as screen
import module.search as search

# Array
cmd = ["get"]
cmd_h = ["try to get download link of the mod from this link"]

# user guide
screen.cls()
print("Welcome Use Minecraft Mod Downloader by Sayinore!".center(80, "-"))
print()

m_name = ""
while m_name == "":
    log.inp("Mod name")
    m_name = input()
    if m_name == "":
        log.error("Invalid mod name")
print()

log.inp("Game version")
g_version = input()
print()

log.inp("Max page number")
log.user("The program will get that page(s) of search result.")
m_page = input()
print()

screen.cls()

log.user("Mod name: " + m_name)
log.user("Game version: " + g_version)
log.user("Max page number: " + m_page)

# search
print()
page = 1
mcbbs_text = []
mcbbs_link = []

while page <= int(m_page):
    log.pro("Processing page " + str(page) + " of the search result")
    text, link = search.mcbbs(m_name, g_version, page)
    for i in link:
        mcbbs_link.append(i)

    for i in text:
        mcbbs_text.append(i)

    page += 1

log.pro("Finished searching")
screen.cls()
log.menu("Thread to download")
user_command, user_number = screen.menu(text, cmd, cmd_h)
if user_command == "get":
    screen.cls()
    link = get.mcbbs(mcbbs_link[int(user_number) - 1])
    if link:
        log.pro("Getting download link succeeded")
        log.info("Going downloading")
        webbrowser.open(link)

    else:
        log.warn("Getting download link failed")
        log.info("Going reading the thread")
        webbrowser.open(mcbbs_link[user_number])

    log.user("If you have finished downloading, please press Enter to continue.")
    input()

    inst.inst(g_version, m_name)
