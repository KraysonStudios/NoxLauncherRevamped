import flet
import socket
import datetime
import aiohttp
import asyncio
import time

from functools import lru_cache
from typing import Dict, List, Any

from filesystem.utils import GetFolderMods
from ui.alert import ErrorAlert

class ModrinthAPI:

    def __init__(self, page: flet.Page, mod_loader: str) -> None:
        
        self.page: flet.Page = page
        self.mod_loader: str = mod_loader
        self.base_url: str = "https://api.modrinth.com/v2"
        self.headers: Dict[str, str] = {"User-Agent": "https://github.com/KraysonStudios/NoxLauncher"}

        self.rate_limiter_storage: Dict[str, Any] = {"count": 0, "time": datetime.datetime.now(), "blocked": False}
        self.mods_versions: Dict[str, str] = {}

    def search(self, parameters: Dict[str, Any]) -> List[flet.Container]:

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


            ModrinthHomePage = self.execute_request(
                f"{self.base_url}/search",
                parameters,
                True,
                False
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
        
        if ModrinthHomePage is None:

            self.page.open(
                ErrorAlert(self.page, description= f"No se ha podido cargar la página principal de Modrinth. Regrese más tarde.").build()
            )

            return
        

        for project in ModrinthHomePage["hits"]:

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
    
    def execute_request(self, url: str, parameters: Dict[str, Any], return_json: bool, return_bytes: bool) -> Any:

        async def _exec(url: str, parameters: Dict[str, Any]) -> Any:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params= parameters, headers= self.headers) as response:

                    if response.status == 200 and not return_json and not return_bytes:
                        return response
                    elif response.status == 200 and return_json:
                        return await response.json()
                    elif response.status == 200 and return_bytes:
                        return await response.content.read()
                    else:
                        raise None

        result = asyncio.run(_exec(url, parameters))

        return result

    def add_mod_version(self, event: flet.ControlEvent) -> None:
        
        if event.control.value is None: return

        mod_slug: str = event.control.data
        
        if self.mods_versions.get(mod_slug) is not None:

            self.mods_versions[mod_slug] = event.control.value
            return
        
        self.mods_versions[mod_slug] = event.control.value

    def set_mod_loader(self, mod_loader: str) -> None: self.mod_loader = mod_loader

    def install_mod(self, event: flet.ControlEvent) -> None: 

        if len(self.mod_loader) == 0:

            self.page.open(
                ErrorAlert(self.page, description= "Debes seleccionar un cargador de mods previamente!").build()
            )

            return
        
        mod_identifier: str = event.control.data
        mod_loader_target: str = self.mod_loader
        mod_version_target: str = self.mods_versions.get(mod_identifier)

        whole_project = self.execute_request(
            f"{self.base_url}/project/{mod_identifier}/version",
            {},
            True,
            False
        )

        if whole_project is None:

            self.page.open(
                ErrorAlert(self.page, description= f"No se ha podido descargar el mod '{mod_identifier.capitalize()}'. Regrese más tarde.").build()
            )

            return

        if self.mods_versions.get(mod_identifier) is None:

            self.page.open(
                ErrorAlert(self.page, description= f"Debes seleccionar una versión de minecraft para el mod '{mod_identifier.capitalize()}'.").build()
            )

            return
        
        matching_versions: List[Dict[str, Any]] = [
            version for version in whole_project
            if mod_version_target in version["game_versions"] and mod_loader_target in version["loaders"]
        ]

        matching_versions.sort(key= lambda date: date["date_published"], reverse= True)

        if len(matching_versions) == 0:

            self.page.open(
                ErrorAlert(self.page, description= f"Cero resultados para '{mod_identifier.capitalize()}', para la version '{mod_version_target}' con los mod loader '{self.mod_loader}'.").build()
            )

            return
        
        install_text_info: flet.Text = flet.Text(value= "Descargando & instalando...", size= 14, font_family= "NoxLauncher", color= "#FFFFFF")
        install_progress_bar: flet.ProgressBar = flet.ProgressBar(width= 150, color= "#148b47")
        
        install: flet.AlertDialog = flet.AlertDialog(
            modal= True,
            icon= flet.Image(
                src= "assets/icon.png",
                width= 150,
                height= 100,
                repeat= flet.ImageRepeat.NO_REPEAT,
                filter_quality= flet.FilterQuality.HIGH
            ),
            bgcolor= "#272727",
            content= flet.Column(
                [
                    flet.Text(value= matching_versions[0]["files"][0]["filename"], size= 21, font_family= "NoxLauncher", color= "#717171"),
                    install_text_info,
                    install_progress_bar
                ],
                alignment= flet.MainAxisAlignment.CENTER,
                horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                height= 100,
                expand_loose= True,
                spacing= 10,
                run_spacing= 10
            ),
            actions= [
                flet.FilledButton(
                    text= "Cancelar",
                    style= flet.ButtonStyle(
                        color= "#FFFFFF",
                        bgcolor= "#148b47",
                        text_style= flet.TextStyle(font_family= "NoxLauncher", size= 18),
                        shape= flet.RoundedRectangleBorder(radius= 10)
                    ),
                    height= 50,
                    width= 150,
                    on_click= lambda _: self.page.close(install)
                )
            ],
            on_dismiss= lambda _: None
        )

        self.page.open(install)

        mod_jar = self.execute_request(
            matching_versions[0]["files"][0]["url"],
            {},
            False,
            True
        )

        if mod_jar is None:

            self.page.open(
                ErrorAlert(self.page, description= f"No se ha podido descargar el mod '{mod_identifier.capitalize()}'. Regrese más tarde.").build()
            )

            return

        with open(f"{GetFolderMods()}/{matching_versions[0]["files"][0]["filename"]}", "wb") as jar: jar.write(mod_jar)

        install_text_info.value = "Instalado."
        install_text_info.size = 14
        install_text_info.update()

        install_progress_bar.value = 100
        install_progress_bar.update()

        time.sleep(3)

        self.page.close(install)
        
    @lru_cache(maxsize= 15)
    def has_internet(self) -> bool:

        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False