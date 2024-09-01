import json
from pathlib import Path
from typing import Any

from lionagi import lionfuncs as ln
from lionagi.os import Converter, SysUtil
from lionagi.os.primitives.core_types import Component


class JsonConverter(Converter):
    _object = "json"

    @classmethod
    def convert_obj_to_sub_dict(cls, object_: str, **kwargs: Any) -> dict:
        kwargs["str_type"] = "json"
        return ln.to_dict(object_, **kwargs)

    @classmethod
    def convert_sub_to_obj_dict(cls, subject: Component, **kwargs: Any) -> dict:
        return ln.to_dict(subject, **kwargs)

    @classmethod
    def to_obj(
        cls,
        subject: Component,
        *,
        convert_kwargs: dict = {},
        **kwargs: Any,
    ) -> Any:
        return ln.to_str(
            subject, serialize_as="json", parser_kwargs=convert_kwargs, **kwargs
        )


class JsonFileConverter(Converter):
    _object = "json_file"

    @classmethod
    def convert_obj_to_sub_dict(cls, object_: str | Path, **kwargs: Any) -> dict:
        object_ = json.load(object_)
        return ln.to_dict(object_, **kwargs)

    @classmethod
    def convert_sub_to_obj_dict(cls, subject: Component, **kwargs: Any) -> dict:
        return ln.to_dict(subject, **kwargs)

    @classmethod
    def to_obj(
        cls,
        subject: Component,
        persist_path: str | Path,
        path_kwargs: dict = {},
        **kwargs: Any,
    ) -> Any:
        text = JsonConverter.to_obj(subject, **kwargs)
        path_kwargs = SysUtil._get_path_kwargs(
            persist_path=persist_path,
            postfix="json",
            **path_kwargs,
        )
        SysUtil.save_to_file(text=text, **path_kwargs)
