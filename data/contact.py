from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


list_of_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']

test_data = [Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
                     last_name=random_string("last_name", 10), address=random_string("address", 20),
                     home_number='+' + str(random.randint(100000000000, 999999999999)), mobile_number='+' + str(random.randint(100000000000, 999999999999)),
                     birth_day=random.randint(1, 31), birth_month=list_of_month[random.randint(0, 11)], birth_year=random.randint(1950, 2021),
                     second_number='+' + str(random.randint(100000000000, 999999999999)),
                     work_number='+' + str(random.randint(100000000000, 999999999999))) for i in range(3)]