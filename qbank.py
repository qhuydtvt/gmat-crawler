from bs4 import BeautifulSoup
from urllib.request import urlopen

link = "https://gmatclub.com/forum/the-official-guide-for-gmat-review-242995.html"

def get_question_links():
    html_text = urlopen(link).read().decode('utf8')
    soup = BeautifulSoup(html_text, "html.parser")
    box_divs = soup.find_all("div", style="border: 1px solid black; padding: 10px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
    
    question_sets = {}
    title = ""
    question_sets[""] = []
    for box_div in box_divs:
        title_div = box_div.find("span", style="font-style: italic")
        if title_div:
          title = title_div.string.strip()
          question_sets[title] = []
        else:
          for a_post_link in box_div.find_all("a", "postlink"):
            if a_post_link:
              question_sets[title].append(a_post_link['href'])
    
    return question_sets

if __name__ == "__main__":
    quesion_set_links = get_question_links()
    print(quesion_set_links["Critical Reasoning"])
