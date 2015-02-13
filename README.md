The purpose of customfloat is to perform calculations using custom floating point specifications. The main use case for such functionality is education. While the IEEE single and double precision floating point numbers are the computing standard, they are too large to easily perform calculations by hand when learning the basics of floating point numbers. In a classroom setting it is common to use custom specifications that are much smaller. These small (~10 bit) numbers are easy to to work with when learning and trying the concepts by hand, but they come with the cost of not being able to check your work because every respectable calculator uses floating point numbers that match IEEE standards. This project aims to allow users to enter their own specifications and perform basic operations on numbers matching that specification.

This project aims to allow users to choose:

- whether or not to have a sign bit
- how many exponent bits they want (>=0)
- how many mantissa bits they want (>=1)
- if special values (positive infinity, negative infinity, NaN) will be represented

Goals:

- Adding numbers
- Subtracting numbers
- Multiplying numbers
- Basic info about the custom spec: min value, max value, bias (if there is an exponent)
