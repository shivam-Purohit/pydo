# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.0, generator: @autorest/python@6.0.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._client import GeneratedClient

try:
    from ._patch import __all__ as _patch_all
    from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
except ImportError:
    _patch_all = []
from ._patch import patch_sdk as _patch_sdk

__all__ = ["GeneratedClient"]
__all__.extend([p for p in _patch_all if p not in __all__])

_patch_sdk()
