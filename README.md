# Toy Robot 4
Fourth iteration of toy robot with updates.

* Toy robot is a program desgined to receive user input for movement of a robot such as forward, back, right, left.
* See *Iteration Updates* below for changes made from the previous iterations.
* You can run the program using the instructions in *To Run* below.
* You can test technical correctness by running the unit tests as in the section *To Test* below.

### Iteration Updates 

* This iteration has additional movements : replay, replay silent, replay reversed, replay reversed silent.
* In this iteration there is an additional element, obstacles that prevent the robot from passing over them.
* There are additional modules world/text and world/turtle.

### To Run

* `python3 robot.py`
* use command line argument `python3 robot.py text` to get the text output.
* use command line argument `python3 robot.py turtle` to get the visual turtle output.
* follow the input prompts to get the desired output.
* type help to see all valid commands.

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run robot tests: `python3 -m unittest test_robot.py`
* To run obstacle tests: `python3 -m unittest test_obstacles.py`
