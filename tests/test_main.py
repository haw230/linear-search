#import unittest
import pytest
import sys

sys.path.insert(0, '/home/ubuntu/workspace/linear_search') #for main.py
sys.path.insert(0, '/home/ubuntu/workspace/solution') #solved_search.py

from main import search
from solution import solved_search
    
def test_answer():
    assert(search([0,1,2], 1)) == solved_search([0,1,2], 1)
    assert(search([1,2,3], 2)) == solved_search([0,1,2], 2)
    assert(search([1,2,3], 3)) == solved_search([0,1,2], 3)
            
def main():
    test_answer()

if __name__ == '__main__':
    main()