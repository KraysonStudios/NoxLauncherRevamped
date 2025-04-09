import flet
import webbrowser

from apis.modrinth import MODRINTH_API
from typing import List

class ModsView:

    def __init__(self, page: flet.Page) -> None:

        self.page: flet.Page = page

        self.mods_list: List[flet.Container] = [
            flet.Container(
                flet.Container(
                    flet.TextField(
                        multiline= False, 
                        width= 700, 
                        height= 50, 
                        border_radius= 10, 
                        border_color= "#717171", 
                        border_width= 2, 
                        label= "Buscar mods", 
                        hint_text= "Ejemplo: Sodium",
                        text_style= flet.TextStyle(
                            font_family= "NoxLauncher",
                            color= "#FFFFFF",
                            size= 13
                        ),
                        hint_style= flet.TextStyle(
                            font_family= "NoxLauncher",
                            color= "#FFFFFF"
                        ),
                        label_style= flet.TextStyle(
                            font_family= "NoxLauncher",
                            color= "#FFFFFF"
                        ),
                    ),
                    width= 900,
                    height= 80,
                    alignment= flet.alignment.center,
                    border_radius= 30,
                    bgcolor= "#272727",
                ),
                alignment= flet.alignment.center,
                width= 910,
                height= 100,
                padding= flet.padding.only(top= 20, left= 10)
            )
        ]

        self.mods_list.extend(MODRINTH_API.retrieve_home())

        self.install_with_forge: bool = False
        self.install_with_fabric: bool = False
        self.install_with_quilt: bool = False

        self.mods_column = flet.Column(
            self.mods_list,
            expand= True,
            expand_loose= True,
            run_spacing= 25,
            spacing= 25,
            scroll= flet.ScrollMode.AUTO
        )

        self.build_ui()

    def build_ui(self) -> flet.View:
        
        return flet.View(
            "/mods",
            appbar= flet.AppBar(
                leading= flet.Container(
                    flet.FilledButton(
                        icon= flet.Icons.ARROW_BACK,
                        icon_color= "#FFFFFF",
                        text= "Volver",
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
                    alignment= flet.alignment.center,
                    padding= flet.padding.only(left= 20)
                ),
                leading_width= 200,
                title= flet.Image(
                    src= "assets/icon.png",
                    repeat= flet.ImageRepeat.NO_REPEAT,
                    width= 150,
                    height= 100,
                    filter_quality= flet.FilterQuality.HIGH,
                ),
                center_title= True,
                title_spacing= 0,
                toolbar_height= 120,
                actions= [
                    flet.Container(
                        flet.Row(
                            controls= [
                                flet.Container(
                                    flet.Image(
                                        src= "assets/discord.png",
                                        width= 50,
                                        height= 50,
                                    ),
                                    alignment= flet.alignment.center,
                                    width= 60,
                                    height= 60,
                                    on_click= lambda _: webbrowser.open_new_tab("https://discord.com/invite/DWfuQRsxwb"),
                                    on_hover= self.external_button_hover,
                                    bgcolor= "#272727",
                                    border_radius= 10
                                ),
                                flet.Container(
                                    flet.Image(
                                        src= "assets/github.png",
                                        width= 50,
                                        height= 50,
                                    ),
                                    alignment= flet.alignment.center,
                                    width= 60,
                                    height= 60,
                                    on_click= lambda _: webbrowser.open_new_tab("https://github.com/KraysonStudios/NoxLauncherRevamped"),
                                    on_hover= self.external_button_hover,
                                    bgcolor= "#272727",
                                    border_radius= 10
                                )
                            ],
                            spacing= 40,
                            alignment= flet.MainAxisAlignment.CENTER,
                            vertical_alignment= flet.VerticalAlignment.CENTER,
                            expand= True,
                            expand_loose= True
                        ),
                        height= 80,
                        width= 200,
                        alignment= flet.alignment.center,
                    )
                ],
                bgcolor= "#272727"
            ),
            controls= [
                flet.Container(
                    flet.Container(
                        flet.Container(
                            flet.Row(
                                controls= [
                                    flet.Column(
                                        [
                                            flet.Container(
                                                flet.Text(
                                                    "Cargadores de Mods",
                                                    size= 15,
                                                    font_family= "NoxLauncher",
                                                    color= "#FFFFFF"
                                                ),
                                                alignment= flet.alignment.center,
                                                height= 30,
                                                expand_loose= True
                                            ),
                                            flet.Container(
                                                flet.Row(
                                                    [
                                                        flet.Image(
                                                            src= "assets/fabric.png",
                                                            width= 60,
                                                            height= 60,
                                                            filter_quality= flet.FilterQuality.HIGH,
                                                        ),
                                                        flet.Text(
                                                            "Fabric",
                                                            font_family= "NoxLauncher",
                                                            size= 15,
                                                            color= "#FFFFFF"
                                                        )  
                                                    ],
                                                    alignment= flet.MainAxisAlignment.CENTER,
                                                    spacing= 20,
                                                    run_spacing= 20
                                                ),
                                                bgcolor= "#272727",
                                                width= 180,
                                                height= 70,
                                                border_radius= 20,
                                                alignment= flet.alignment.center,
                                                on_click= self.on_click_mod_loader,
                                                data= "fabric"
                                            ),
                                            flet.Container(
                                                flet.Row(
                                                    [
                                                        flet.Image(
                                                            src= "assets/quilt.png",
                                                            width= 70,
                                                            height= 70,
                                                            filter_quality= flet.FilterQuality.HIGH,
                                                        ),
                                                        flet.Text(
                                                            "Quilt",
                                                            font_family= "NoxLauncher",
                                                            size= 15,
                                                            color= "#FFFFFF"
                                                        )  
                                                    ],
                                                    alignment= flet.MainAxisAlignment.CENTER,
                                                    spacing= 20,
                                                    run_spacing= 20
                                                ),
                                                bgcolor= "#272727",
                                                width= 180,
                                                height= 70,
                                                border_radius= 20,
                                                alignment= flet.alignment.center,
                                                on_click= self.on_click_mod_loader,
                                                data= "quilt"
                                            ),
                                            flet.Container(
                                                flet.Row(
                                                    [
                                                        flet.Image(
                                                            src= "assets/forge.png",
                                                            width= 50,
                                                            height= 50,
                                                            filter_quality= flet.FilterQuality.HIGH,
                                                        ),
                                                        flet.Text(
                                                            "Forge",
                                                            font_family= "NoxLauncher",
                                                            size= 15,
                                                            color= "#FFFFFF"
                                                        )  
                                                    ],
                                                    alignment= flet.MainAxisAlignment.CENTER,
                                                    spacing= 20,
                                                    run_spacing= 20
                                                ),
                                                bgcolor= "#272727",
                                                width= 180,
                                                height= 70,
                                                border_radius= 20,
                                                alignment= flet.alignment.center,
                                                on_click= self.on_click_mod_loader,
                                                data= "forge"
                                            )
                                        ],
                                        alignment= flet.MainAxisAlignment.CENTER,
                                        horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                                        height= 1000,
                                        width= 200,
                                        spacing= 25,
                                        run_spacing= 25
                                    ),
                                    flet.VerticalDivider(color= "#717171", width= 1, thickness= 1),
                                    self.mods_column
                                ],
                                expand_loose= True,
                                expand= True,
                                run_spacing= 25,
                                spacing= 25
                            ),
                            width= 1000,
                            height= 500,
                            border_radius= 10,
                            blur= flet.Blur(
                                5,
                                5,
                                tile_mode= flet.BlurTileMode.MIRROR
                            )
                        ),
                        alignment= flet.alignment.center,
                        expand= True,
                        expand_loose= True
                    ),
                    image= flet.DecorationImage(
                        src= "assets/bgmods.png", 
                        fit= flet.ImageFit.COVER, 
                        filter_quality= flet.FilterQuality.HIGH, 
                        repeat= flet.ImageRepeat.NO_REPEAT,
                    ), 
                    expand_loose= True,
                    expand= True
                )
            ],
            padding= 0
        )

    def external_button_hover(self, event: flet.ControlEvent) -> None:

        event.control.bgcolor = "#4a4a4a" if event.control.bgcolor == "#272727" else "#272727"
        event.control.update()

            
    def on_click_mod_loader(self, event: flet.ControlEvent) -> None:

        event.control.bgcolor = "#148b47" if event.control.bgcolor == "#272727" else "#272727"

        match event.control.data:

            case "fabric": self.install_with_fabric = True
            case "forge": self.install_with_forge = True
            case "quilt": self.install_with_quilt = True

        event.control.update()
