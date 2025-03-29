import flet

from basic.constants import *

class HomeView:

    def __init__(self, page: flet.Page) -> None:
        self.page: flet.Page = page
        self.build_ui()

    def build_ui(self) -> flet.View:

        self.page.title = f"NoxLauncher v{NOXLAUNCHER_VERSION} - home"

        return flet.View(
            "/home",
            controls= [],
            padding= 0
        )