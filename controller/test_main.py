import unittest
import pandas as pd
from controller.main import GenrePercentagePerYearChart, AvgRatingPerYearChart, AvgRatingPerGenreChart, GenreDistributionChart, TotalRatingsPerYearChart, RatingsPercentagePerGenreChart, RatingsPercentagePerYearChart, plot_chart

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
        
class TestTotalRatingsPerYearChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating amount': ["2K", "2.5K", "333K", "2K", "2.5K", "0.5K"]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = TotalRatingsPerYearChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)
        
class TestRatingsPercentagePerGenreChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating amount': [2, 20, 3334, 2000, 2500, 500]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = RatingsPercentagePerGenreChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)

class TestRatingsPercentagePerYearChart(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating amount': [2, 20, 3334, 2000, 2500, 500]
        }
        self.data = pd.DataFrame(data)
    def test_plot(self):
        generated_chart = plot_chart(None, self.data, None)
        self.assertIsNone(generated_chart)
    
class TestRatingsPercentagePerYearChartDuo(unittest.TestCase):
    def setUp(self):
        data = {
            'Year': [2019, 2019, 2020, 2020, 2021, 2021],
            'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy', 'Drama'],
            'Rating amount': [2, 20, 3334, 2000, 2500, 500]
        }
        self.data = pd.DataFrame(data)

    def test_plot(self):
        chart = RatingsPercentagePerYearChart(None, self.data)

        generated_chart = chart.plot()
        self.assertGreater(generated_chart, 0)

if __name__ == '__main__':
    unittest.main()