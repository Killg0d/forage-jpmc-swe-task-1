import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote) , (quote["stock"], quote["top_bid"]["price"],quote["top_ask"]["price"],(quote["top_bid"]["price"]+quote["top_ask"]["price"])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote) , (quote["stock"], quote["top_bid"]["price"],quote["top_ask"]["price"],(quote["top_bid"]["price"]+quote["top_ask"]["price"])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_normal(self):
    # Test cases with non-zero price_b
    test_cases = [
        {"price_a": 120.48, "price_b": 119.2},
        {"price_a": 117.87, "price_b": 121.68}
    ]

    for case in test_cases:
        with self.subTest(case=case):
            result = getRatio(case["price_a"], case["price_b"])
            self.assertEqual(result,case["price_a"]/case["price_b"])

  def test_getRatio_price_b_zero(self):
    # Test case where price_b is zero
    result = getRatio(120.48, 0)
    self.assertIsNone(result)

  def test_getRatio_price_a_zero(self):
     # Test case where price_a is zero
     test_case={"price_a": 0, "price_b": 119.2}
     self.assertEqual(getRatio(test_case["price_a"],test_case['price_b']),test_case['price_a']/test_case['price_b'])

if __name__ == '__main__':
    unittest.main()
