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
print('\nStart Calculating Jensen_Shannon_Divergence ...')

import collections
vf = collections.Counter(pii) # extract vocabulary & frequencies

import random
spii = random.sample(pii, n)

import numpy as np
print("entropy by ensen_Shannon_Divergence: ")
def jsd3(w):
            d = np.diff( np.array( np.where(np.array(pii) == w)[0] ) )
            p = d/n # probability of term in original set
            d = None
            sd = np.diff( np.array( np.where(np.array(spii) == w)[0] ) )
            q = sd/n # probability of term in shuffled set
            sd = None
            m = (p+q)/2
            kld_pm = sum( p*np.log(p/m) )
            kld_qm = sum( q*np.log(q/m) )
            jsd = (kld_pm+kld_qm)/2 # jsd
            w_jsd = [w, "%f" % jsd]
            print([w, "%f" % jsd])
            return w_jsd

start1 = time.time()
jsd = list(map(jsd3,vf.keys()))
end1 = time.time()

pii = None
spii = None
vf = None

print("\nTime Calculating Jensen_Shannon_Divergence: ",(end1-start1))

print('\nStart Saving output ... ')
# EXCELS Wr.............................................
from xlsxwriter import Workbook
f = Workbook(r"C:\Users\user\Desktop\Jensen_Shannon_DivergenceFr2.xlsx")
worksheet = f.add_worksheet("My sheet")
row = 0
col = 0
with open(r"C:\Users\user\Desktop\Jensen_Shannon_DivergenceFr2.txt", 'w') as fout:
    for w, e2 in jsd:
        fout.write( "{} \t {} \n".format(w, e2))
        worksheet.write(row, col, w)
        worksheet.write(row, col + 1, e2)
        row += 1
    fout.write(f"\n\nNumber of decimal places Pi number {n = }\n")
    fout.write(f"Time Calculating Jensen_Shannon_Divergence: {end1-start1} \n")
    fout.write(f"Time read data: {end-start}")
    f.close()
print("End Program ....\n")