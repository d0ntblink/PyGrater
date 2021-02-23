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
    USAGE = 'usage: main.py -i "Your question here."\n' \
            '       main.py --question "Your question here."\n\n' \
            'NOTE: Double quotes ("") are required surrounding your question.'

    try:
        options, arguments = getopt.getopt(
            argv,                    # Arguments
            'hi:',                   # Short Options
            ['help', 'question='])   # Long Options
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    for opt, arg in options:
        if opt in ['-h', '--help']:
            print(USAGE)
            sys.exit()
        elif opt in ['-i', '--question']:
            inlineQuestion = inputCleanser(arg)
            return inlineQuestion
    _ = arguments  # please stop bugging me about the unused variable

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