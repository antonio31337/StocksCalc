class BiggestDrop:
    def __init__(self, normalizer):
        self.normalizer = normalizer

    def get_insight(self):
        biggest_drop = None
        biggest_drop_in_percentage = None
        prev_data_point = None

        for data_point in self.normalizer.normalize():

            if biggest_drop is None:
                biggest_drop = data_point
                biggest_drop_in_percentage = 0
            elif self.calculate_drop_in_percentage(prev_data_point, data_point) > biggest_drop_in_percentage:
                biggest_drop = data_point
                biggest_drop_in_percentage = self.calculate_drop_in_percentage(prev_data_point, data_point)

            prev_data_point = data_point

        return biggest_drop, biggest_drop_in_percentage


class BiggestIntradayDrop(BiggestDrop):

    @staticmethod
    def calculate_drop_in_percentage(prev_data_point, data_point):
        return (prev_data_point.close - data_point.low) / prev_data_point.close * 100


class BiggestDropFromOpenToClose(BiggestDrop):

    @staticmethod
    def calculate_drop_in_percentage(prev_data_point, data_point):
        return (prev_data_point.close - data_point.close) / prev_data_point.close * 100



