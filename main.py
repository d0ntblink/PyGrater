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

from string_beautifier import inputCleanser
from google_page_pull import create_url, get_html
from response_parser import parser

if __name__ == "__main__":
    userQuestion = inputCleanser(input('What would you like to ask Google? '))

    htmlResponse = get_html(url=create_url(question=userQuestion))
    # print(htmlResponse)  # this is for testing

    googleAnswer = parser(soup=htmlResponse)
    print('Google says: {}'.format(googleAnswer))