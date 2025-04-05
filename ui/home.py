import flet
import webbrowser

class HomeView:

    def __init__(self, page: flet.Page) -> None:
        self.page: flet.Page = page
        self.build_ui()

    def build_ui(self) -> flet.View:

        return flet.View(
            "/home",
            appbar= flet.AppBar(
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
            bottom_appbar= flet.BottomAppBar(
                height= 120,
                expand_loose= True,
                bgcolor= "#272727",
                content= flet.Row(
                    expand= True,
                    expand_loose= True,
                    controls= [
                        flet.Container(
                            flet.TextField(
                                multiline= False, 
                                width= 250, 
                                height= 70, 
                                border_radius= 10, 
                                border_color= "#717171", 
                                border_width= 2, 
                                label= "Nombre de usuario", 
                                hint_text= "Ejemplo: elRasshXD",
                                text_style= flet.TextStyle(
                                    font_family= "NoxLauncher",
                                    color= "#FFFFFF"
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
                            height= 70,
                            width= 250,
                            alignment= flet.alignment.center,
                            padding= flet.padding.only(top= 10)
                        ),
                        flet.Container(
                            flet.Dropdown(
                                hint_text= "Versión de Minecraft", 
                                options= [flet.dropdown.Option("1.16.5")], 
                                border_color= "#717171", border_radius= 10, 
                                border_width= 2, 
                                width= 270,
                                text_style= flet.TextStyle(
                                    font_family= "NoxLauncher"
                                ),
                                hint_style= flet.TextStyle(
                                    font_family= "NoxLauncher"
                                ),
                            ),
                            height= 70,
                            width= 270,
                            alignment= flet.alignment.center,
                        ),
                        flet.Container(
                            flet.FilledButton(
                                text= "Jugar",
                                color= "#FFFFFF",
                                bgcolor= "#148b47",
                                width= 150,
                                height= 45,
                                style= flet.ButtonStyle(
                                    shape= flet.RoundedRectangleBorder(radius= 5),
                                    text_style= flet.TextStyle(
                                        font_family= "NoxLauncher"
                                    )
                                )
                            ),
                            height= 45,
                            width= 150,
                            alignment= flet.alignment.center,
                        ),
                        flet.Container(expand= True, expand_loose= True),
                        flet.Container(
                            flet.IconButton(
                                flet.Icons.LOGIN,
                                icon_size= 40,
                                icon_color= "#717171"
                            ),
                            height= 70,
                            width= 70,
                            alignment= flet.alignment.center,
                            padding= flet.padding.only(right= 10)
                        ),
                        flet.Container(
                            flet.IconButton(
                                flet.Icons.SETTINGS,
                                icon_size= 40,
                                icon_color= "#717171",
                                on_click= lambda _: self.page.go("/settings")
                            ),
                            height= 70,
                            width= 70,
                            alignment= flet.alignment.center,
                            padding= flet.padding.only(right= 10)
                        )
                    ],
                    spacing= 30,
                    run_spacing= 30,
                    vertical_alignment= flet.VerticalAlignment.CENTER
                )
            ),
            controls= [
                flet.Container(
                    image= flet.DecorationImage(
                        src= "assets/bghome.png", 
                        fit= flet.ImageFit.COVER, 
                        filter_quality= flet.FilterQuality.HIGH, 
                        repeat= flet.ImageRepeat.NO_REPEAT
                    ), 
                    expand_loose= True,
                    expand= True
                )
            ],
            padding= 0
        )
    
    def external_button_hover(self, event) -> None:

        event.control.bgcolor = "#4a4a4a" if event.control.bgcolor == "#272727" else "#272727"
        event.control.update()
