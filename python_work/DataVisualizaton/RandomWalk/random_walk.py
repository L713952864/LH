from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=50000):
        """初始化随机漫步次数
            随机漫步起始于(0, 0)
        """
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice(list(range(0, 5)))
        return direction * distance

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            """
            x_direction = choice([-1, 1])
            x_distance = choice(list(range(0, 5)))
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 3, 5, 7, 9])
            y_step = y_direction * y_distance
            """
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # 将x_step与x_values中最后一个值相加得到下一个点的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)