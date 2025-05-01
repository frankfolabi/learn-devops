# Introduction to Markdoen
You may wonder how README file are created? Well, it is written using the Markdown language. Interestingly, you can embed HTML to it.

Here is a quick review. 

### 1. Headings 
To create a title and increase the font size, use the \# to preface the statement. 
# `#` produces this h1 size
###### `######` This is the smallest with h6


### 2. Comments
Comments can be written by surronding your text with `<!-- -->`
<!-- This comment would not show in my file 
You can even have it on multiple lines -->


### 3. Lists

Unordered list
Use star `*` or hyphen `-` to create an unordered list
   * you can have a sub point
      * if you indent your star with few spaces
   - The dash - can also be used 
   + A plus + another one level

Ordered Lists
Use `1.`
1. first item
1. second item
1. third item


### 4. Italics

_How was this line italicize?_ Use the \_ on both ends of the lines_ or \*text here*

*This also italicize as well*


### 5. Bold

Use \**some text**

***This is bold italics*** with ***

**Here comes boldface text**
__another bold type__


### 6. Other Features

The backslash `\` is used to escape charaters.

![Display Image](/path/to/the/image.png)

[Link](/path/to/the/link)

`back tick is used for code snippets` 

```
This is for multiline codes
```


### 7. Table Creation

Would you like to create a table?
Name | Year
-|-
Linux|1991
Python|1991

- Another table 

| First column | Second column | Third column|
|--------------|---------------|-------------|
|item          |item           |item         |  
|another       |point          |items        |


### 8. Misc

&copy; Copyright symbol `&copy;`

&bull; This will create a dot

> This is a quoted text

Here is a<br />line break

The language syntax highlight effect:
```python
def colorful():
   print("Colourful code.")
return n
```


### 9 GFM - GitHub-Flavored Markdown

#### a. Checkboxes

- [X] This is marked
- [ ] This is unmarked


#### b. Templates

/template


#### c. Mentions

@username @team @frankfolabi


#### d. Emoji

:smile:

:wave:

:bow:


#### e. Coloured Text
Using HTML tags, colors can be displayed.

<div style="color: red;">This is red text</div>

<div style="color: blue;">This is blue text</div>

<div style="color: aqua;">This is aqua text</div>

<div style="color: orange;">This is orange text</div>

<div style="color: yellow;">This is yellow text</div>


#### f. Pull Requests or Issues

#123 can be used to link the PR or issue with that number.


#### g. Strikethrough
You can use double tildes (`~~`) to strike through text:
~~This text is crossed out~~





