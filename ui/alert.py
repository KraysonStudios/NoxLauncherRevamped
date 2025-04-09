import flet

class ErrorAlert:

    def __init__(self, page: flet.Page, bgcolor: str = "#272727", description: str = "") -> None:

        self.page: flet.Page = page

        self.bgcolor: str = bgcolor
        self.description: str = description

    def build(self) -> flet.AlertDialog:

        error_alert: flet.AlertDialog = flet.AlertDialog(
            modal= True,
            title= flet.Container(
                flet.Image(
                    src= "assets/error.png",
                    width= 90,
                    height= 90,
                ),
                expand_loose= True,
                alignment= flet.alignment.center
            ),
            content= flet.Text(
                self.description,
                font_family= "NoxLauncher",
                size= 14,
                color= "#FFFFFF"
            ),
            bgcolor= self.bgcolor,
            actions_alignment= flet.MainAxisAlignment.END,
            actions= [
                flet.FilledButton(
                    text= "Ok",
                    color= "#FFFFFF",
                    bgcolor= "#148b47",
                    width= 100,
                    height= 45,
                    style= flet.ButtonStyle(
                        shape= flet.RoundedRectangleBorder(radius= 5),
                        text_style= flet.TextStyle(
                            font_family= "NoxLauncher"
                        )
                    ),
                    on_click= lambda _: self.page.close(error_alert),
                ),
            ]
        )

        return error_alert