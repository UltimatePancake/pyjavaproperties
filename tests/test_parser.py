import os
import pytest
from pyjavaproperties import Properties


p = Properties()

file_path = os.path.join(os.path.dirname(__file__), "resources/test.properties")
p.load(open(file_path))

def test_parser_length():
    assert len(p.items()) == 4

def test_parser_content():
    assert p['test.property.1'] == 'herp'

def test_parser_empty_content():
    assert p['test.property.3'] == ''
