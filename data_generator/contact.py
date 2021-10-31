import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                     work_number='+' + str(random.randint(100000000000, 999999999999))) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(test_data, unpicklable=False, indent=2))
