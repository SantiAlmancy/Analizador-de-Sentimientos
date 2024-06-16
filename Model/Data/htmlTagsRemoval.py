from bs4 import BeautifulSoup

def remove_html_tags(input_string):
    soup = BeautifulSoup(input_string, 'html.parser')
    return soup.get_text()

# Example usage:
html_string = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
cleaned_text = remove_html_tags(html_string)
print(cleaned_text)  # Output: "This is bold and italic text."
