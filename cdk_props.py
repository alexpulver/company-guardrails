import importlib
from typing import Any, Dict, Optional, Sequence, cast


def merge(props: Sequence[Any], overrides: Optional[Any]) -> Any:
    merged_props_dict: Dict[str, Any] = {}
    overrides_props_dict = to_dict(overrides)

    _check_type_match(props, overrides)
    for index, props_obj in enumerate(props):
        props_dict = to_dict(props_obj)
        _check_conflicts(props_dict, index, merged_props_dict, overrides_props_dict)
        merged_props_dict.update(props_dict)
    merged_props_dict.update(overrides_props_dict)

    props_module_name = _get_module_name(props[0])
    props_class_name = _get_class_name(props[0])
    props_module = importlib.import_module(props_module_name)
    props_class = getattr(props_module, props_class_name)
    merged_props_obj = props_class(**merged_props_dict)
    return merged_props_obj


def to_dict(props: Any) -> Dict[str, Any]:
    if props is None:
        return {}
    return cast(Dict[str, Any], vars(props).copy()["_values"])


def _check_type_match(props: Any, overrides: Optional[Any]) -> None:
    if overrides is None:
        props_types = {type(props_obj) for props_obj in props}
    else:
        props_types = {type(props_obj) for props_obj in props + [overrides]}
    if len(props_types) > 1:
        raise ValueError(f"type mismatch between props: {props_types}")


def _check_conflicts(
    props_dict: Dict[str, Any],
    index: int,
    merged_props_dict: Dict[str, Any],
    overrides_props_dict: Dict[str, Any],
) -> None:
    for prop in props_dict:
        if (
            prop in merged_props_dict
            and props_dict[prop] != merged_props_dict[prop]
            and prop not in overrides_props_dict
        ):
            raise ValueError(
                f"Props object at index {index} includes '{prop}' prop with value "
                f"'{props_dict[prop]}'. It was defined by previous props object(s) "
                f"with value '{merged_props_dict[prop]}' and is not in overrides"
            )


def _get_module_name(props: Any) -> str:
    return type(props).__module__


def _get_class_name(props: Any) -> str:
    return type(props).__name__


def _get_absolute_name(module_name: str, class_name: str) -> str:
    return f"{module_name}.{class_name}"
