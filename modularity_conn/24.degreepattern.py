#!/usr/bin/python

import operator
import os

os.chdir(os.environ["state"]+"/groupstats")
print os.getcwd()

## these are the codes for the possible combinations
combo_dict = {(1, 2, 3, 4): 1,
 (1, 2, 4, 3): 2,
 (1, 3, 2, 4): 3,
 (1, 3, 4, 2): 4,
 (1, 4, 2, 3): 5,
 (1, 4, 3, 2): 6,
 (2, 1, 3, 4): 7,
 (2, 1, 4, 3): 8,
 (2, 3, 1, 4): 9,
 (2, 3, 4, 1): 10,
 (2, 4, 1, 3): 11,
 (2, 4, 3, 1): 12,
 (3, 1, 2, 4): 13,
 (3, 1, 4, 2): 14,
 (3, 2, 1, 4): 15,
 (3, 2, 4, 1): 16,
 (3, 4, 1, 2): 17,
 (3, 4, 2, 1): 18,
 (4, 1, 2, 3): 19,
 (4, 1, 3, 2): 20,
 (4, 2, 1, 3): 21,
 (4, 2, 3, 1): 22,
 (4, 3, 1, 2): 23,
 (4, 3, 2, 1): 24}

combo_codes = []
meds = open("mediansAllConditions.sorted.txt","r")
for line in meds:
    aa = line.split()
    aa_int = map(int,aa)
    if sum(aa_int) == 0:
        combo_codes.append(0)
    else:    
        aa_dict = dict(zip(range(1,5),aa_int))
        sorted_aa_key = sorted(aa_dict.iteritems(), key=operator.itemgetter(1))
        key_tuple = sorted_aa_key[0][0], sorted_aa_key[1][0], sorted_aa_key[2][0], sorted_aa_key[3][0]
        combo_codes.append(combo_dict[key_tuple])


code_out = ""
for code in combo_codes:
    code_out += `code`+"\n"


outf = open("combo_pairs_pattern.txt","w")
outf.write(code_out)
outf.close()

print os.system("paste -d ' ' ijk_coords_TTavg152T1 combo_pairs_pattern.txt > combo_pairs_pattern.ijk.txt")
print os.system("3dUndump -prefix combo_pairs_pattern.ijk -ijk -datum short -master automask_d1_TTavg152T1+tlrc combo_pairs_pattern.ijk.txt")
