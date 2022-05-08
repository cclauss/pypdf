"""Helpers for working with PDF types."""

from typing import List, Union

try:
    # Python 3.8+: https://peps.python.org/pep-0586
    from typing import Literal  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import Literal  # type: ignore[misc]

try:
    # Python 3.10+: https://www.python.org/dev/peps/pep-0484/
    from typing import TypeAlias  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import TypeAlias  # type: ignore[misc]

from PyPDF2.generic import (
    ArrayObject,
    Bookmark,
    Destination,
    NameObject,
    NullObject,
    NumberObject,
)

BorderArrayType: TypeAlias = List[Union[NameObject, NumberObject, ArrayObject]]
BookmarkTypes: TypeAlias = Union[Bookmark, Destination]
FitType: TypeAlias = Literal[
    "/Fit", "/XYZ", "/FitH", "/FitV", "/FitR", "/FitB", "/FitBH", "/FitBV"
]
# Those go with the FitType: They specify values for the fit
ZoomArgType: TypeAlias = Union[NumberObject, NullObject]
ZoomArgsType: TypeAlias = List[ZoomArgType]

# Recursive types are not yet supported by mypy:
#    OutlinesType = List[Union[Destination, "OutlinesType"]]
# See https://github.com/python/mypy/issues/731
# Hence use this for the moment:
OutlinesType = List[Union[Destination, List[Union[Destination, List[Destination]]]]]


LayoutType: TypeAlias = Literal[
    "/NoLayout",
    "/SinglePage",
    "/OneColumn",
    "/TwoColumnLeft",
    "/TwoColumnRight",
    "/TwoPageLeft",
    "/TwoPageRight",
]
PagemodeType: TypeAlias = Literal[
    "/UseNone",
    "/UseOutlines",
    "/UseThumbs",
    "/FullScreen",
    "/UseOC",
    "/UseAttachments",
]
