class CustomFloat():
    def __init__(self, specification, **kwargs):
        """Creates a custom floating point number

        Arguments:
        specification -- The floating point specification that this number 
            complies with

        Key Word Arguments:
        sign -- The bit value of the sign bit if the number has a sign bit. 0 
            for positive, 1 for negative (Default 0).
        exponent -- The bit value of the exponent if the number has exponent 
            bits. Inputs must be between 0 and 2^n - 1 where n is the number of
            exponent bits (Default: A value that when adjusted for the bias will
            result in 0)
        mantissa -- The bit value of the mantissa. Do not include a leading 1
            for normalized numbers (Default 0).
        """
        self.specification = specification
        
        if specification.sign and kwargs['sign']:
            self.sign = kwargs['sign']
        elif specification.sign:
            self.sign = 0

        if specification.exponent > 0 and kwargs['exponent']:
            self.exponent = kwargs['exponent']
        elif specification.exponent > 0:
            self.exponent = specification.bias

        if kwargs['mantissa']:
            self.mantissa = kwargs['mantissa']
        else:
            self.mantissa = 0
   
    def getValue(self):
        val = (1 + self.mantissa * 2 ** (-1 * self.specification.mantissa)) * \
                2 ** (self.exponent - self.specification.bias)
        if self.sign and self.sign == 1:
            val *= -1

        return val

class FloatSpecification():
    __slots__ = ('sign', 'exponent', 'mantissa', 'special_values', 'bias')

    def __init__(self, exponent, mantissa, sign=True, special_values=True):
        #TODO: Account for denormalized special values
        """Creates a floating point specification

        Arguments:
        exponent -- The number of exponent bits (int)
        mantissa -- The number of mantissa bits (int)
        
        Keyword Arguments:
        sign -- Determines if the number has a sign bit (default=True)
        special_values -- Determines if infinite and nan values can be 
            represented (default=True)
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

    def getMinValue(self):
        if self.sign:
            return -1 * self.getMaxValue()
        else:
            return 0

    def getMinFraction(self):
        if self.exponent > 0:
            return
        else:
            return 0

IEEE_SINGLE_PRECISION = FloatSpecification(8, 23)
IEEE_DOUBLE_PRECISION = FloatSpecification(11, 52)
