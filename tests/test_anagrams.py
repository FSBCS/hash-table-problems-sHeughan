import pytest
from p1 import group_anagrams

def test_basic():
    assert group_anagrams(["bat", "tab", "eat", "tea", "tan", "nat"]) == [["bat", "tab"], ["eat", "tea"], ["tan", "nat"]]

def test_single_word():
    assert group_anagrams(["bat"]) == [["bat"]]

def test_empty_list():
    assert group_anagrams([]) == []

def test_no_anagrams():
    assert group_anagrams(["bat", "cat", "dog"]) == [["bat"], ["cat"], ["dog"]]

def test_all_anagrams():
    assert group_anagrams(["bat", "tab", "abt"]) == [["bat", "tab", "abt"]]
