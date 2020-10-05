"""
Data to be Generated:

Batches:
2015: CS: Sem 1
2016: TE: Sem 5


Given:
Credits = 4

MinExt = 21
MinTotal = 40

MaxExt = 60
MaxInt = 40
MaxMarks = 100


Per Subject:
    FCD = 70+
    FC = [60 - 70)
    SC = [40 - 60)

Total:
    FCD = 350+
    FC = [300-350]
    SC Otherwise

Required:
For Each Subject:
    FCD, SC, FC, Fail, Appeared

Total:
    FCD, FC, SC, Fail, Appeared.

Do:
For Each USN:
    Gen AppearChance(0,100); If < 90:
    TotalAppear+=1
        For Each Subcode:
            Gen Chance(0,100); If < 90:
                SubAppear+=1
                Gen Marks; Case:
                    If FCD? SubFCD+=1
                    If FC? SubFC+=1
                    if SC? SubSC+=1
                    if Fail? SubFail+=1
    If Fail in Any Subcode:
        TotalFail+=1


"""

import json
import random

# Constants for Generation:

USNAMT = 100
SUBJECT_AMT = 5

GEN_MIN_EXTE = 15
GEN_MAX_EXTE = 60

GEN_MIN_INTE = 15
GEN_MAX_INTE = 40

GEN_SUB_TOT = 100
GEN_TOT = SUBJECT_AMT * GEN_SUB_TOT

GEN_FCD = 0.7
GEN_FC = 0.6
GEN_SC = 0.4


GEN_CHANCE = 90
# Constants for Checking:

CHK_SUB_MIN_EXT = 21
CHK_SUB_MIN_TOT = 40

CHK_SUB_FCD = GEN_SUB_TOT * GEN_FCD
CHK_SUB_FC = GEN_SUB_TOT * GEN_FC
CHK_SUB_SC = GEN_SUB_TOT * GEN_SC


CHK_TOT_FCD = GEN_TOT * GEN_FCD
CHK_TOT_FC = GEN_TOT * GEN_FC
CHK_TOT_SC = GEN_TOT * GEN_SC


def chk_sub_pass(exte, sum) -> bool:
    return (exte >= CHK_SUB_MIN_EXT) and (sum >= CHK_SUB_MIN_TOT)


def chk_sub_fcd(sum) -> bool:
    return sum >= CHK_SUB_FCD


def chk_sub_fc(sum) -> bool:
    return CHK_SUB_FC <= sum < CHK_SUB_FCD


def chk_tot_fcd(sum) -> bool:
    return sum >= CHK_TOT_FCD


def chk_tot_fc(sum) -> bool:
    return CHK_TOT_FC <= sum < CHK_TOT_FCD


# Generator

final_dict = {}
usn_format = "1CR15CS{}"
sub_format = "15CS1{}"

usns = [usn_format.format(str(x).zfill(3)) for x in range(1, USNAMT + 1)]
subcodes = [sub_format.format(str(x)) for x in range(1, SUBJECT_AMT + 1)]

final_dict["usn"] = usns
final_dict["subcode"] = subcodes
final_dict["scores"] = []
final_dict["static"] = {
    "Usns": USNAMT,
    "Subjects": SUBJECT_AMT,
    "Semester": 1,
    "Batch": 2015,
    "Scheme": 2015,
    "Dept": "CS",
    "MaxExt": GEN_MAX_EXTE,
    "MinExt": CHK_SUB_MIN_EXT,
    "MaxInt": GEN_MAX_INTE,
    "MinInt": 0,
    "Total": GEN_SUB_TOT,
    "MinTotal": CHK_SUB_MIN_TOT,
    "FCD": CHK_SUB_FCD,
    "FC": CHK_SUB_FC,
    "SC": CHK_SUB_SC,
    "TotalFCD": CHK_TOT_FCD,
    "TotalFC": CHK_TOT_FC,
    "TotalSC": CHK_TOT_SC,
}


data_count = {
    "Appeared": 0,
    "FCD": 0,
    "FC": 0,
    "SC": 0,
    "Fail": 0,
    "SubData": {
        key: {"Appeared": 0, "FCD": 0, "FC": 0, "SC": 0, "Fail": 0} for key in subcodes
    },
}


for usn in usns:
    if random.randint(0, 100) < GEN_CHANCE:
        # Student Has Sat for Some Exams Atleast.
        data_count["Appeared"] += 1
        temp_appear = 0
        temp_sum = 0
        temp_fail = False
        for subcode in subcodes:
            if random.randint(0, 100) < GEN_CHANCE:
                # Student Has Appeared for This Subject
                temp_appear += 1
                data_count["SubData"][subcode]["Appeared"] += 1

                # Gen Marks
                inte = random.randint(GEN_MIN_INTE, GEN_MAX_INTE)
                exte = random.randint(GEN_MIN_EXTE, GEN_MAX_EXTE)

                sum = inte + exte
                temp_sum += sum
                final_dict["scores"].append((usn, subcode, inte, exte, sum))

                # Calculate Stuff:
                if chk_sub_pass(exte, sum):
                    # Pass
                    if chk_sub_fcd(sum):
                        data_count["SubData"][subcode]["FCD"] += 1
                    elif chk_sub_fc(sum):
                        data_count["SubData"][subcode]["FC"] += 1
                    else:
                        data_count["SubData"][subcode]["SC"] += 1
                else:
                    # Failed
                    data_count["SubData"][subcode]["Fail"] += 1
                    temp_fail = True

        if temp_appear == 0:
            data_count["Appeared"] -= 1
            continue

        if temp_fail is True:
            data_count["Fail"] += 1
        else:
            if chk_tot_fcd(temp_sum):
                data_count["FCD"] += 1
            elif chk_tot_fc(temp_sum):
                data_count["FC"] += 1
            else:
                data_count["SC"] += 1


final_dict["data"] = data_count

with open("data.json", "w") as f:
    json.dump(final_dict, f)
