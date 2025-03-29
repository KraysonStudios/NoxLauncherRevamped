import flet

from ui.home import HomeView

class Launcher:

    def __init__(self, page: flet.Page) -> None:
        
        self.page: flet.Page = page
        self.rounter: StandaloneRouter = StandaloneRouter(page)

        self.rounter.go_to_home()

        self.build_ui()

    def build_ui(self) -> None:

        ...

class StandaloneRouter:

    def __init__(self, page: flet.Page):
        self.page: flet.Page = page
        self.build_routing()
        
    def build_routing(self) -> None:

        def routing(_: flet.RouteChangeEvent) -> None:
            self.page.views.clear()

            match self.page.route:
                case "/home": self.page.views.append(HomeView(self.page).build_ui())

            self.page.update()

        self.page.on_route_change = routing

    def go_to_home(self) -> None:
        self.page.go("/home")
    