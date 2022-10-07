from typing import List, Tuple
import unittest, pytest
import numpy as np

def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows

class One_hot_encoder_uninttests(unittest.TestCase):
    def test_nunique_some_items(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(exp_transformed_cities,transformed_cities)
        
    def test_nunique_all_items(self):
        cities = ['Moscow', 'Moscow', 'Moscow']
        exp_transformed_cities = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1])
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(exp_transformed_cities,transformed_cities)
        
    def test_many_items(self): 
        #check if sum of all vectors is vector with all one's
        items = []
        for i in range (1000):
            items.append(str(i))
        transformed_items = fit_transform(items)
        all_vectors = [np.array(x[1]) for x in transformed_items]
        
        self.assertEqual(sum(all_vectors).tolist(),np.ones(1000).tolist())
    
    def test_exception(self):
        with self.assertRaises(TypeError):
            fit_transform()
        
#pytests
def test_nunique_some_items():
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]
        transformed_cities = fit_transform(cities)
        assert exp_transformed_cities == transformed_cities

def test_nunique_all_items():
        cities = ['Moscow', 'Moscow', 'Moscow']
        exp_transformed_cities = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1])
        ]
        transformed_cities = fit_transform(cities)
        assert exp_transformed_cities == transformed_cities

def test_many_items(): 
        #check if sum of all vectors is vector with all one's
        items = []
        for i in range (1000):
            items.append(str(i))
        transformed_items = fit_transform(items)
        all_vectors = [np.array(x[1]) for x in transformed_items]
        
        assert sum(all_vectors).tolist() == np.ones(1000).tolist()
        
def test_exception():
    with pytest.raises(TypeError):
        fit_transform()