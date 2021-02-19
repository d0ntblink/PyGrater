#  https://github.com/d0ntblink/pygrater/
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



if __name__ == "__main__":
    userQuestion = functions.inputCleanser(input('What would you like to ask Google? '))

    print(userQuestion)