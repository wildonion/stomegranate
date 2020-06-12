

# https://www.youtube.com/watch?v=RO5alU6PpSU
# https://realpython.com/primer-on-python-decorators/
# https://www.allaboutcircuits.com/textbook/digital/chpt-8/logic-simplification-karnaugh-maps/


# ---------------------------------
# karnuagh map using sop (minterms)
# ---------------------------------

# >>> f and minterms length validation using argparse

import numpy as np
import argparse

function = input("Enter your function vars | eg : f(x,y,z) >>> ")
minterms = input("Enter your minterms | eg : 1, 2, 0, 4 >>> ")
minArr = minterms.split(",")
fvars = function[2:len(function)-1].split(",")
nvars = len(fvars)
totalCombo = 2 ** nvars


if nvars is 3:
    kMap = np.full((2, 3), 0)
else:
    kMap = np.full((nvars, nvars), 0)

# -----------
# truth table
# -----------
# >>> get all total combo in 2 ** nvars
# >>> use np arr to draw the table

truth_table = np.full((totalCombo, nvars), 0)
for i in range(totalCombo+1):
	if i != 0 : 
		comboArr = []
		comboArr.append(int(bin(totalCombo%i)) >> nvars)
		# print(f"i is >> {bin(totalCombo%i)}")
		print(comboArr)


print(truth_table)
print(kMap)