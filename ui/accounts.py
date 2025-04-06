import flet
import webbrowser

class AccountView:

    def __init__(self, page: flet.Page) -> None:
        
        self.page: flet.Page = page

    def build_ui(self) -> flet.View:

        return flet.View(
            "/accounts",
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
                        on_click= lambda _: self.page.go("/home"),
                    ),
                    alignment= flet.alignment.center,
                    padding= flet.padding.only(left= 20),
                    on_hover= lambda _: None
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
                                    bgcolor= "#272727",
                                    border_radius= 10,
                                    on_hover= self.external_button_hover
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
                                    bgcolor= "#272727",
                                    border_radius= 10,
                                    on_hover= self.external_button_hover
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
                                [
                                    flet.Container(
                                        flet.Column(
                                            [
                                                flet.Row(
                                                    [
                                                        flet.Image(
                                                            src= "assets/icon.png",
                                                            width= 100,
                                                            height= 70,
                                                            repeat= flet.ImageRepeat.NO_REPEAT,
                                                            filter_quality= flet.FilterQuality.HIGH
                                                        ),
                                                        flet.Text(
                                                            "No Premiun",
                                                            font_family= "NoxLauncher",
                                                            size= 25,
                                                            color= "#FFFFFF"
                                                        )
                                                    ],
                                                    alignment= flet.MainAxisAlignment.CENTER,
                                                    expand_loose= True,
                                                    height= 100,
                                                    run_spacing= 20,
                                                    spacing= 20
                                                ),
                                                flet.Container(
                                                    flet.Text(
                                                        spans= [
                                                            flet.TextSpan(
                                                                "Ely.by",
                                                                style= flet.TextStyle(
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#FFFFFF"
                                                                )
                                                            ),
                                                            flet.TextSpan(
                                                                "  -  ",
                                                                style= flet.TextStyle(
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#FFFFFF"
                                                                )
                                                            ),
                                                            flet.TextSpan(
                                                                "https://ely.by",
                                                                style= flet.TextStyle(
                                                                    decoration= flet.TextDecoration.UNDERLINE,
                                                                    weight= flet.FontWeight.BOLD,
                                                                    decoration_thickness= 2,
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#148b47"
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 40
                                                ),
                                                flet.Container(
                                                    flet.TextField(
                                                        multiline= False, 
                                                        width= 350, 
                                                        height= 70, 
                                                        border_radius= 10, 
                                                        border_color= "#717171", 
                                                        border_width= 2, 
                                                        label= "Email", 
                                                        hint_text= "Ejemplo: miemail@gmail.com",
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
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.TextField(
                                                        multiline= False, 
                                                        width= 350, 
                                                        height= 70, 
                                                        password= True,
                                                        can_reveal_password= True,
                                                        border_radius= 10, 
                                                        border_color= "#717171", 
                                                        border_width= 2, 
                                                        label= "Contraseña", 
                                                        hint_text= "Ejemplo: dahellllll2025",
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
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.FilledButton(
                                                        icon= flet.Icons.LOGIN,
                                                        icon_color= "#FFFFFF",
                                                        text= "Iniciar Sesión",
                                                        color= "#FFFFFF",
                                                        bgcolor= "#148b47",
                                                        width= 200,
                                                        height= 45,
                                                        style= flet.ButtonStyle(
                                                            shape= flet.RoundedRectangleBorder(radius= 5),
                                                            text_style= flet.TextStyle(
                                                                font_family= "NoxLauncher"
                                                            )
                                                        ),
                                                    ),
                                                    expand_loose= True,
                                                    alignment= flet.alignment.center
                                                )
                                            ],
                                            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                                            expand= True,
                                            expand_loose= True
                                        ),
                                        bgcolor= "#272727",
                                        width= 400,
                                        height= 400,
                                        border_radius= 10
                                    )
                                ],
                                expand= True,
                                expand_loose= True,
                                alignment= flet.MainAxisAlignment.CENTER,
                            ),
                            flet.Column(
                                [
                                    flet.Container(
                                        flet.Row(
                                            [
                                                flet.Text(
                                                    "No Premiun",
                                                    font_family= "NoxLauncher",
                                                    size= 16
                                                ),
                                                flet.Switch(
                                                    active_color= "#148b47",
                                                    inactive_thumb_color= "#717171"
                                                ),
                                                flet.Text(
                                                    "Premiun",
                                                    font_family= "NoxLauncher",
                                                    size= 16
                                                ),
                                            ],
                                            expand= True,
                                            expand_loose= True,
                                            alignment= flet.MainAxisAlignment.CENTER,
                                            spacing= 20,
                                            run_spacing= 20
                                        ),
                                        height= 100,
                                        width= 350,
                                        alignment= flet.alignment.center,
                                        bgcolor= "#272727",
                                        border_radius= 20,
                                        border= flet.border.all(2, "#717171")
                                    )
                                ],
                                width= 350,
                                expand= True,
                                alignment= flet.MainAxisAlignment.CENTER,
                                horizontal_alignment= flet.CrossAxisAlignment.CENTER
                            ),
                            flet.Column(
                                [
                                    flet.Container(
                                        flet.Column(
                                            [
                                                flet.Row(
                                                    [
                                                        flet.Image(
                                                            src= "assets/mojang.png",
                                                            width= 100,
                                                            height= 70,
                                                            repeat= flet.ImageRepeat.NO_REPEAT,
                                                            filter_quality= flet.FilterQuality.HIGH
                                                        ),
                                                        flet.Text(
                                                            "Premiun",
                                                            font_family= "NoxLauncher",
                                                            size= 25,
                                                            color= "#FFFFFF"
                                                        )
                                                    ],
                                                    alignment= flet.MainAxisAlignment.CENTER,
                                                    expand_loose= True,
                                                    height= 100,
                                                    run_spacing= 20,
                                                    spacing= 20
                                                ),
                                                flet.Container(
                                                    flet.Text(
                                                        spans= [
                                                            flet.TextSpan(
                                                                "Microsoft",
                                                                style= flet.TextStyle(
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#FFFFFF"
                                                                )
                                                            ),
                                                            flet.TextSpan(
                                                                "  -  ",
                                                                style= flet.TextStyle(
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#FFFFFF"
                                                                )
                                                            ),
                                                            flet.TextSpan(
                                                                "https://minecraft.net",
                                                                style= flet.TextStyle(
                                                                    decoration= flet.TextDecoration.UNDERLINE,
                                                                    weight= flet.FontWeight.BOLD,
                                                                    decoration_thickness= 2,
                                                                    size= 14,
                                                                    font_family= "NoxLauncher",
                                                                    color= "#148b47"
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 40
                                                ),
                                                flet.Container(
                                                    flet.TextField(
                                                        multiline= False, 
                                                        width= 350, 
                                                        height= 70, 
                                                        border_radius= 10, 
                                                        border_color= "#717171", 
                                                        border_width= 2, 
                                                        label= "Email", 
                                                        hint_text= "Ejemplo: miemail@gmail.com",
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
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.TextField(
                                                        multiline= False, 
                                                        width= 350, 
                                                        height= 70, 
                                                        password= True,
                                                        can_reveal_password= True,
                                                        border_radius= 10, 
                                                        border_color= "#717171", 
                                                        border_width= 2, 
                                                        label= "Contraseña", 
                                                        hint_text= "Ejemplo: dahellllll2025",
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
                                                    alignment= flet.alignment.center_left,
                                                    padding= flet.padding.only(left= 20),
                                                    expand_loose= True,
                                                    height= 70
                                                ),
                                                flet.Container(
                                                    flet.FilledButton(
                                                        icon= flet.Icons.LOGIN,
                                                        icon_color= "#FFFFFF",
                                                        text= "Iniciar Sesión",
                                                        color= "#FFFFFF",
                                                        bgcolor= "#148b47",
                                                        width= 200,
                                                        height= 45,
                                                        style= flet.ButtonStyle(
                                                            shape= flet.RoundedRectangleBorder(radius= 5),
                                                            text_style= flet.TextStyle(
                                                                font_family= "NoxLauncher"
                                                            )
                                                        ),
                                                    ),
                                                    expand_loose= True,
                                                    alignment= flet.alignment.center
                                                )
                                            ],
                                            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                                            expand= True,
                                            expand_loose= True
                                        ),
                                        bgcolor= "#272727",
                                        width= 400,
                                        height= 400,
                                        border_radius= 10
                                    )
                                ],
                                expand= True,
                                expand_loose= True,
                                alignment= flet.MainAxisAlignment.CENTER,
                            )
                        ],
                        alignment= flet.MainAxisAlignment.CENTER,
                        spacing= 20,
                        run_spacing= 20
                    ),
                    image= flet.DecorationImage(
                        src= "assets/bgaccounts.png", 
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
    
    def on_bg_completed(self, event: flet.ControlEvent) -> None:

        event.control.play()
        event.control.update()

    def external_button_hover(self, event: flet.ControlEvent) -> None:

        event.control.bgcolor = "#4a4a4a" if event.control.bgcolor == "#272727" else "#272727"
        event.control.update()