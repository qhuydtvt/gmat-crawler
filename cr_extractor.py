from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def extract(link):
    soup = BeautifulSoup(urlopen(link).read().decode('utf8'), "html.parser")

    for div in soup.find_all("div", {'style':'border: 1px solid black; padding: 10px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);'}): 
        div.decompose()
    
    div = soup.find("div", "item text")
    stimulus = div.contents[0].strip()
    print(stimulus)
    # print(div.contents[1])
    
    stem_and_choice = str(re.search(r'<br>(.*?)(E.)(.*?)(<)', str(div.contents[1]), re.DOTALL).group(0))

    # print(stem_and_choice)
    print(str(re.search(r'<br>(.*?)(A.)', stem_and_choice).group(0)).replace("A.", "").replace("<br>",""))
    print(str(re.search(r'(A\.)(.*?)(B\.)', stem_and_choice).group(0)).replace("A.", "").replace("B.",""))
    print(str(re.search(r'(B\.)(.*?)(C\.)', stem_and_choice).group(0)).replace("B.", "").replace("C.",""))
    print(str(re.search(r'(C\.)(.*?)(D\.)', stem_and_choice).group(0)).replace("C.", "").replace("D.",""))
    print(str(re.search(r'(D\.)(.*?)(E\.)', stem_and_choice).group(0)).replace("D.", "").replace("E.", "").replace("<br/>",""))
    print(str(re.search(r'(E\.)(.*?)(<)', stem_and_choice, re.DOTALL).group(0)).replace("E.", "").strip())
    
    # print(stem_and_choice)
    

    # # print(div.find(text=True).strip())
    
    # # with open("table.html", "w") as f:
    # #     f.write(soup.prettify())
    
    # #right_tds = post_table.find_all('td', 'right')
    # #print(right_tds[0].prettify())

if __name__ == "__main__":
    extract("https://gmatclub.com/forum/in-mernia-commercial-fossil-hunters-often-sell-important-fossils-they-243489.html")