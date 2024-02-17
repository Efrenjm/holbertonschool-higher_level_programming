class Student:
    """Represents a student with name, surname, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the student to a dictionary representation,
        optionally including specific attributes.

        Args:
            attrs (list of str, optional): A list of attribute names
            to include in the dictionary. If None, all attributes are
            included. Defaults to None.

        Returns:
            dict: A dictionary representing the student, containing
            the specified attributes.
        """

        student = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

        if attrs is not None:
            student = {attr: student[attr] for attr in attrs
                       if attr in student}

        return student
