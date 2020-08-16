import json
import random

cc_data = {}
dc_data = {}
with open("Collegecode.json") as fcc, open("Departmentcode.json") as fdc:
    cc_data = json.load(fcc)
    dc_data = json.load(fdc)

cc_data = list(cc_data.keys())
# Avoiding MBA for now
dc_data = [x for x in dc_data.keys() if len(x) == 2]


# Format is (COLL){3} (BATCH){2} (DEPT){2}{3, for MBA} (USN){3}{2, for MBA}

for x in range(300):
    cc = random.choice(cc_data)
    dc = random.choice(dc_data)
    batch = random.randint(10, 19)
    usn = random.randint(1, 450)
    dip = True if usn >= 400 else False
    usn = str(usn).zfill(3)
    print("{}{}{}{}, {}, {}, {}".format(cc, batch, dc, usn, 2000 + batch, dc, dip))
