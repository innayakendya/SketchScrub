# test_sketchscrub.py
"""
Tests for SketchScrub module.
"""

import unittest
from sketchscrub import SketchScrub

class TestSketchScrub(unittest.TestCase):
    """Test cases for SketchScrub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchScrub()
        self.assertIsInstance(instance, SketchScrub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchScrub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
