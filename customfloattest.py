import unittest
import customfloat

class MaxValue(unittest.TestCase):

    def testIEEESingle(self):
        self.assertEqual(customfloat.IEEE_SINGLE_PRECISION.getMaxValue(), 340282346638528859811704183484516925440, "Incorrect IEEE Single Precision max value")

    def testIEEEDouble(self):
        self.assertEqual(customfloat.IEEE_DOUBLE_PRECISION.getMaxValue(),
                179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368, "Incorrect IEEE Double Precision max value")

    def testCustomSpecStandard(self):
        custom_spec = customfloat.FloatSpecification(3,6)
        self.assertEqual(custom_spec.getMaxValue(), 15.875)

    def testCustomSpecNoSign(self):
        custom_spec = customfloat.FloatSpecification(3,6, sign=False)
        self.assertEqual(custom_spec.getMaxValue(), 15.875)

if __name__ == "__main__":
    unittest.main()
