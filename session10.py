from datetime import datetime, date
import typing
import random
from decimal import Decimal
from faker import Faker
from collections import namedtuple, Counter


fake = Faker()
## Q2 10000 Random Profiles using dictionary approach
def dict_approach():
    counts, dict1 = dict(), dict()
    mean_loc1, mean_loc2 = 0, 0
    new_age, sum_age = 0, 0

    for i in range(1,10001):
        value = fake.profile()

        blood_group = value['blood_group']
        current_location = value['current_location']
        mean_loc1 = mean_loc1 + current_location[0]
        mean_loc2 = mean_loc2 + current_location[1]
        counts['mean_loc1'], counts['mean_loc2'] = mean_loc1/i, mean_loc2/i
        birthdate = value['birthdate']
        age = date.today().year - birthdate.year
        counts['oldest_age'] = age if age >= new_age else new_age
        sum_age = sum_age + age
        counts['avg_age'] = sum_age/i
        dict1[blood_group] = dict1[blood_group] + 1 if blood_group in dict1 else 1
    counts['blood_group'] = max(dict1)
    return counts

## Q1 10000 Random Profiles using dictionary approach
def named_tuple():
    counts = dict()
    
    sum_age, mean_loc1, mean_loc2 = 0, 0, 0
    new_age = 0
    Details = namedtuple('Details', 'blood_group mean_loc1 mean_loc2 oldest_age avg_age')
    
    for i in range(1,10001):
        value = fake.profile()

        blood_group = value['blood_group']
        current_location = value['current_location']
        mean_loc1 = mean_loc1 + current_location[0]
        mean_loc2 = mean_loc2 + current_location[1]
        birthdate = value['birthdate']
        age = date.today().year - birthdate.year
        oldest_age = age if age >= new_age else new_age
        sum_age = sum_age + age
        counts[blood_group] = counts[blood_group] + 1 if blood_group in counts else 1

    dt = Details(max(counts),mean_loc1/i, mean_loc2/i,oldest_age,sum_age/i)
    return dt

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
