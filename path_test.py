# This file tests the A* path-finding algorithm written in node.py
import unittest
from path import a_star, create_pathmap

class TestPathModule(unittest.TestCase):

    def test_already_at_goal(self):
        pathmap = create_pathmap(10, 10, fill=1.0)
        location = (5,5)
        path = a_star(pathmap, location, location)
        self.assertEqual(path, [(5,5)])

    def test_a_star(self):
        pathmap = create_pathmap(10, 10, fill=1.0)
        start_location = (0,9)
        end_location = (9,0)
        # Create blocking wall on the diagonal, except for at (0,0)
        for i in range(1, 10):
            pathmap[i][i] = 0
        path = a_star(pathmap, start_location, end_location)
        expected_path = \
            [(9,0), (8,0), (7,0), (6,0), (5,0), (4,0), (3,0), (2,0), (1,0),
             (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8),
             (0,9)]
        self.assertEqual(path, expected_path)

    def test_no_available_path(self):
        pathmap = create_pathmap(10, 10, fill=1.0)
        start_location = (0,9)
        end_location = (9,0)
        # Create blocking wall on the diagonal
        for i in range(0, 10):
            pathmap[i][i] = 0
        path = a_star(pathmap, start_location, end_location)
        self.assertEqual(path, None)


if __name__=="__main__":
    unittest.main()
