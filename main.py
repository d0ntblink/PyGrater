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

import functions
from google_page_pull import create_url, get_html

if __name__ == "__main__":
    userQuestion = functions.inputCleanser(input('What would you like to ask Google? '))

    htmlResponse = get_html(url=create_url(question=userQuestion))
    # print(htmlResponse)  # this is for testing

    googleAnswer = 'LOL'  # obviously replace this with the parsed output
    print('Google says: {}'.format(googleAnswer))