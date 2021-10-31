import json
from model.group import Group
import random
import string
import os.path
import getopt  # для чтения опций командной строки
import sys  # чтобы получить допступ к опциям командной строки
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


testdata = [Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 20))
            for i in range(n)]
# путь, куда будут сохраняться сгенерированные данные
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata, unpicklable=False, indent=2))
