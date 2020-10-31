import session10 as main
import pytest
import random
import os
import inspect
import re
from datetime import datetime, date
from  collections import namedtuple, Counter


main_funcs = [func for func in inspect.getmembers(main) if inspect.isfunction(func[1])]



README_CONTENT_CHECK_FOR = ["namedtuple", "dictionary"]

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 250, "Make your README.md file interesting! Add atleast 300 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_profile_using_dict():
    *_, = profile_using_dict()
    assert len(_) > 1, "Returns all the calculation"

def test_profile_using_named_tuple():
    *_, = profile_using_named_tuple()
    assert len(_) > 1, "Returns all the calculation"

def test_named_tuple_vs_dict():
    cnt = 0
    for _ in range(10):
        start1 = perf_counter()
        *_, = profile_using_dict()
        end1 = perf_counter()
        elapsed1 = end1 - start1

        start2 = perf_counter()
        *_, = profile_using_named_tuple()
        end2 = perf_counter()
        elapsed2 = end2 - start2

        if elapsed2 < elapsed1:
            cnt+=1
    assert cnt >= 4, "checking more than random times the namedtuple is performing better"
    
def test_company_profile():
    profile = main.return_n_companies(1)[0]
    assert profile.low <= profile.open and profile.high >= profile.low and \
    profile.close >= profile.low , f'str(profile)'
