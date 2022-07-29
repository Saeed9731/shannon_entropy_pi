import time
  
print('start Program ...\n')

print('Start Read data')
print('still Wating...\n')

start = time.time()

# Read data
with open(r"C:\Users\user\Desktop\pi9\pi9.txt",'r') as f:
    for line in f:
        pii = list(map(str,"".join(line.split())))

end =  time.time()
n = len(pii)
print(f"{n = }")

print('Read data Finished')
print("Time read data: ",(end-start))

time.sleep(5)
print('\nStart Calculating Shannon Entropy ...')

# Start Calculating Shannon Entropy
import collections
start1 = time.time()
vf = collections.Counter(pii) # extract vocabulary & frequencies
pii = None
p = [ x/n for x in list(vf.values()) ] # probability of terms
import numpy as np
e1 = -sum( p*np.log(p) ) # entropy by probability of term Frequency
end1 =  time.time()
print(f"Shannon entropy by probability of term Frequency {e1 = }")
print("Time Calculating Shannon Entropy: ",(end1-start1))
print('\nStart Saving output ... ')
with open(r"C:\Users\user\Desktop\Shannon entropy_probability_Fr.txt", "w") as external_file:
    external_file.write(f"Number of decimal places Pi number {n = }\n")
    external_file.write(f"Shannon entropy by probability of term Frequency {e1 = }\n")
    external_file.write(f"Time Calculating Shannon Entropy: {end1-start1} \n")
    external_file.write(f"Time read data: {end-start}")
print("End Program ....")
