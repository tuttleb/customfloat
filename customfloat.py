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
   
    def getValue(self, precise=True):
        """Returns a string representation of this value in base 10

        precise -- Determines if the numbers above and below should be used to
            help determine value. Should be left alone to avoid getting to much
            precision. (Defualt: True)
        """
        val = (1 + self.mantissa * 2 ** (-1 * self.specification.mantissa)) * \
                2 ** (self.exponent - self.specification.bias)
        if self.sign and self.sign == 1:
            val *= -1

        if not precise:
            return str(val)


        #TODO: Deal with values of zero and mantissa maxed out
        if self.mantissa < 2 ** self.specification.mantissa - 1:
            pass

        if self.mantissa > 0:
            pass

        #Create the numbers directly above and below the current number
        numAbove = CustomFloat(self.specification, sign=self.sign, exponent=self.exponent, mantissa=self.mantissa + 1)
        numBelow = CustomFloat(self.specification, sign=self.sign, exponent=self.exponent, mantissa=self.mantissa - 1)

        numAbove_str = str(numAbove.getValue(precise=False))
        numBelow_str = str(numBelow.getValue(precise=False))
        val_str = str(val)

        print(numAbove_str)
        print(val_str)
        print(numBelow_str)

        max_length = max([len(numAbove_str), len(numBelow_str), len(val_str)])
        
        #Add zeroes on the end so they are all the same length
        numAbove_str = numAbove_str.ljust(max_length, '0')
        numBelow_str = numBelow_str.ljust(max_length, '0')
        val_str = val_str.ljust(max_length, '0')

        index = 0

        #Find the last index where all values are the same
        #In need of a better solution
        for i in range(max_length):
            print(val_str[i])
            if val_str[i] != '.' and val_str[i] != '-' and val_str[i] != 'e':
                above = int(numAbove_str[i])
                current = int(val_str[i])
                below = int(val_str[i])

                if above == current == below:
                    index = i
                else:
                    break

        #This does not work because the numbers need to be rounded up first.
        if int(numAbove_str[index+1]) != int(val_str[index+1]) + 1 or int(val_str[index+1]) != int(val_str[index+1]) + 1:
            return val_str[:index+1]

        #The value after the last shared index is the last included digit
        val_after_change = int(val_str[index+1])
        #TODO: Deal with carrying digits
        #Round up if necessary
        if int(val_str[index+2]) >= 5:
            val_after_change += 1


        val_str = val_str[:index+1] + str(val_after_change)

        return val_str

    def _isInt(self, i):
        try:
            int(i)
            return True
        except ValueError:
            return False

    def _strToNumList(self, num_str):
        return [int(i) if self._isInt(i) else i for i in num_str]

    def _roundUpNumArray(self, num_list):
        #TODO: Check if the number should be rounded?
        carry = 1
        for i in range(len(num_list)-1, -1, -1):
            if not self._isInt(num_list[i]):
                continue
            else:
                num = int(num_list[i])
                



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
