import sys
if len(sys.argv)<=2:
    sys.exit("Uncorrect usage")

for arg in sys.argv[1:]:
    print("hello,",arg.title())
