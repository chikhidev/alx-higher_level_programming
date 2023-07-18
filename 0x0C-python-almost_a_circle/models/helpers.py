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
        if type(value) is not int:
            raise TypeError(f"{prop_name} must be an integer")
        if value <= 0 and (prop_name == 'width' or prop_name == 'height'):
            raise ValueError(f"{prop_name} must be > 0")
        if value < 0 and (prop_name == 'x' or prop_name == 'y'):
            raise ValueError(f"{prop_name} must be >= 0")