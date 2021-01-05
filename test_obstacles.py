import unittest
import world.obstacles as obstacles
from unittest.mock import patch
import sys
from io import StringIO


class MyObstacleTests(unittest.TestCase):
    def test_is_path_blocked(self):
        self.assertFalse(obstacles.is_path_blocked(10,5,10,8))
        self.assertFalse(obstacles.is_path_blocked(10,8,10,5))
        self.assertFalse(obstacles.is_path_blocked(2,5,10,5))
        self.assertFalse(obstacles.is_path_blocked(10,5,2,5))
        
        
if __name__ == "__main__":
    unittest.main()

 