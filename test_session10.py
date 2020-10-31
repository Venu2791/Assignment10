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
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 300 words"

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
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
	
num_profiles = 10
nt_profiles = main.all_profiles_named_tuple(num_profiles)
dict_profiles = main.all_profiles_by_dictionary(num_profiles)	

def test_blood_type_named_tuple():
    counter = Counter()
    for p in nt_profiles:
        counter[p[1]] += 1
    assert counter.most_common(1)[0][0] == main.blood_type_named_tuple(nt_profiles),'Check named tuple implementation of most common blood type'
	   
def test_blood_type_dictionary():
    counter = Counter()
    for key, profile in dict_profiles.items():
        counter[profile.get('blood_type', '')] += 1
    assert counter.most_common(1)[0][0] == main.blood_type_dictionary(dict_profiles),'Check dict implementation of most common blood type'
	

def test_mean_location_named_tuple():
    mean_loc = (0,0)
    num = len(nt_profiles._fields)
    for p in nt_profiles:
        mean_loc = mean_loc[0]+p[3][0],  mean_loc[1]+p[3][1]
        mean_loc[0]/num, mean_loc[1]/num == main.oldest_age_named_tuple(nt_profiles),'Check namedtuple implementation of mean location'
	

def test_mean_location_dictionary():
    mean_loc = (0,0)
    num = len(dict_profiles)
    for key, p in dict_profiles.items():
        cur_loc = p.get('cur_loc', (0, 0))
        mean_loc = mean_loc[0]+cur_loc[0],  mean_loc[1]+cur_loc[1] 
        mean_loc[0]/num, mean_loc[1]/num == main.mean_location_dictionary(dict_profiles),'Check dict implementation of mean location'      
	

def test_oldest_age_dictionary():
    profiles = [p for key, p in dict_profiles.items()]
    max_age_prof = sorted(profiles, key=lambda x:x['age'])[-1]
    assert max_age_prof['age'] == main.oldest_age_dictionary(dict_profiles),'Check dict implementation of max age'      
	

def test_oldest_age_named_tuple():
    age = 0
    age = max(p.age for p in nt_profiles)
    assert age == main.oldest_age_named_tuple(nt_profiles),'Check namedtuple implementation of max age'
	

def test_average_age_named_tuple():
    avg_age = sum(p.age for p in nt_profiles)/len(nt_profiles._fields)
    assert avg_age == main.average_age_named_tuple(nt_profiles),'Check namedtuple implementation of avg. age'
	

def test_average_age_dictionary():
    avg_age = sum(p['age'] for _, p in dict_profiles.items())/len(dict_profiles)
    assert avg_age == main.average_age_dictionary(dict_profiles),'Check dict implementation of avg. age'
	

def test_company_profile():
    profile = main.return_n_companies(1)[0]
    assert profile.low <= profile.open and profile.high >= profile.low and profile.close >= profile.low , f'str(profile)'

