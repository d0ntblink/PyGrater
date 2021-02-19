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
import google_page_pull


if __name__ == "__main__":
    userQuestion = functions.inputCleanser(input('What would you like to ask Google? '))

    htmlResponse = google_page_pull.pagePull(userQuestion)
    # print(htmlResponse)  # this is for testing

    googleAnswer = 'LOL'  # obviously replace this with the parsed output
    print('Google says: {}'.format(googleAnswer))