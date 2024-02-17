import json


def from_json_string(my_str):
    """
    Convierte una cadena JSON a un objeto de Python.

    Args:
        my_str: La cadena JSON a convertir.

    Returns:
        El objeto de Python representado por la cadena JSON.
    """

    if not my_str:
        return None
    return json.loads(my_str)
