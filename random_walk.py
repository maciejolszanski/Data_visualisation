from random import choice


class Randomwalk():
    '''Genearate random walk'''

    def __init__(self, num_points=5000):

        self.num_points = num_points

        # Origin
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Ganarate all points for random walk'''

        while len(self.x_values) < self.num_points:

            # set the direction and value of the step
            x_direction = choice([-1, 1])
            x_distance = choice([x for x in range(0,5)])
            x_step = x_direction * x_distance
            
            y_direction = choice([-1, 1])
            y_distance = choice([y for y in range(0,5)])
            y_step = y_direction * y_distance

            # reject moves that lead nowhere
            if x_step == 0 and y_step == 0:
                continue
        
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
