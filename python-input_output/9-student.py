class Student:
    """
    Representa a un estudiante con nombre, apellido y edad.
    """

    def __init__(self, first_name, last_name, age):
        """
        Inicializa un nuevo estudiante.

        Args:
          first_name: El nombre del estudiante.
          last_name: El apellido del estudiante.
          age: La edad del estudiante.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convierte el estudiante a un diccionario serializable en JSON.

        Returns:
          Un diccionario que representa al estudiante.
        """

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
