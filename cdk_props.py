import importlib
from typing import Any, Dict, cast


def update(props: Any, other_props: Any) -> Any:
    props_module_name = _get_module_name(props)
    props_class_name = _get_class_name(props)
    props_absolute_name = _get_absolute_name(props_module_name, props_class_name)

    other_props_module_name = _get_module_name(other_props)
    other_props_class_name = _get_class_name(other_props)
    other_props_absolute_name = _get_absolute_name(
        other_props_module_name, other_props_class_name
    )

    # pylint: disable=unidiomatic-typecheck
    if type(props) != type(other_props):
        raise ValueError(
            f"type mismatch between props: "
            f"'{props_absolute_name}', '{other_props_absolute_name}'"
        )

    props_dict = to_dict(props)
    other_props_dict = to_dict(other_props)
    props_dict.update(other_props_dict)

    props_module = importlib.import_module(props_module_name)
    props_class = getattr(props_module, props_class_name)
    updated_props = props_class(**props_dict)
    return updated_props


def to_dict(props: Any) -> Dict[str, Any]:
    return cast(Dict[str, Any], vars(props).copy()["_values"])


def _get_module_name(props: Any) -> str:
    return type(props).__module__


def _get_class_name(props: Any) -> str:
    return type(props).__name__


def _get_absolute_name(module_name: str, class_name: str) -> str:
    return f"{module_name}.{class_name}"
