from bs4 import BeautifulSoup


def parser(soup):
    # Find the answer
    answer = soup.find("div", class_="BNeawe iBp4i AP7Wnd")

    # Clean The Answer and Create Conditon for No Answer
    if answer == None:
        return "Suprise! Google does not know the answer to that question!"
    else:
        return answer.text