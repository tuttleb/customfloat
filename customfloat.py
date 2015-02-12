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
    __slots__ = ('sign', 'exponent', 'mantissa', 'positive_infinity', 'negative_infinity', 'nan', 'bias')

    def __init__(self, exponent, mantissa, sign=True, infinite_values=True, nan=True):
        """Creates a floating point specification

        Arguments:
        exponent -- The number of exponent bits (int)
        mantissa -- The number of mantissa bits (int)
        
        Keyword Arguments:
        sign -- Determines if the number has a sign bit (default=True)
        infinite_values -- Determines if infinite values can be represented (default=True)
        nan -- Determines if Not a Number (NaN) values can be represented (default=True)
        """
        self.sign = sign
        self.exponent = exponent
        self.mantissa = mantissa
        self.nan = nan

        if sign and infinite_values:
            self.negative_infinity = True
        if infinite_values:
            self.positive_infinity = True

        if sign and exponent > 1:
            self.bias = 2 ** (exponent - 1) - 1
        else:
            self.bias = 0

    def getMaxValue(self):
        #TODO: deal with infinities
        max_val = (2 ** (self.mantissa + 1)) - 1
        print("max: " + str(max_val))

        if self.nan:
            #decrease by one because all ones represents nan
            max_val -= 1

        if self.exponent > 0:
            max_val <<= (2 ** self.exponent) - self.bias - self.mantissa - 2

        return max_val

IEEE_SINGLE_PRECISION = FloatSpecification(8, 23)
IEEE_DOUBLE_PRECISION = FloatSpecification(11, 52)
