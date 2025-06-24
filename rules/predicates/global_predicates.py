from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from ..geometry_objects.construction_object import Construction
    from .implementations.macro_predicate import MacroData


_CONSTRUCTIONS: Optional[dict[str, 'Construction']] = {}
_MACROS: Optional[dict[str, 'MacroData']] = {}


def get_constructions() -> dict[str, 'Construction']:
    """
    TODO: Document
    """
    if _CONSTRUCTIONS == None:
        raise Exception(
            "_CONSTRUCTIONS has not yet been loaded. Did you remember to call `pred_config.load_constructions_and_macros`?"
        )
    return _CONSTRUCTIONS


def get_macros() -> dict[str, 'MacroData']:
    """
    TODO: Document
    """
    if _MACROS == None:
        raise Exception(
            "_MACROS has not yet been loaded. Did you remember to call `pred_config.load_constructions_and_macros`?"
        )
    return _MACROS
