import re

def main():
    HTML = input("HTML: ")
    print(parse(HTML))

def parse(link):
    if matches := re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', link):
        return "https://youtu.be/" + matches.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
