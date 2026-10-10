import re
from bs4 import BeautifulSoup

html_content = """
<html> 
<head> 
<title>My first web page</title> 
</head> 
<body> 
<h1>My first web page</h1> 
<h2>What this is tutorial</h2> 
<p>A simple page put together using HTML. <em>I said a simple page.</em>.</p> <ul> 
    <li>To learn HTML</li> 
    <li> 
        To show off 
        <ol> 
            <li>To my boss</li> 
            <li>To my friends</li> 
            <li>To my cat</li> 
            <li>To the little talking duck in my brain</li> 
        </ol> 
    </li> 
    <li>Because I have fallen in love with my computer.</li> 
</ul> 
<h3>Where to find the tutorial</h3> 
<p><a href="http://www.aaa.com"><img src=http://www.aaa.com/badge1.gif></a></p> 
<h4>Some random table</h4> <table> 
    <tr class="tutorial1"> 
        <td>Row 1, cell 1</td> 
        <td>Row 1, cell 2<img src=http://www.bbb.com/badge2.gif></td> 
        <td>Row 1, cell 3</td> 
    </tr> 
    <tr class="tutorial2"> 
        <td>Row 2, cell 1</td> 
        <td>Row 2, cell 2</td> 
        <td>Row 2, cell 3<img src=http://www.ccc.com/badge3.gif></td> 
    </tr> 
</table> 
</body> 
   </html> 
"""

soup = BeautifulSoup(html_content, "html.parser")

# a [2 points]. Print the text of the <title> element by navigating the HTML tags. 
print(f'\n[A] Title: {soup.title.text}\n')

# b.[2 points]. Print the text of the second <li> element inside the <ol> below "To show off" by navigating the HTML tags. 
print(f'[B] Second <li> in <ol>: {soup.find("ol").find_all("li")[1].text}\n')

# c.[2 points]. Print all <td> elements in the first <tr> row of the table by navigating the HTML tags. 
print(f'[C] All <td> in first <tr>: {soup.find("tr").find_all("td")}\n')
# d.[2 points]. Print the text of the <h2> element that contains the word "tutorial" by navigating the HTML tags and using a RegEx. 
print(f'[D] <h2> containing "tutorial": {soup.find("h2", string=re.compile("tutorial")).text}\n')

# e.[2 points]. Print all text nodes that contain the word "HTML" by using a RegEx. 
print(f'[E] Text nodes that contain word HTML: {[text for text in soup.stripped_strings if re.search("HTML", text)]}\n')

# f.[2 points]. Print all <td> elements in the second <tr> row of the table by navigating the HTML tags. 
print(f'[F] All <td> in second <tr>: {soup.find_all("tr")[1].find_all("td")}\n')
# g.[2 points]. Print all <img> tags contained within the <table> element by navigating the HTML tags. 
print(f'[G] All <img> tags in <table>: {soup.find("table").find_all("img")}\n')
