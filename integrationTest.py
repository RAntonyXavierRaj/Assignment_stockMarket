# this test file has some errors.
# But just to show my attempt I have submitted this.

import unittest
from main import main 
from marketIndex import marketIndex as index

class stockTestCase(unittest.TestCase):  # market index integration test
    """Tests for stock.py`."""
    main.main()
    
    def test_dividend_yield(self):
        """Checking Value of Dividend yield"""
        self.assertAlmostEqual(index.stocks[2].calculateDividendYield(105.0), 0.21905, 5)
            
    def test_price_earnings_ratio(self):
        """Checking Value of PE ratio"""
        self.assertAlmostEqual(index.stocks[2].calculatePriceToEarningsRatio(105.0), 4.56522, 5)
        
    def test_volume_weighted_stock_price(self):
        """Checking Value of Volume Weighted Stock price"""
        self.assertAlmostEqual(index.stocks[2].calculateVolumeWeightedStockPrice(), 102.38462, 5)
        
    def test_all_share_index(self):
        """Checking Value of Volume Weighted Stock price"""
        self.assertAlmostEqual(index.allShareIndex(), 102.5872, 103.18572, 7)

if __name__ == '__main__':
    unittest.main()