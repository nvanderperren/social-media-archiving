from sys import argv
from argparse import ArgumentParser

with open(argv[1]) as input:
    lines = input.readlines()
    input.close()

with open(argv[1], 'w') as output:
    for line in lines:
        output.write('      - ' + line)

output.close()

