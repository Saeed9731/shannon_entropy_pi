import time
  

print('start Program ...\n')

print('Start Read data')
print('still Wating...\n')

start = time.time()
# G:\programing\coding\pi.txt
# "C:\Users\user\Desktop\pi9\pi9.txt"
with open(r"C:\Users\user\Desktop\pi9\pi9.txt",'r') as f:
    for line in f:
        pii = list(map(str,"".join(line.split())))

end =  time.time()
n = len(pii)
print(f"{n = }")
print('Read data Finished')
print("Time read data: ",(end-start))

time.sleep(4)

print('\nStart Calculating Shannon Entropy ...')
import collections
vf = collections.Counter(pii)

import numpy as np
print("entropy by probability of term distance: ")

def js(w):
        d = np.diff( list( np.where(np.array(pii) == w)[0] ) )
        p = [ x/n for x in d ] # probability of term
        e2 = -sum( p*np.log(p) ) # entropy by probability of term distance
        w_e2 = [w, "%f" % e2]
        print([w, "%f" % e2])
        return w_e2

start1 = time.time()
jsd = list(map(js,vf.keys()))
end1 = time.time()
pii = None
vf = None

print("\nTime Calculating Shannon Entropy: ",(end1-start1))

print('\nStart Saving output ... ')
# EXCELS Wr.............................................
from xlsxwriter import Workbook
f = Workbook(r"C:\Users\user\Desktop\Shannon entropy_probability_Fr2.xlsx")
worksheet = f.add_worksheet("My sheet")
row = 0
col = 0
with open(r"C:\Users\user\Desktop\Shannon entropy_probability_Fr2.txt", 'w') as fout:
    for w, e2 in jsd:
        fout.write( "{} \t {} \n".format(w, e2))
        worksheet.write(row, col, w)
        worksheet.write(row, col + 1, e2)
        row += 1
    fout.write(f"\n\nNumber of decimal places Pi number {n = }\n")
    fout.write(f"Time Calculating Shannon Entropy: {end1-start1} \n")
    fout.write(f"Time read data: {end-start}")
    f.close()
print("End Program ....\n")