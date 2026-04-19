import pytest
from string_utils import *

# count_vowels tests
def test_count_vowels_normal():
    assert count_vowels("Hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_case():
    assert count_vowels("AEIOU") == 5


# reverse_string tests
def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single():
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    assert reverse_string("") == ""


# is_palindrome tests
def test_is_palindrome_simple():
    assert is_palindrome("racecar") == True

def test_is_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False


# word_count tests
def test_word_count_normal():
    assert word_count("Hello World") == 2

def test_word_count_spaces():
    assert word_count("   spaces   ") == 1

def test_word_count_empty():
    assert word_count("") == 0


# capitalise_words tests
def test_capitalise_words_normal():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_mixed():
    assert capitalise_words("hELLo WoRLD") == "Hello World"

def test_capitalise_words_empty():
    assert capitalise_words("") == ""


# remove_duplicates tests
def test_remove_duplicates_normal():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_single():
    assert remove_duplicates("a") == "a"

def test_remove_duplicates_long():
    assert remove_duplicates("aaaaaaa") == "a"


# exception test
def test_functions_none_input():
    with pytest.raises(TypeError):
        count_vowels(None)