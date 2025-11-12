from get_curr_function import get_currencies
import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
req = requests.get(url)
data = req.json()["Valute"]


if __name__ == "__main__":
    
    import unittest
    
    class TestFunction(unittest.TestCase):
        
        def test_1(self):
            self.assertEqual(get_currencies(["USD"], url), {"USD": data["USD"]["Value"]})
            
        def test_2(self):
            self.assertEqual(get_currencies(["AUD"], url), {"AUD": data["AUD"]["Value"]})
            
        def test_3(self):
            self.assertEqual(get_currencies(["AZN", "DZD"], url),
                {"AZN": data["AZN"]["Value"], "DZD": data["DZD"]["Value"]})

        def test_4(self):
            self.assertEqual(get_currencies(["AZN", "RUT"], url), None)

    unittest.main()