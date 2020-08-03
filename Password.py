import random
import argparse
import os
import sys
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "1234567890"
SYMBOLS = "!@#$%^&*(){}[]<>,."
parser = argparse.ArgumentParser()
parser.add_argument("length" , help="Give the desired length for password(Minimum-length = 8) ")
parser.add_argument("strength",help ="Give the strength for password\nl --> low, m --> medium, s --> strong")
args = parser.parse_args()
if int(args.length) < 8:
    print("\nPLEASE GIVE LENGTH GREATER THAN OR EQUAL TO '8'\n")
    os.system(f'cmd /c "python {__file__} -h"')
    sys.exit()
if args.strength not in "lms":
    print("\nPLEASE ONLY GIVE AVAILABLE OPTIONS(l,m,s)\n")
    os.system(f'cmd /c "python {__file__} -h"')
    sys.exit()
password = ""
if args.strength == 'l':
    string = UPPERCASE + LOWERCASE
elif args.strength == 'm':
    string = UPPERCASE + LOWERCASE + DIGITS
else:
    string = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS
for i in range(int(args.length)):
    password = password + random.choice(string)
print(f"YOUR PASSWORD: {password}")
