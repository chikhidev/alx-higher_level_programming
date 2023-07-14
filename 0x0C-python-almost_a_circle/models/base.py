class Base:
    """
    Base model
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The id value for the instance. If provided, the instance's id
                will be set to the given value. If not provided, the instance's id
                will be automatically generated.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
