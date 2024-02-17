def class_to_json(obj):
    """
    Convierte un objeto de clase a un diccionario serializable en JSON.

    Args:
        obj: La instancia de la clase a convertir.

    Returns:
        Un diccionario que representa el objeto de clase.
    """

    # Diccionario vacío para almacenar la representación del objeto
    result = {}

    # Recorrer los atributos del objeto
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            result[attr_name] = attr_value
        else:
            pass

    return result
