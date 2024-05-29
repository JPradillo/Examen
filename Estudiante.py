"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""

class Persona:
    """
    Clase persona con los campos apellidos, nombre y nif
    :return: Nombre apellidos y nif de la persona.
    """
    apellidos = "Apellidos"
    nombre = "Nombre"
    nif = "11111111Z"

class Estudiante(Persona):
    curso = "Primaria"

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Método contructor de la clase Estudiante que recibe una serie de parámetros.
        :param nif: NIF
        :param curso: Curso
        :param nombre: Nombre
        :param apellidos: Apellidos
        """
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """
        Propiedad de la clase estudiante que devuelve el NIF.
        :return: NIF
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Devuelve el nif que tenga el Estudiante.
        :param value: Valor que le quieras dar al nif.
        :return: Devuelve el valor dado.
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Propiedad de la clase estudiante que devuelve el NIF.
        :return: NIF
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Devuelve el curso al que va el Estudiante.
        :param value: Valor que le quieras dar al curso.
        :return: Devuelve el valor dado.
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Propiedad de la clase estudiante que devuelve el nombre.
        :return: Nombre
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Devuelve el nombre que tenga el Estudiante.
        :param value: Valor que le quieras dar al nombre.
        :return: Devuelve el valor dado.
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Propiedad de la clase estudiante que devuelve el apellidos.
        :return: Apellidos
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Devuelve los apellidos que tenga el Estudiante.
        :param value: Valor que le quieras dar a los apellidos.
        :return: Devuelve el valor dado.
        """
        self.__apellidos = value
