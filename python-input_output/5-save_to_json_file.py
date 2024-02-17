import json


def save_to_json_file(my_obj, filename):
    """
    Guarda un objeto Python en un archivo de texto como JSON.

    Args:
        my_obj: El objeto Python a guardar.
        filename: El nombre del archivo de texto.
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file, indent=4)
