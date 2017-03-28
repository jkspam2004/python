import unittest
#from tdd_package.src.parse_csv import read_data

class ParseCSVTest(unittest.TestCase):
    """
    Test parser for csv file
    """

    def setUp(self):
        self.data = "/Users/eto/Git/python/Learn/tdd_package/src/football.csv"
        self.parsed_data = [
            ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
            ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
            ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
        ]

    def test_csv_read_data_headers(self):
        """
        Check the headers
        """
        self.assertEqual(
            read_data(self.data)[0], ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points']
        )

    def test_csv_read_data_team_name(self):
        """
        Check reading team name
        """
        self.assertEqual(read_data(self.data)[1][0], 'Arsenal')

    def test_csv_read_data_points(self):
        """
        Check reading team score points
        """
        self.assertEqual(read_data(self.data)[1][7], '87')

    def test_get_min_score_difference(self):
        """
        Test the minimum score difference
        minimum difference is 37: goals - goals_allowed = 67 - 30 
        """
        self.assertEqual(get_min_score_difference(self.parsed_data), 1) # winning team 1

    def test_get_team(self):
        """
        Get the team name 
        """
        index_value = get_min_score_difference(self.parsed_data)
        self.assertEqual(get_team(index_value, self.parsed_data), 'Liverpool')


if __name__ == '__main__':
    print "package:", __package__

    if __package__ is None:
        #run inside of test dir $ python parse_csv_test.py -v
        import sys
        sys.path.insert(0, "../src")

        try:
            from parse_csv import read_data, get_min_score_difference, get_team
            sys.path.pop(0)
        except ImportError:
            print('No Import')
    else:
        #run outside of tdd_package dir $ python -m tdd_package.test.parse_csv_test -v
        from ..src.parse_csv import read_data, get_min_score_difference, get_team
       

    unittest.main()

"""
example from realpython
https://realpython.com/blog/python/python-interview-problem-parsing-csv-files/
"""
