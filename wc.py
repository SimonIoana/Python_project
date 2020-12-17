import os
def myhelp():
 print ("-c: print the byte counts.")
 print ("-l: print the newline counts.")
 print ("-w: print the word counts.")
 print ("-m: print the character counts.")
 print ("--help: print this help and exits.")
 exit(0)

def wc(op, filename):
    try:
        fin = open(filename, 'r')
        text = fin.read()
        fin.close()
    except IOError:
        print("File %s not found" % filename)
        raise SystemExit

    number_of_characters = len(text)
    number_of_lines = text.count('\n') + 1
    wordlist = text.split(None)
    number_of_words = len(wordlist)
    help = myhelp()
    number_of_bytes=os.path.getsize('wc.py')

    if op == '-l':
        print("%d %s" % (number_of_lines, filename))
    elif op == '-w':
        print("%d %s" % (number_of_words, filename))
    elif op == '-m':
        print("%d %s" % (number_of_characters, filename))
    elif op == '-c':
        print("%d %s" % (number_of_bytes, filename))
    elif op == '--help':
        print("%d %s" % (help, filename))
    elif op == 'defalut':
        print("%d %d %d %s" % (number_of_lines, number_of_words, number_of_characters, filename))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] in ('-l', '-w', '-m', '-c', '--help'):
            for filename in sys.argv[2:]:
                wc(sys.argv[1], filename)
        else:
            if sys.argv[1][0] == '-':
                print('Your option is not valid!')
            else:
                for filename in sys.argv[1:]:
                    wc('default', filename)
    else:
        print("error")
