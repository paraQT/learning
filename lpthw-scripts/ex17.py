from sys import argv
from os.path import exists

script, from_file, to_file = argv

# in_file = open(from_file)
#in_file = open(from_file).read()

#print("The input file is %d bytes long" % len(in_file))
#print("Does the output file exist? %r" % exists(to_file))
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(in_file)

open(to_file, 'w').write(open(from_file).read())

#print("Alright, all done.")

#out_file.close()
#in_file.close()
