import flet

from ui.home import HomeView
from ui.settings import SettingsView
from ui.accounts import AccountView
from basic.constants import NOXLAUNCHER_VERSION

class NoxLauncher:

    def __init__(self, page: flet.Page) -> None:
        
        self.page: flet.Page = page

        self.page.title = f"NoxLauncher v{NOXLAUNCHER_VERSION}"

        self.page.fonts = {
            "NoxLauncher": "assets/fonts/NoxLauncher.ttf" 
        }

        self.page.theme = None
        self.page.theme_mode = None
        self.page.window.width = 1290
        self.page.window.height = 720
        self.page.bgcolor = "#272727"

        self.page.update()

        self.rounter: StandaloneRouter = StandaloneRouter(page)
        
        self.page.go("/home")

class StandaloneRouter:

    def __init__(self, page: flet.Page):
        self.page: flet.Page = page
        self.build_routing()
        
    def build_routing(self) -> None:

        def routing(_: flet.RouteChangeEvent) -> None:
            self.page.views.clear()

            match self.page.route:
                case "/home": self.page.views.append(HomeView(self.page).build_ui())
                case "/accounts": self.page.views.append(AccountView(self.page).build_ui())
                case "/settings": self.page.views.append(SettingsView(self.page).build_ui())

            self.page.update()

        self.page.on_route_change = routing
    
