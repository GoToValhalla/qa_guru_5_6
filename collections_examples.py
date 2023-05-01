from collections import defaultdict

d = defaultdict(int)

print(d)

d = defaultdict(list)

d["users"].append("Marina")

print(d)

from collections import namedtuple

user = namedtuple("user", ["name", "age"])
user1 = user(name="Marina", age= 23)

print(user1)

from collections import OrderedDict

