"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
  def __init__(self, n):
      self.decimal_val = n               
      self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
      return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))

    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
  return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(number):
  return (binary2int(number.binary_vec[:len(number.binary_vec)//2]),
            binary2int(number.binary_vec[len(number.binary_vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def subquadratic_multiply(x, y):
    # Base case: if one of the numbers has only one bit, directly multiply the decimal values
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val

    # Ensure x and y have the same length by padding with zeros
    while len(x.binary_vec) < len(y.binary_vec):
        x.binary_vec = ['0'] + x.binary_vec
    while len(y.binary_vec) < len(x.binary_vec):
        y.binary_vec = ['0'] + y.binary_vec

    # Additional padding to make sure the total length is even
    if len(x.binary_vec) % 2 == 1:
        x.binary_vec = ['0'] + x.binary_vec
        y.binary_vec = ['0'] + y.binary_vec

    n = len(x.binary_vec)
    mid = n // 2

    # Splitting the numbers
    x_high = binary2int(x.binary_vec[:mid])
    x_low = binary2int(x.binary_vec[mid:])
    y_high = binary2int(y.binary_vec[:mid])
    y_low = binary2int(y.binary_vec[mid:])

    # Recursive Karatsuba multiplication
    z0 = subquadratic_multiply(x_low, y_low)
    z2 = subquadratic_multiply(x_high, y_high)
    z1 = subquadratic_multiply(BinaryNumber(x_low.decimal_val + x_high.decimal_val), BinaryNumber(y_low.decimal_val + y_high.decimal_val)) - z2 - z0

    # The final combination of the results, adjusted for base and shifts
    result = (z2 * (2 ** (2 * mid))) + (z1 * (2 ** mid)) + z0
    return result


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

print(subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)))

