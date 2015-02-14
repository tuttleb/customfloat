import unittest
import customfloat

class MaxValue(unittest.TestCase):

    def testIEEESingle(self):
        self.assertEqual(customfloat.IEEE_SINGLE_PRECISION.getMaxValue(), 340282346638528859811704183484516925440, "Incorrect IEEE Single Precision max value")

    def testIEEEDouble(self):
        self.assertEqual(customfloat.IEEE_DOUBLE_PRECISION.getMaxValue(),
                179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368, "Incorrect IEEE Double Precision max value")

    def testCustomSpecStandard(self):
        custom_spec = customfloat.FloatSpecification(3, 6)
        self.assertEqual(custom_spec.getMaxValue(), 15.875)

    def testCustomSpecNoSign(self):
        custom_spec = customfloat.FloatSpecification(3, 6, sign=False)
        self.assertEqual(custom_spec.getMaxValue(), 15.875)

    def testCustomSpecNoSpecialValues(self):
        custom_spec = customfloat.FloatSpecification(3, 6, special_values=False)
        self.assertEqual(custom_spec.getMaxValue(), 31.75)

    def testCustomSpecNoExponent(self):
        custom_spec = customfloat.FloatSpecification(0, 6)
        self.assertEqual(custom_spec.getMaxValue(), 63)

    def testCustomSpecMantissaOnly(self):
        custom_spec = customfloat.FloatSpecification(0, 6, sign=False, special_values=False)
        self.assertEqual(custom_spec.getMaxValue(), 63)

class MinValue(unittest.TestCase):

    def testIEEESingle(self):
        self.assertEqual(customfloat.IEEE_SINGLE_PRECISION.getMinValue(), -340282346638528859811704183484516925440, "Incorrect IEEE Single Precision min value")

    def testIEEEDouble(self):
        self.assertEqual(customfloat.IEEE_DOUBLE_PRECISION.getMinValue(), -179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368, "Incorrect IEEE Double Precision min value")

    def testCustomSpecStandard(self):
        custom_spec = customfloat.FloatSpecification(3, 6)
        self.assertEqual(custom_spec.getMinValue(), -15.875)

    def testCustomSpecNoSign(self):
        custom_spec = customfloat.FloatSpecification(3, 6, sign=False)
        self.assertEqual(custom_spec.getMinValue(), 0)

    def testCustomSpecNoSpecialValues(self):
        custom_spec = customfloat.FloatSpecification(3, 6, special_values=False)
        self.assertEqual(custom_spec.getMinValue(), -31.75)

    def testCustomSpecNoExponent(self):
        custom_spec = customfloat.FloatSpecification(0, 6)
        self.assertEqual(custom_spec.getMinValue(), -63)

    def testCustomSpecMantissaOnly(self):
        custom_spec = customfloat.FloatSpecification(0, 6, sign=False, special_values=False)
        self.assertEqual(custom_spec.getMinValue(), 0)

if __name__ == "__main__":
    unittest.main()
