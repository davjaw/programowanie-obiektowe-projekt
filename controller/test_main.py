import unittest
import pandas as pd
from controller.main import GenrePercentagePerYearChart, AvgRatingPerYearChart, AvgRatingPerGenreChart, GenreDistributionChart

class TestAvgRatingPerYearChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating': [7.5, 8.2, 6.9, 7.8, 8.1, 7.6]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = AvgRatingPerYearChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)
        
class TestAvgRatingPerGenreChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating': [7.5, 8.2, 6.9, 7.8, 8.1, 7.6]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = AvgRatingPerGenreChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)

class TestGenreDistributionChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating': [7.5, 8.2, 6.9, 7.8, 8.1, 7.6]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = GenreDistributionChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)
    
class TestGenrePercentagePerYearChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating': [7.5, 8.2, 6.9, 7.8, 8.1, 7.6]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = GenrePercentagePerYearChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)

if __name__ == '__main__':
    unittest.main()