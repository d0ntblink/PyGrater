from bs4 import BeautifulSoup


def parser(soup):
    # Find the answer
    answerBasic = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    answerAdv = soup.find("div", class_="BNeawe s3v9rd AP7Wnd")


    # Clean The Answer and Create Conditon for No Answer
    if answerBasic and answerAdv == None:
        return "Suprise! Google does not know the answer to that question!"
    elif (answerBasic == None) and (answerAdv != None):
    	return answerAdv.text
    elif (answerAdv == None) and (answerBasic != None):
    	return answerBasic.text