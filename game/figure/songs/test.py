import os, sys
l = os.listdir()

for i in l:
    if i.endswith('png'):
        os.system(f"touch {i[:-4]}.txt")