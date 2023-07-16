Base = __import__('models.base')

class Rectangle(Base):
    """Rectabgle inherits from Base class
    """
    def __init__(self, width, height, x, y, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(value))


    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.validate(width)
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width
        

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.validate(height)
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.validate(x)
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.validate(y)
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def id(self):
        return self.Base.id
    
    @id.setter
    def id(self, id):
        self.validate(id)
        self.Base.id = id


    def area(self):
        return self.__x * self.__y
    
    def display(self):
        if self.__x > 0 and self.__y > 0 :
            for i in range(0, self.__y):
                for j in range(0, self.__x):
                    print('#', end='')
                print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.Base.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width, 
                                                        self.__height
                                                        )