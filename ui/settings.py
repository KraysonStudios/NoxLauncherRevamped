import flet
import webbrowser

class SettingsView:

    def __init__(self, page: flet.Page) -> None:
        self.page: flet.Page = page
        self.build_ui()

    def build_ui(self) -> flet.View:

        return flet.View(
            "/home",
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
                    flet.Row(
                        controls= [
                            flet.Column(
                                controls= [
                                    flet.Container(
                                        flet.Column(
                                            controls= [
                                                flet.Container(
                                                    flet.Row(
                                                        controls= [
                                                            flet.Image(
                                                                src= "assets/icon.png",
                                                                width= 100,
                                                                height= 70,
                                                                repeat= flet.ImageRepeat.NO_REPEAT,
                                                                filter_quality= flet.FilterQuality.HIGH
                                                            ),
                                                            flet.Text(
                                                                "NoxLauncher",
                                                                font_family= "NoxLauncher",
                                                                size= 25,
                                                                color= "#FFFFFF"
                                                            )
                                                        ],
                                                        alignment= flet.MainAxisAlignment.CENTER,
                                                        vertical_alignment= flet.VerticalAlignment.CENTER,
                                                        spacing= 25,
                                                        run_spacing= 25
                                                    ),
                                                    alignment= flet.alignment.center,
                                                    expand_loose= True,
                                                    height= 100
                                                ),
                                                flet.Container(
                                                    flet.Row(
                                                        controls= [
                                                            flet.Switch(
                                                                active_color= "#148b47",
                                                                inactive_thumb_color= "#717171"
                                                            ),
                                                            flet.Text(
                                                                "Desactivar o activar el autocerrado.",
                                                                size= 13,
                                                                font_family= "NoxLauncher",
                                                                color= "#FFFFFF"
                                                            )
                                                        ],
                                                        alignment= flet.MainAxisAlignment.START,
                                                        run_spacing= 15,
                                                        spacing= 15
                                                    ),
                                                    expand_loose= True,
                                                    alignment= flet.alignment.center,
                                                    padding= flet.padding.only(left= 10),
                                                    height= 50
                                                ),
                                                flet.Container(
                                                    flet.Row(
                                                        controls= [
                                                            flet.Switch(
                                                                active_color= "#148b47",
                                                                inactive_thumb_color= "#717171"
                                                            ),
                                                            flet.Text(
                                                                spans= [
                                                                    flet.TextSpan(
                                                                        "Desactivar o activar ",
                                                                        style= flet.TextStyle(
                                                                            font_family= "NoxLauncher",
                                                                            size= 13,
                                                                            color= "#FFFFFF",
                                                                        )
                                                                    ),
                                                                    flet.TextSpan(
                                                                        "DiscordRPC",
                                                                        style= flet.TextStyle(
                                                                            font_family= "NoxLauncher",
                                                                            weight= flet.FontWeight.BOLD,
                                                                            size= 14,
                                                                            color= "#148b47",
                                                                            decoration= flet.TextDecoration.UNDERLINE,
                                                                            decoration_color= "#148b47",
                                                                            decoration_style= flet.TextDecorationStyle.SOLID
                                                                        )
                                                                    ),
                                                                    flet.TextSpan(
                                                                        ".",
                                                                        style= flet.TextStyle(
                                                                            font_family= "NoxLauncher",
                                                                            size= 13,
                                                                            color= "#FFFFFF",
                                                                        )
                                                                    ),
                                                                ]
                                                            )
                                                        ],
                                                        alignment= flet.MainAxisAlignment.START,
                                                        run_spacing= 15,
                                                        spacing= 15
                                                    ),
                                                    expand_loose= True,
                                                    alignment= flet.alignment.center,
                                                    padding= flet.padding.only(left= 10),
                                                    height= 50
                                                ),
                                            ],
                                            horizontal_alignment= flet.CrossAxisAlignment.START,
                                            spacing= 0,
                                            run_spacing= 0
                                        ),
                                        width= 500,
                                        height= 240,
                                        bgcolor= "#272727",
                                        border_radius= 10
                                    ),
                                ],
                                alignment= flet.MainAxisAlignment.CENTER,
                                horizontal_alignment= flet.CrossAxisAlignment.CENTER
                            ),
                            flet.Column(
                                controls= [
                                    flet.Container(
                                        flet.Column(
                                            controls= [
                                                flet.Container(
                                                    flet.Row(
                                                        controls= [
                                                            flet.Image(
                                                                src= "assets/java.png",
                                                                width= 100,
                                                                height= 70,
                                                                repeat= flet.ImageRepeat.NO_REPEAT,
                                                                filter_quality= flet.FilterQuality.HIGH
                                                            ),
                                                            flet.Text(
                                                                "Java",
                                                                font_family= "NoxLauncher",
                                                                size= 30,
                                                                color= "#FFFFFF"
                                                            )
                                                        ],
                                                        alignment= flet.MainAxisAlignment.CENTER,
                                                        vertical_alignment= flet.VerticalAlignment.CENTER,
                                                        spacing= 15,
                                                        run_spacing= 15
                                                    ),
                                                    alignment= flet.alignment.center,
                                                    expand_loose= True,
                                                    height= 100
                                                ),
                                                flet.Container(
                                                    flet.Text(
                                                        "Localización de Java",
                                                        size= 15,
                                                        font_family= "NoxLauncher",
                                                        color= "#FFFFFF"
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 50
                                                ),
                                                flet.Container(
                                                    flet.Dropdown(
                                                        hint_text= "Java",
                                                        options= [], 
                                                        border_color= "#717171",
                                                        border_width= 2, 
                                                        border_radius= 10, 
                                                        label_style= flet.TextStyle(
                                                            font_family= "NoxLauncher",
                                                            color= "#148b47"
                                                        ),
                                                        hint_style= flet.TextStyle(
                                                            font_family= "NoxLauncher",
                                                            color= "#FFFFFF"
                                                        ),
                                                        width= 300
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20, right= 20, bottom= 30),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.Text(
                                                        "Java Virtual Machine (Argumentos)",
                                                        size= 15,
                                                        font_family= "NoxLauncher",
                                                        color= "#FFFFFF"
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 50
                                                ),
                                                flet.Container(
                                                    flet.Row(
                                                        controls= [
                                                            flet.TextField(
                                                                multiline= False, 
                                                                width= 300, 
                                                                height= 70, 
                                                                border_radius= 10, 
                                                                border_color= "#717171", 
                                                                border_width= 2, 
                                                                label= "JVM Args", 
                                                                hint_text= "Ejemplo: -Xms1G -Xmx2G",
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
                                                                    color= "#148b47"
                                                                ),
                                                            ),
                                                            flet.Container(
                                                                flet.FilledButton(
                                                                    icon= flet.Icons.UPDATE,
                                                                    icon_color= "#FFFFFF",
                                                                    text= "Actualizar",
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
                                                                ),
                                                                alignment= flet.alignment.center,
                                                                padding= flet.padding.only(bottom= 20)
                                                            ),
                                                        ],
                                                        expand_loose= True,
                                                        height= 70,
                                                        spacing= 15,
                                                        run_spacing= 15
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.Text(
                                                        "Memoria dedicada (RAM)",
                                                        size= 15,
                                                        font_family= "NoxLauncher",
                                                        color= "#FFFFFF"
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 50
                                                ),
                                                flet.Container(
                                                    flet.Slider(
                                                        active_color= "#148b47",
                                                        thumb_color= "#717171",
                                                        height= 40,
                                                        expand_loose= True
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20, right= 20),
                                                    expand_loose= True,
                                                    height= 40
                                                ),
                                            ],
                                            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                                            spacing= 0,
                                            run_spacing= 0
                                        ),
                                        width= 500,
                                        height= 470,
                                        bgcolor= "#272727",
                                        border_radius= 10
                                    ),
                                ],
                                alignment= flet.MainAxisAlignment.CENTER,
                                horizontal_alignment= flet.CrossAxisAlignment.CENTER
                            )
                        ],
                        alignment= flet.MainAxisAlignment.CENTER,
                        vertical_alignment= flet.VerticalAlignment.CENTER,
                        spacing= 80,
                        run_spacing= 80
                    ),
                    image= flet.DecorationImage(
                        src= "assets/bgsettings.png", 
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
