from main import subquadratic_multiply
from main import BinaryNumber


## Feel free to add your own tests here.
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
  assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
  assert subquadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
  assert subquadratic_multiply(BinaryNumber(12), BinaryNumber(3)) == 12*3
  assert subquadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 20*20
   

