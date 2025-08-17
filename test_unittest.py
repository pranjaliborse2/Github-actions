
from functions import add, subtract, divide
import numpy as np
# import unittest

def test_func_add():
    assert add(0, np.inf) == np.inf 

def test_func_subtract():
    assert subtract(np.inf,100000000000000000000) == np.inf and subtract(100000000000000000000,-np.inf) == np.inf

def test_func_divide():
    assert divide(1,0) == 0

# class test_functions(unittest.TestCase):
#     def test_func_add(self):
#         self.assertEqual(add(0, np.inf), np.inf)

#     def test_func_subtract(self):
#         self.assertEqual(subtract(np.inf,100000000000000000000), np.inf) and self.assertEqual(subtract(100000000000000000000,-np.inf),np.inf)

#     def test_func_divide(self):
#         self.assertEqual(divide(1,0),0)

# if __name__=='__main__':
#     unittest.main()