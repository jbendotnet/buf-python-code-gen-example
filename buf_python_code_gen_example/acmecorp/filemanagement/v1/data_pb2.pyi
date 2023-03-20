from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["name", "size", "mime_type", "extension"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    mime_type: str
    extension: str
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., mime_type: _Optional[str] = ..., extension: _Optional[str] = ...) -> None: ...
