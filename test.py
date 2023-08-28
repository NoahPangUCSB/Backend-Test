import unittest

from main import multiToOne
from main import oneToMulti

class TestConvertArr(unittest.TestCase):

    def setUp(self):
        self.multiCon_dict_1 = {
                'one':
                {
                    'two': 3,
                    'four': [ 5,6,7]
                },
                'eight':
                {
                    'nine':
                    {
                        'ten':11
                    }
                }
            }
        self.oneDict_1 = {
                'one/two':3,
                'one/four/0':5,
                'one/four/1':6,
                'one/four/2':7,
                'eight/nine/ten':11
            }

        self.multiCon_list_2 = [
            {
                'one': 'hi',
                'two': 'bye'
            },
            2,
            (3, 4),
            {},
            {
                '05': 1
            }
        ]

        self.oneDict_2 = {
            '0/one': 'hi',
            '0/two': 'bye',
            '1': 2,
            '2/0': 3,
            '2/1': 4,
            '3': {},
            '4/05': 1
        }
        
        # Assuming for now that we aren't considering tuples as
        # a possible container, since the indices are the same as lists
        
        # self.multiCon_tuple_3 = (
        #     [2, 4],
        #     {
        #         'd': 2
        #     },
        #     {}
        # )

        # self.oneDict_3 = {
        #     '0/0': 2,
        #     '0/1': 4,
        #     '1/d': 2,
        #     '2': {}
        # }

        self.multiDict_empty_4 = {}

        self.oneDict_4 = {}
        
    def test_multiToOne_Dict(self):
        result = multiToOne(self.multiCon_dict_1)
        self.assertEqual(result, self.oneDict_1)
    
    def test_multiToOne_List(self):
        result = multiToOne(self.multiCon_list_2)
        self.assertEqual(result, self.oneDict_2)
    
    # def test_multiToOne_Tuple(self):
    #     result = multiToOne(self.multiCon_tuple_3)
    #     self.assertEqual(result, self.oneDict_3)
    
    def test_multiToOne_Empty(self):
        result = multiToOne(self.multiDict_empty_4)
        self.assertEqual(result, self.oneDict_4)
        
    
    def test_oneToMulti_Dict(self):
        result = oneToMulti(self.oneDict_1)
        self.assertEqual(result, self.multiCon_dict_1)
    
    def test_oneToMulti_List(self):
        result = oneToMulti(self.oneDict_2)
        self.assertEqual(result, self.multiCon_list_2)
    
    def test_oneToMulti_Empty(self):
        result = oneToMulti(self.oneDict_4)
        self.assertEqual(result, self.multiDict_empty_4)


if __name__ == '__main__':
    unittest.main()