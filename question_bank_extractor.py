from bs4 import BeautifulSoup
from urllib.request import urlopen

link = "https://gmatclub.com/forum/the-official-guide-for-gmat-review-242995.html"

if __name__ == "__main__":
    html_text = urlopen(link).read().decode('utf8')
    soup = BeautifulSoup(html_text, "html.parser")
    box_divs = soup.find_all("div", style="border: 1px solid black; padding: 10px; background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
    
    text = ""
    for box_div in box_divs:
        title_div = box_div.find("span", style="font-style: italic")
        if title_div:
            text += title_div.string + ":\n"
        else:
            for a_post_link in box_div.find_all("a", "postlink"):
                if a_post_link:
                    text += a_post_link['href'] + "\n"
            
    with open("gmat_question_links.txt", "w") as f:
        f.write(text)
