import unittest
import sys
import os

# append module root directory to sys.path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

class FoosboardTestCase(unittest.TestCase):
    pass
