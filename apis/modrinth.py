import flet
import socket
import datetime
import requests

from typing import Dict, List, Any

class ModrinthAPI:

    def __init__(self, loaders: List[str]) -> None:
    
        self.mc_loaders: List[str] = loaders
        self.base_url: str = "https://api.modrinth.com/v2"
        self.headers: Dict[str, str] = {"User-Agent": "https://github.com/KraysonStudios/NoxLauncher"}

        self.rate_limiter_storage: Dict[str, Any] = {"count": 0, "time": datetime.datetime.now(), "blocked": False}

    def retrieve_home(self) -> List[flet.Container]:

        contain: List[flet.Container] = []

        if self.rate_limiter():

            contain.clear()
            contain.append(
                flet.Container(
                    flet.Row(
                        [
                            flet.Icon(
                                flet.Icons.ERROR,
                                size= 40,
                                color= flet.Colors.RED_400
                            ),
                            flet.Text(
                                "Te encuentras limitado. Regrese más tarde.",
                                font_family= "NoxLauncher",
                                size= 20,
                                color= "#FFFFFF"
                            )
                        ],
                        spacing= 20,
                        run_spacing= 20,
                        alignment= flet.MainAxisAlignment.CENTER,
                    ),
                    alignment= flet.alignment.center,
                    expand_loose= True,
                    height= 100,
                    padding= flet.padding.only(left= 20, right= 20)
                )
            )

            return contain
        
      
        if not self.has_internet():

            contain.clear()
            contain.append(
                flet.Container(
                    flet.Row(
                        [
                            flet.Icon(
                                flet.Icons.ERROR,
                                size= 40,
                                color= flet.Colors.RED_400
                            ),
                            flet.Text(
                                "No te encuentras conectado a internet. Vuelve más tarde.",
                                font_family= "NoxLauncher",
                                size= 15,
                                color= "#FFFFFF"
                            )
                        ],
                        spacing= 20,
                        run_spacing= 20,
                        alignment= flet.MainAxisAlignment.CENTER,
                    ),
                    alignment= flet.alignment.center,
                    expand_loose= True,
                    height= 100,
                    padding= flet.padding.only(left= 20, right= 20)
                )
            )

            return contain
        
        request: requests.Request = requests.get(f"{self.base_url}/search", headers= self.headers)

        for project in request.json()["hits"]:

            contain.append(
                flet.Container(
                    flet.Column(
                        [
                            flet.Row(
                                [
                                    flet.Image(src= project["icon_url"], width= 60, height= 60),
                                    flet.VerticalDivider(color= "#717171", width= 1, thickness= 1),
                                    flet.Text(
                                        project["title"],
                                        font_family= "NoxLauncher",
                                        size= 18,
                                        color= "#FFFFFF",
                                        overflow= flet.TextOverflow.FADE
                                    )
                                ],
                                spacing= 10,
                                run_spacing= 10
                            ),
                            flet.Container(
                                flet.Text(
                                    project["description"],
                                    font_family= "NoxLauncher",
                                    size= 14,
                                    color= "#FFFFFF",
                                    overflow= flet.TextOverflow.FADE
                                ),
                                alignment= flet.alignment.center_left,
                                expand_loose= True,
                                height= 50,
                            ),
                            flet.Container(
                                flet.Row(
                                    [
                                        flet.Icon(
                                            flet.Icons.DOWNLOAD,
                                            size= 30,
                                            color= "#717171"
                                        ),
                                        flet.Text(
                                            project["downloads"],
                                            font_family= "NoxLauncher",
                                            size= 15,
                                            color= "#FFFFFF",
                                            overflow= flet.TextOverflow.ELLIPSIS
                                        ),
                                    ],
                                    spacing= 10,
                                    run_spacing= 10
                                ),
                                alignment= flet.alignment.center,
                                expand_loose= True,
                                height= 40
                            ),
                            flet.Row(
                                [
                                    flet.Container(
                                        flet.Text(
                                            version,
                                            font_family= "NoxLauncher",
                                            size= 13,
                                            color= "#FFFFFF",
                                            overflow= flet.TextOverflow.ELLIPSIS
                                        ),
                                        alignment= flet.alignment.center,
                                        bgcolor= "#272727",
                                        width= 100,
                                        height= 45,
                                        border_radius= 20,
                                    ) for version in project["categories"]
                                ],
                                spacing= 10,
                                run_spacing= 10,
                                alignment= flet.MainAxisAlignment.START,
                                vertical_alignment= flet.MainAxisAlignment.START
                            ),
                            flet.Row(
                                [
                                    flet.Container(
                                        flet.Text(
                                            version,
                                            font_family= "NoxLauncher",
                                            size= 13,
                                            color= "#FFFFFF",
                                            overflow= flet.TextOverflow.ELLIPSIS
                                        ),
                                        alignment= flet.alignment.center,
                                        bgcolor= "#272727",
                                        width= 80,
                                        height= 45,
                                        border_radius= 20,
                                    ) for version in reversed(project["versions"])
                                ],
                                spacing= 10,
                                run_spacing= 10,
                                scroll= flet.ScrollMode.AUTO,
                                alignment= flet.MainAxisAlignment.START
                            ),
                            flet.Container(
                                flet.FilledButton(
                                    icon= flet.Icons.DOWNLOAD,
                                    icon_color= "#FFFFFF",
                                    text= "Instalar",
                                    color= "#FFFFFF",
                                    bgcolor= "#148b47",
                                    width= 150,
                                    height= 45,
                                    style= flet.ButtonStyle(
                                        shape= flet.RoundedRectangleBorder(radius= 5),
                                        text_style= flet.TextStyle(
                                            font_family= "NoxLauncher"
                                        )
                                    ),
                                    on_click= lambda _: self.page.go("/home")
                                ),
                                expand_loose= True,
                                height= 40,
                                padding= flet.padding.only(top= 5, right= 20),
                                alignment= flet.alignment.center_right
                            ),
                        ],
                        expand= True,
                        expand_loose= True,
                        alignment= flet.MainAxisAlignment.CENTER,
                        horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                        spacing= 10,
                        run_spacing= 10
                    ),
                    expand_loose= True,
                    alignment= flet.alignment.center,
                    height= 350,
                    padding= flet.padding.only(left= 20, right= 20)
                )
            )

        return contain

    def rate_limiter(self) -> bool: 

        if self.rate_limiter_storage["count"] >= 10 and not self.rate_limiter_storage["blocked"]:

            self.rate_limiter_storage["time"] =  datetime.datetime.now() + datetime.timedelta(seconds= 30)
            self.rate_limiter_storage["blocked"] = True
            return True

        elif self.rate_limiter_storage["time"] <= datetime.datetime.now() and self.rate_limiter_storage["blocked"]: 

            self.rate_limiter_storage["count"] = 0
            self.rate_limiter_storage["time"] = datetime.datetime.now()
            self.rate_limiter_storage["blocked"] = False
            return False
        
        elif self.rate_limiter_storage["count"] >= 10: return True

        self.rate_limiter_storage["count"] += 1
        
        return False
    
    def has_internet(self) -> bool:

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False

MODRINTH_API: ModrinthAPI = ModrinthAPI([])