import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_file(*args):
    """
    Agrega todos los argumentos a una lista de Python
    y los guarda en un archivo JSON.
    """

    items_list = load_from_json_file("add_item.json") or []
    items_list.extend(args)
    save_to_json_file(items_list, "add_item.json")
