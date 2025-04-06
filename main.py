import flet

from ui.launcher import NoxLauncher
from basic.constants import DEPLOYMENT_TYPE, NOXLAUNCHER_VERSION

def main(page: flet.Page) -> None:

    NoxLauncher(page)

if __name__ == "__main__":

    flet.app(target= main, name= f"NoxLauncher {DEPLOYMENT_TYPE} v{NOXLAUNCHER_VERSION}")