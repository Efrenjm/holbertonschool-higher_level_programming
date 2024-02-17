import json


def load_from_json_file(filename):
    """
    Carga un objeto Python desde un archivo JSON.

    Args:
        filename: El nombre del archivo JSON.

    Returns:
        El objeto Python representado en el archivo JSON.
    """

    with open(filename, "r") as file:
        return json.load(file)
