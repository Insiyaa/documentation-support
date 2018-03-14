from bs4 import BeautifulSoup as soup
from urllib.request import urlopen



def parseHTML(url):
    client = urlopen(url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html,"html.parser")
    return page_soup

def getnavList(page_soup):
    index = page_soup.find_all("div", {"class":"toctree-wrapper"})
    index_items = index[0].find_all("a", {"reference internal"})
    return index_items

def printNavList(index_items):
    for item in index_items:
        print(item.text)

def printDocdata(nav, nav_url, index_items):
    nav = nav.rstrip('.')
    k = len(nav)
    for item in index_items:
        if nav in item.text[:k]:
            div_id = item['href'].split("#",1)
            if len(div_id) == 2:
                div_id = div_id[1]
            else:
                div_id = None
            page_soup = parseHTML(nav_url + item['href'])
            req_div = page_soup.find_all("div",{"id":div_id})
            print(req_div[0].text)
            return
    print("Invalid choice!")


def main():
    
    while(1):
        print("1. Python 3.6\n2. Python 2.7")
        print("Enter your choice:")
        try:
            version = int(input())
        except:
            print("Invalid choice: Enter 1 or 2")
        if version == 1:
            while 1:
                nav_url = "https://docs.python.org/3/reference/"
                my_url = "https://docs.python.org/3/reference/index.html"
                page_soup = parseHTML(my_url)
                index_items = getnavList(page_soup)

                printNavList(index_items)
                print("Enter:")
                nav = input()
                if nav == "q":
                    flag = 0
                    break
                printDocdata(nav, nav_url, index_items)
                print("q: quit\nl: documentation menu\nc: change python version")
                choice = input()
                if choice == "q":
                    flag = 0
                    break
                elif choice == "l":
                    continue
                elif choice == "c":
                    flag = 1
                    break

        elif version == 2:
            while 1:
                nav_url = "https://docs.python.org/2.7/reference/"
                my_url = "https://docs.python.org/2.7/reference/index.html"
                page_soup = parseHTML(my_url)
                index_items = getnavList(page_soup)

                printNavList(index_items)
                print("Enter:")
                nav = input()
                if nav == "q":
                    flag = 0
                    break
                printDocdata(nav, nav_url, index_items)
                print("q: quit\nl: documentation menu\nc: change python version")
                choice = input()
                if choice == "q":
                    flag = 0
                    break
                elif choice == "l":
                    continue
                elif choice == "c":
                    flag = 1
                    break
        else:
            print("Invalid choice")
            continue
        
        if flag == 0:
            break

            
if __name__ == "__main__":
    main()
    