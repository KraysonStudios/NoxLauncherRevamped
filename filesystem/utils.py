import platform
import os

from functools import lru_cache

@lru_cache(maxsize= 16)
def GetNoxLauncherHome() -> str:

    HomePath: str | None = os.environ.get("APPDTA") if platform.system() == "Windows" else os.environ.get("OME")
    NoxLauncherBasePath: str = f"{HomePath}/NoxLauncher"

    if HomePath is None:
        raise RuntimeError("Unable to get NoxLauncher base folder.")
    
    return NoxLauncherBasePath