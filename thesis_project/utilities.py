import csv
import datetime
import os
import random
import re
import string


# TODO: Linter for numbers

def random_string_generator(len_string=10):
    """Generates a random string of length len_string.
    String will contain only lowercase letters and digits.
    :param len_string: length of returned string (default 10)
    :return: string of length len_string
    """

    lowercase_letters_and_digits = list(string.ascii_lowercase + string.digits)
    return ''.join(random.choices(lowercase_letters_and_digits, weights=None, k=len_string))


def convert_date_int_yyyymmdd(int_yyyymmdd):
    if isinstance(int_yyyymmdd, datetime.date):
        return int_yyyymmdd
    elif int_yyyymmdd is None:
        return None
    str_yyyymmdd = str(int_yyyymmdd)
    year = str_yyyymmdd[0:4]
    month = str_yyyymmdd[4:6]
    day = str_yyyymmdd[6:]
    date_tup = tuple(map(int, [year, month, day]))
    return datetime.date(date_tup[0], date_tup[1], date_tup[2])


def decode_genotype(genotype):
    if type(genotype) is str:
        if genotype == 't':
            return 'knock out'
        elif genotype == 'f':
            return 'wild type'
        return genotype
    if genotype == 0:
        return 'wild type'
    return 'knock out'


def encode_genotype(genotype):
    if type(genotype) is bool:
        return genotype
    elif genotype == 'wild type':
        return False
    return True


def prep_string_for_db(instring):
    instring_lower = instring.lower()
    split_string = re.split('[_\-/ ]', instring_lower)
    joined_string = "-".join(split_string)
    return joined_string


# TODO write TestUtilitiesDatabase test_list_from_cursor(self)
def list_from_cursor(cursor_fetch):
    return list(item for tup in cursor_fetch for item in tup)


def read_table_csv_to_list(backup_folder_path, table_name):
    table_filename = table_name + '.csv'
    table_dir = os.path.join(backup_folder_path, table_filename)
    with open(table_dir) as f:
        contents = list(csv.reader(f))
    return contents
