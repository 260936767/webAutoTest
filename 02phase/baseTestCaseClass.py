import unittest

import sys,os
sys.path.append(os.getcwd())

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")