import flet
import socket
import datetime
import aiohttp
import asyncio

from functools import lru_cache
from typing import Dict, List, Any

class ModrinthAPI:

    def __init__(self, loaders: List[str]) -> None:
    
        self.mc_loaders: List[str] = loaders
        self.base_url: str = "https://api.modrinth.com/v2"
        self.headers: Dict[str, str] = {"User-Agent": "https://github.com/KraysonStudios/NoxLauncher"}

        self.rate_limiter_storage: Dict[str, Any] = {"count": 0, "time": datetime.datetime.now(), "blocked": False}
        self.mods_versions: Dict[str, List[str]] = {}

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

        try:


            response = self.execute_request(
                f"{self.base_url}/search",
                {
                    "limit": 5,
                }
            )                

        except:

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
                                "Algo a salido mal, regrese más tarde.",
                                font_family= "NoxLauncher",
                                size= 17,
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

        for project in response["hits"]:

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
                                        padding= flet.padding.all(10),
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

                                        flet.Row(
                                            [
                                                flet.Image(
                                                    src= "assets/version.png",
                                                    width= 30,
                                                    height= 30,
                                                    filter_quality= flet.FilterQuality.HIGH,
                                                ),
                                                flet.Text(
                                                    version,
                                                    font_family= "NoxLauncher",
                                                    size= 13,
                                                    color= "#FFFFFF",
                                                    overflow= flet.TextOverflow.ELLIPSIS
                                                ),
                                            ],
                                            spacing= 8,
                                            run_spacing= 8,
                                            alignment= flet.MainAxisAlignment.CENTER
                                        ),
                                        alignment= flet.alignment.center,
                                        bgcolor= "#272727",
                                        padding= flet.padding.all(10),
                                        border_radius= 20,
                                    ) for version in reversed(project["versions"])
                                ],
                                spacing= 10,
                                run_spacing= 10,
                                scroll= flet.ScrollMode.AUTO,
                                alignment= flet.MainAxisAlignment.START
                            ),
                            flet.Container(
                                flet.Row(
                                    controls= [
                                        flet.Container(
                                            flet.Dropdown(
                                                hint_text= "Versión de Minecraft", 
                                                options= [
                                                    flet.dropdown.Option(
                                                        version, 
                                                        style= flet.ButtonStyle(
                                                            text_style= flet.TextStyle(
                                                                size= 13,
                                                                font_family= "NoxLauncher",
                                                                color= "#FFFFFF"
                                                            )
                                                        )
                                                    ) for version in reversed(project["versions"]) 
                                                ], 
                                                border_color= "#717171", 
                                                menu_height= 250,
                                                border_radius= 10, 
                                                border_width= 2, 
                                                width= 270,
                                                text_style= flet.TextStyle(
                                                    font_family= "NoxLauncher",
                                                    color= "#FFFFFF"
                                                ),
                                                hint_style= flet.TextStyle(
                                                    font_family= "NoxLauncher",
                                                    color= "#FFFFFF"
                                                ),
                                                on_change= self.add_mod_version,
                                                data= project["slug"],
                                            ),
                                            width= 300,
                                            height= 150,
                                            alignment= flet.alignment.center,
                                            border_radius= 20,
                                            bgcolor= "#272727",  
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
                                                on_click= self.install_mod,
                                                data= project["slug"]
                                            ),
                                            alignment= flet.alignment.center,
                                        )
                                    ],
                                    alignment= flet.MainAxisAlignment.END,
                                    vertical_alignment= flet.CrossAxisAlignment.END,
                                    run_spacing= 20,
                                    spacing= 20
                                ),
                                expand_loose= True,
                                height= 70,
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
                    height= 430,
                    padding= flet.padding.only(left= 20, right= 20)
                )
            )

        return contain

    def rate_limiter(self) -> bool: 

        if self.rate_limiter_storage["count"] >= 5 and not self.rate_limiter_storage["blocked"]:

            self.rate_limiter_storage["time"] =  datetime.datetime.now() + datetime.timedelta(seconds= 30)
            self.rate_limiter_storage["blocked"] = True
            return True

        elif self.rate_limiter_storage["time"] <= datetime.datetime.now() and self.rate_limiter_storage["blocked"]: 

            self.rate_limiter_storage["count"] = 0
            self.rate_limiter_storage["time"] = datetime.datetime.now()
            self.rate_limiter_storage["blocked"] = False
            return False
        
        elif self.rate_limiter_storage["count"] >= 5: return True

        self.rate_limiter_storage["count"] += 1
        
        return False
    
    def execute_request(self, url: str, parameters: Dict[str, Any]) -> Any:

        async def _exec(url: str, parameters: Dict[str, Any]) -> Any:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params= parameters, headers= self.headers) as response:

                    if response.status == 200:
                        return await response.json()
                    else:
                        raise RuntimeError(f"Request '{url}' throw status code '{response.status}'.")

        result = asyncio.run(_exec(url, parameters))

        return result

    def add_mod_version(self, event: flet.ControlEvent) -> None:
        
        if event.control.value is None: return

        mod_slug: str = event.control.data

        if self.mods_versions.get(mod_slug) is not None:

            self.mods_versions[mod_slug].append(event.control.value)
            return
        
        self.mods_versions[mod_slug] = [event.control.value]

    def install_mod(self, event: flet.ControlEvent) -> None: 
        
        modrinth_identifier: str = event.control.data
    
    @lru_cache(maxsize= 15)
    def has_internet(self) -> bool:

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False

MODRINTH_API: ModrinthAPI = ModrinthAPI([])