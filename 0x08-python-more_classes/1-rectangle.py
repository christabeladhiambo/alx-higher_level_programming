"""
class Rectangle:
"""
Create a new rectangle
"""
def __init__(self, width=0, height=0):
"""
Init thArgs:

							            self: The self classes

								                width (int): The width

											                 height (int): The height

														               Raises:

															                   Raises about the setter function

																	           Returns: Anything

																		           """

																			           self.width = width

																				           self.height = height



																					       @property

																					           def height(self):

																							           """

																								           Give the height

																									           Args:

																										               self: The self classes

																											               Return: The value of of height

																												               """

																													               return self.__height



																														           @height.setter

																															       def height(self, value):

																																               """

																																	               Set the height

																																		               Args:

																																			                   self: The self classes

																																					               value (int): The value to fill

																																								            Raises:

																																									                TypeError: If the height is not an int

																																											            ValueError: If the height is less than 0

																																												            Return: Anything

																																													            """

																																														            if type(value) is not int:

																																															                raise TypeError('height must be an integer')

																																																	        if value < 0:

																																																		            raise ValueError('height must be >= 0')

																																																			            self.__height = value



																																																				        @property

																																																					    def width(self):

																																																						            """

																																																							            Give the width

																																																								            Args:

																																																									                self: The self classes

																																																											        Return: The value of of width

																																																												        """

																																																													        return self.__width



																																																														    @width.setter

																																																														        def width(self, value):

																																																																        """

																																																																	        Set the width

																																																																		        Args:

																																																																			            self: The self classes

																																																																				                value (int): The value to fill

																																																																							             Raises:

																																																																								                 TypeError: If the width is not an int

																																																																										             ValueError: If the width is less than 0

																																																																											             Return: Anything

																																																																												             """

																																																																													             if type(value) is not int:

																																																																														                 raise TypeError('width must be an integer')

																																																																																         if value < 0:

																																																																																	             raise ValueError('width must be >= 0')

																																																																																		             self.__width = value
