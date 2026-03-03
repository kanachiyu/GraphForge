# test_graphforge.py
"""
Tests for GraphForge module.
"""

import unittest
from graphforge import GraphForge

class TestGraphForge(unittest.TestCase):
    """Test cases for GraphForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GraphForge()
        self.assertIsInstance(instance, GraphForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GraphForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
