#  Project Page: https://github.com/d0ntblink/pygrater/
#  
#  -------------------------------------------------------  #
#  PyGrater: An elegant way to search Google using the cli  #
#  -------------------------------------------------------  #
#  
#  This tool will take a user input (question) and respond
#  with a Google answer snippet.
# 
#  -------------------------------------------------------

import sys, getopt
from string_beautifier import inputCleanser
from google_page_pull import create_url, get_html
from response_parser import parser

#  Input: System read arguments from command line
# Output: User's input question
#   Misc: -h and --help return usage instructions
def checkArgs(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:', ['help', 'question='])
    except getopt.GetoptError:
        print('main.py -i "Your question here."')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('usage: main.py -i "Your question here."')
            print('       main.py --question "Your question here."')
            sys.exit()
        elif opt in ['-i', '--question']:
            inlineQuestion = inputCleanser(arg)
            return inlineQuestion

if __name__ == "__main__":
    inlineQuestion = checkArgs(sys.argv[1:])

    if inlineQuestion:
        userQuestion = inlineQuestion
    else:
        userQuestion = inputCleanser(input('What would you like to ask Google? '))

    htmlResponse = get_html(url=create_url(question=userQuestion))
    # print(htmlResponse)  # this is for testing

    googleAnswer = parser(soup=htmlResponse)
    print('Google says: {}'.format(googleAnswer))