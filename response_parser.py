from bs4 import BeautifulSoup


def parser(soup):
    # Find the answer
    answerBasic = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    answerAdv = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")

    # Clean The Answer and Create Conditon for No Answer
    if (answerBasic and answerAdv) != None:
        return(answerBasic.text)
    elif (answerBasic == None) and (answerAdv != None):
        return(answerAdv.text)
    else:
        return("Google Does Not Know!")

    
  
  