class CustomFloat():
    def __init__(self, specification):
        """Creates a custom floating point number

        Arguments:
        specification -- the floating point specification that this number complies with
        """
        self.specification = specification
        
        if specification.sign:
            self.sign = 0b0

        if specification.exponent > 0:
            self.exponent = 0b0

        self.mantissa = 0b0

class FloatSpecification():
    __slots__ = ('sign', 'exponent', 'mantissa', 'special_values', 'bias')

    def __init__(self, exponent, mantissa, sign=True, special_values=True):
        """Creates a floating point specification

        Arguments:
        exponent -- The number of exponent bits (int)
        mantissa -- The number of mantissa bits (int)
        
        Keyword Arguments:
        sign -- Determines if the number has a sign bit (default=True)
        special_values -- Determines if infinite and nan values can be represented (default=True)
        """
        self.sign = sign
        self.exponent = exponent
        self.mantissa = mantissa
        self.special_values = special_values

        if exponent > 1:
            self.bias = 2 ** (exponent - 1) - 1
        else:
            self.bias = 0

    def getMaxValue(self):
        if self.exponent > 0 and self.special_values:
            """
            Creates a value equivalent with a 1 to the left of the decimal and 
            mantissa 1's to the right of the decimal. This is then shifted to 
            the left bias times. The bias is one less than the max value of the
            exponent and is used because all 1's in the exponent represents a 
            special value.
            """
            return (2 - 2 ** (-1 * self.mantissa)) * 2 ** self.bias
        elif self.exponent > 0:
            """
            Does the same process as above except the final shift is increased
            by 1 because there are no special values.
            """
            return (2 - 2 ** (-1 * (self.mantissa))) * 2 ** (self.bias + 1)
        else:
            """
            There is no exponent so treat this like a normal binary number.
            """
            return (2 ** self.mantissa) - 1

IEEE_SINGLE_PRECISION = FloatSpecification(8, 23)
IEEE_DOUBLE_PRECISION = FloatSpecification(11, 52)
