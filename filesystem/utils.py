import os
import flet
import platform
import minecraft_launcher_lib

from functools import lru_cache
from typing import List
from handler.exceptions import handle_exceptions

@handle_exceptions
@lru_cache(maxsize= 16)
def GetHome() -> str:

    HomePath: str | None = os.environ.get("APPDATA") if platform.system() == "Windows" else os.environ.get("HOME")

    if HomePath is None:
        raise RuntimeError("Unable to get NoxLauncher base folder.")

    NoxLauncherBasePath: str = f"{HomePath}/NoxLauncher"

    if not os.path.exists(NoxLauncherBasePath): os.makedirs(NoxLauncherBasePath)
    
    return NoxLauncherBasePath

@handle_exceptions
@lru_cache(maxsize= 16)
def GetFolderMods() -> str:

    NoxLauncherModsPath: str = f"{GetHome()}/mods"

    if not os.path.exists(NoxLauncherModsPath): os.makedirs(NoxLauncherModsPath)
    
    return NoxLauncherModsPath

@handle_exceptions
@lru_cache(maxsize= 16)
def GetFolderVersions() -> str:

    NoxLauncherModsPath: str = f"{GetHome()}/versions"

    if not os.path.exists(NoxLauncherModsPath): os.makedirs(NoxLauncherModsPath)
    
    return NoxLauncherModsPath

@handle_exceptions
def GetReleaseMinecraftVersions() -> List[flet.dropdown.Option]: 

    installed_versions: List[str] = [version for version in os.listdir(GetFolderVersions()) if os.path.isdir(version)]

    vanilla_releases: List[str] = [vanilla_version["id"] for vanilla_version in minecraft_launcher_lib.utils.get_version_list() if vanilla_version["type"] == "release"]

    versions: List[flet.dropdown.Option] = []

    for installed in installed_versions:
        versions.append(
            flet.dropdown.Option(
                key= f"{GetFolderVersions}/{installed}",
                text= installed,
                style= flet.ButtonStyle(
                    text_style= flet.TextStyle(
                        font_family= "NoxLauncher",
                        color= "#FFFFFF"
                    )
                ),
                icon= flet.Image(
                    src= "assets/icon.png",
                    width= 40,
                    height= 30,
                    filter_quality= flet.FilterQuality.LOW
                )
            )
        )

    for vanilla_version in vanilla_releases:

        if vanilla_version not in installed_versions:

            versions.append(
                flet.dropdown.Option(
                    key= f"INSTALL VANILLA VERSION: {vanilla_version}",
                    text= vanilla_version,
                    style= flet.ButtonStyle(
                        text_style= flet.TextStyle(
                            font_family= "NoxLauncher",
                            color= "#FFFFFF"
                        )
                    ),
                    leading_icon= flet.Image(
                        src= "assets/vanilla_version.png",
                        width= 40,
                        height= 30,
                        filter_quality= flet.FilterQuality.LOW
                    ),
                )
            )

    return versions