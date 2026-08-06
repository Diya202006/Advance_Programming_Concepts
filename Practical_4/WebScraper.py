import re
 
def extract_urls(html):
    pattern = r'(https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}[^\s"\'>]*|www\.[A-Za-z0-9.-]+\.[A-Za-z]{2,}[^\s"\'>]*)'
    urls = re.findall(pattern, html)
    return urls
 
html = input("Enter HTML content:\n")

url_list = extract_urls(html)

if len(url_list) > 0:
    print("\nExtracted URLs:")
    for url in url_list:
        print(url)
else:
    print("No valid URLs found.")