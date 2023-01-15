# phddsf22m001scraper-- Assignment 01

A web scraping library that allows you to extract information from HTML pages using CSS selectors.

## Installation

```bash
pip install phddsf22m001scraper
```

## Usage

**Example Use 01:**

```python
import phddsf22m001scraper as myscraper

css_selectors = {
    'title': 'title',
    'div': 'div'
}

result = myscraper.web_scraper("https://example.com", css_selectors)

print(result)
```

Output:

```
{'title': [<title>Example Domain</title>], 'div': [<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>]}
```

**Example Use 02:**

```python
import phddsf22m001scraper as myscraper
url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
css_selectors = {
    "title": "h3>a"
   
}
result = myscraper.web_scraper(url, css_selectors)
booklinks= result['title']
for link in booklinks:
    print (link.text)
```

Output:

```
A Light in the ...
Tipping the Velvet
Soumission
Sharp Objects
Sapiens: A Brief History ...
The Requiem Red
The Dirty Little Secrets ...
The Coming Woman: A ...
The Boys in the ...
The Black Maria
Starving Hearts (Triangular Trade ...
Shakespeare's Sonnets
Set Me Free
Scott Pilgrim's Precious Little ...
Rip it Up and ...
Our Band Could Be ...
Olio
Mesaerion: The Best Science ...
Libertarianism for Beginners
It's Only the Himalayas
```

## Arguments

- `url`: The URL of the HTML page to scrape
- `css_selectors`: A dictionary of keys and values representing the element name and the corresponding CSS selector to use

## Returns

- A dictionary of element names and the corresponding list of element(s) extracted from the HTML page

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.