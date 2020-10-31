from datetime import datetime, date
import typing
import random
from decimal import Decimal
from faker import Faker
from collections import namedtuple, Counter

## Q2 10000 Random Profiles using dictionary approach
def profile_by_dictionary():
    p = faker.profile()
    p = {
        'name': p['name'],
        'age': get_age(p['birthdate']),
        'blood_type': p['blood_group'],
        'cur_loc': p['current_location']
    }

    return p


def all_profiles_by_dictionary(num_profiles):
    if not isinstance(num_profiles, int):
        raise ValueError("Number of Profiles needs to be an integer")
    profiles = {i: profile_by_dictionary() for i in range(num_profiles)}
    return profiles


def blood_type_dictionary(dict_profiles):
    counter = Counter()
    for key, profile in dict_profiles.items():
        counter[profile.get('blood_type', '')] += 1
    return counter.most_common(1)[0][0]


def mean_location_dictionary(dict_profiles):
    mean_loc = (0, 0)
    num = len(dict_profiles)
    for key, p in dict_profiles.items():
        cur_loc = p.get('cur_loc', (0, 0))
        mean_loc = mean_loc[0]+cur_loc[0],  mean_loc[1]+cur_loc[1]
    return mean_loc[0]/num, mean_loc[1]/num


def oldest_age_dictionary(dict_profiles):
    age = 0
    for key, p in dict_profiles.items():
        p_age = p.get('age', 0)
        if p_age > age:
            age = p_age
    return age


def average_age_dictionary(dict_profiles):
    age = sum(p.get('age', 0) for key, p in dict_profiles.items())
    return age/len(dict_profiles)

## Q1 10000 Random Profiles using named tuple approach
def get_age(x):
    return int((date.today() - x).days/365)


faker = Faker()
nt_keys_str = 'name blood_type age curr_loc'
profile = namedtuple('Profile', nt_keys_str)


def profile_by_named_tuple():
    profile = namedtuple('Profile', nt_keys_str)
    p1 = faker.profile()
    nt_1 = profile(p1['name'], p1['blood_group'], get_age(
        p1['birthdate']), p1['current_location'])
    return nt_1


def all_profiles_named_tuple(num_profiles):
    if not isinstance(num_profiles, int):
        raise ValueError("Number of Profiles needs to be an integer")

    nt_parent_keys_str = ' '.join(f'p{i}' for i in range(num_profiles))
    nt_parent = namedtuple('Parent_Tuple', nt_parent_keys_str)
    n_profies = tuple(profile_by_named_tuple() for _ in range(num_profiles))
    return nt_parent(*n_profies)


def blood_type_named_tuple(nt_profiles):
    counter = Counter()
    for p in nt_profiles:
        counter[p[1]] += 1
    return counter.most_common(1)[0][0]


def mean_location_named_tuple(nt_profiles):
    mean_loc = (0, 0)
    num = len(nt_profiles._fields)
    for p in nt_profiles:
        mean_loc = mean_loc[0]+p[3][0],  mean_loc[1]+p[3][1]
    return mean_loc[0]/num, mean_loc[1]/num


def oldest_age_named_tuple(nt_profiles):
    age = 0
    for p in nt_profiles:
        if p[-2] > age:
            age = p[-2]
    return age


def average_age_named_tuple(nt_profiles):
    age = sum(p[-2] for p in nt_profiles)
    return age/len(nt_profiles._fields)

## Q3 Stock of 100 companies
company_profile = namedtuple('Company', ['name', 'symbol', 'open', 'low', 'high', 'close'])


def return_symbol(x):
    return x[:3].upper() if len(
        x.split()) < 2 else ''.join(a[0].upper() for a in x.split())


def return_n_companies(num_companies):

    if not isinstance(num_companies, int):
        raise ValueError("Number of Company Profiles needs to be an integer")

    precision = 10
    weights_range = (.3, .9)
    stock_value_range = (1, 10000)
    max_high = round(random.uniform(1, 1.5), precision)
    min_low = round(random.uniform(.5, 1), precision)
    weights = [round(random.uniform(*weights_range), precision)
            for _ in range(num_companies)]
    norm_weights = [round(w / sum(weights), precision) for w in weights]

    profiles = []
    for i in range(num_companies):
        company_name = faker.company()
        company_sym = return_symbol(company_name)
        company_open = round(
            (random.randint(*stock_value_range) * norm_weights[i]), precision)
        company_high = round(random.uniform(
            company_open, company_open * max_high), precision)
        company_low = min(company_open, round(random.uniform(
            company_open * min_low, company_high), precision))
        company_close = round(random.uniform(
            company_low, company_high), precision)
        company = company_profile(
            company_name, company_sym, company_open, company_low, company_high, company_close)
        profiles.append(company)

    return profiles
