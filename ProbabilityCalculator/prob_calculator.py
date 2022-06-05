import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        """
        A hat will always be created with at least one ball. The arguments passed into the hat object
        upon creation should be converted to a contents instance variable. contents should be a list
        of strings containing one item for each ball in the hat. Each item in the list should be a color
        name representing a single ball of that color. For example,
        if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].
        """
        # self.contents = list()
        # for k, v in kwargs.items():
        #     for i in range(v):
        #         self.contents.append(k)
        self.contents = [k for k, v in kwargs.items() for x in range(v)]

    def draw(self, num):
        """
        The Hat class should have a draw method that accepts an argument
        indicating the number of balls to draw from the hat.
        This method should remove balls at random from contents and return those balls as a list of strings.
        The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
        If the number of balls to draw exceeds the available quantity, return all the balls.
        """
        if num >= len(self.contents):
            return self.contents
        # return random.sample(self.contents, num)
        # lst = list()
        # for x in range(num):
        #     s = random.choice(self.contents)
        #     self.contents.remove(s)
        #     # lst.append(self.contents.pop(random.randrange(len(self.contents))))
        #     lst.append(s)
        # return lst
        """
        They didn't specified random method!
        """
        return [self.contents.pop(random.randrange(len(self.contents))) for i in range(num)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    This function should accept the following arguments:
        * hat: A hat object containing balls that should be copied inside the function.
        * expected_balls: An object indicating the exact group of balls
          to attempt to draw from the hat for the experiment.
          For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat,
          set expected_balls to {"blue":2, "red":1}.
        * num_balls_drawn: The number of balls to draw out of the hat in each experiment.
        * num_experiments: The number of experiments to perform.
         (The more experiments performed, the more accurate the approximate probability will be.)
         The experiment function should return a probability.
    """
    # exp_balls = [k for k, v in expected_balls.items() for x in range(v)]
    # match = 0
    # for x in range(num_experiments):
    #     new_hat = copy.deepcopy(hat)
    #     drawn = new_hat.draw(num_balls_drawn)
    #     if all(item in drawn for item in exp_balls):
    #         match += 1
    """
    They didn't specified random method!
    """
    match = 0
    for i in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        match += 1 if balls_req == len(expected_balls) else 0
    try:
        return match / num_experiments
    except ZeroDivisionError:
        return -1


