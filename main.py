import flet
import sys

from handler import handle_uncaught_exception
from ui.launcher import Launcher
from basic.constants import * 

def main(page: flet.Page) -> None:

    sys.excepthook = handle_uncaught_exception   

    Launcher(page)

if __name__ == "__main__":

    flet.app(target= main, name= f"NoxLauncher v{NOXLAUNCHER_VERSION}")