def validate_integer_property(value, prop_name):
        """
        Validate an integer property.

        Args:
            value (int): The value to be validated.
            prop_name (str): The name of the property for error messages.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{prop_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{prop_name} must be > 0")