from typing import Callable, Any
from functools import wraps

def handle_exceptions(func: Callable[[Any], Any]) -> None: 

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable[[Any], Any] | None:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return None
        
    return wrapper