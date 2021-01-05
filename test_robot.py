import unittest
import robot
import world.obstacles as obstacles
from unittest.mock import patch
from io import StringIO
import sys


class MyRobotTests(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\noff"))
    def test_get_robot_name(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nside 10\nforward 10\noff"))
    def test_get_command(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I did not understand 'side 10'.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""")


    def test_test_split_command_input(self):
        self.assertEqual(robot.split_command_input("forward 10"), ("forward", '10'))
        self.assertEqual(robot.split_command_input("replay"), ("replay", ""))


    @patch("sys.stdin", StringIO("HAL\nforward 10\noff"))
    def test_split_command_input_function_output(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""")


    def test_is_int(self):
        self.assertTrue(robot.is_int("10"))
        self.assertFalse(robot.is_int("ten"))


    def test_valid_command(self):
        self.assertTrue(robot.valid_command("forward 10"))
        self.assertFalse(robot.valid_command(""))
        self.assertFalse(robot.valid_command("side 10"))


    @patch("sys.stdin", StringIO("HAL\nhelp\noff"))
    def test_do_help(self):
        self.maxDiff = None
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, 
LEFT, SPRINT]

 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 20\nback 10\noff"))
    def test_show_position(self):
        with patch("sys.stdout", StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 20 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay\noff"))
    def test_do_replay(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,25).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""")

    
    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay silent\noff"))
    def test_do_replay_silently(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.maxDiff = None
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay reversed\noff"))
    def test_do_replay_reversed(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.maxDiff = None
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 10\nforward 5\nreplay reversed silently\noff"))
    def test_do_replay_reversed_silently(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()        
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Sorry, I did not understand 'replay reversed silently'.
HAL: What must I do next? HAL: Shutting down..""")

    
    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nreplay 2\noff"))
    def test_do_replay_n(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 3 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nforward 4\nforward 5\nreplay 3-1\noff"))
    def test_do_replay_n_to_m(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 4 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,18).
 > HAL moved forward by 4 steps.
 > HAL now at position (0,22).
 > HAL replayed 2 commands.
 > HAL now at position (0,22).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nforward 4\nforward 5\nreplay 3 reversed\noff"))
    def test_do_replay_n_reversed(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 4 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,18).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 1 steps.
 > HAL now at position (0,21).
 > HAL replayed 3 commands in reverse.
 > HAL now at position (0,21).
HAL: What must I do next? HAL: Shutting down..""")


    @patch("sys.stdin", StringIO("HAL\nforward 1\nforward 2\nforward 3\nforward 4\nforward 5\nreplay 3 reversed\noff"))
    def test_do_replay_n_silent(self):
        with patch("sys.stdout", new=StringIO()) as out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
            output = out.getvalue().strip()
        self.assertEqual(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,1).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 4 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,18).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 1 steps.
 > HAL now at position (0,21).
 > HAL replayed 3 commands in reverse.
 > HAL now at position (0,21).
HAL: What must I do next? HAL: Shutting down..""")


if __name__ == "__main__":
    unittest.main()