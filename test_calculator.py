import unittest
from calculator import calculate_BMI

class TestCalculator(unittest.TestCase):

  def test_normal_bmi_calculation(self):
        """Test normal BMI calculations"""
        # Test case 1: Normal weight
        result = calculate_BMI(70, 175)  # 70kg, 175cm
        expected_bmi = round(70 / (1.75 ** 2), 2)  # Should be 22.86
        self.assertEqual(result["bmi"], expected_bmi)
        self.assertEqual(result["category"], "Normal weight")
        self.assertIsNone(result["error"])
        
        # Test case 2: Different normal weight
        result = calculate_BMI(60, 160)  # 60kg, 160cm
        expected_bmi = round(60 / (1.6 ** 2), 2)  # Should be 23.44
        self.assertEqual(result["bmi"], expected_bmi)
        self.assertEqual(result["category"], "Normal weight")
    
def test_underweight_category(self):
        """Test underweight BMI category"""
        result = calculate_BMI(45, 175)  # Should result in BMI < 18.5
        self.assertLess(result["bmi"], 18.5)
        self.assertEqual(result["category"], "Underweight")
        self.assertIsNone(result["error"])

def test_overweight_category(self):
        """Test overweight BMI category"""
        result = calculate_BMI(80, 170)  # Should result in 25 <= BMI < 30
        self.assertGreaterEqual(result["bmi"], 25)
        self.assertLess(result["bmi"], 30)
        self.assertEqual(result["category"], "Overweight")
    
def test_obese_category(self):
        """Test obese BMI category"""
        result = calculate_BMI(100, 170)  # Should result in BMI >= 30
        self.assertGreaterEqual(result["bmi"], 30)
        self.assertEqual(result["category"], "Obese")
    
def test_boundary_values(self):
        """Test BMI boundary values"""
        # Test lower boundary of normal weight (18.5)
        # Need to find weight that gives exactly 18.5 BMI for height 170cm
        height_m = 1.7
        weight_for_185_bmi = 18.5 * (height_m ** 2)
        result = calculate_BMI(weight_for_185_bmi, 170)
        self.assertEqual(result["bmi"], 18.5)
        self.assertEqual(result["category"], "Normal weight")
        
        # Test upper boundary of normal weight (just under 25)
        weight_for_249_bmi = 24.9 * (height_m ** 2)
        result = calculate_BMI(weight_for_249_bmi, 170)
        self.assertAlmostEqual(result["bmi"], 24.9, places=1)
        self.assertEqual(result["category"], "Normal weight")

if __name__ == "__main__":
    unittest.main()