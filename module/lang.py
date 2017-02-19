import locale
import gettext

lang = gettext.translation(locale.getdefaultlocale(envvars="LANG")[0], localedir="language", fallback=True)
lang.install()
_ = lang.gettext
