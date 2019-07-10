
import random
import shutil

test_file = 'ImageSplits/test.txt'
jpg_imag = 'JPEGImages/'
val_data = 'validation/'

l = []
with open(test_file) as f:
    for file in f:
	    l.append(file.split('\n')[0])

    random.shuffle(l)
    new_m = open(file, 'w')
    for i in l[:2500]:
        file= 'ImageSplits/val.txt'
        
        new_m.write(i)
        shutil.copy2(jpg_imag+i,val_data)
        