# pyText-Html-Script

Python script to convert notes or txt files to generate a html file

As I learn new things I'm constantly writing notes (Sublime Text is my go to text editor) and I got the idea, 
"You know what? It would be nice to be able to view my notes in a better to read format" 

### USAGE ON LINUX:
save script in /usr/local/bin
 ```sh
 cd /usr/local/bin
 ```
 ```sh
chmod +x TextToHtml.py
```
 ```sh
cd /usr/local/bin
```
 ```sh
TextToHtml.py /path/to/your/document.txt nameOfYourHtmlFileYouWantToCreate.html
```

The Script takes 2 command line arguments the first is your path to the document you want to convert into html format, 
the second is the name of the html document you want it to be saved as.
The html document will be saved in /usr/local/bin

## Format of your .txt file
If you want a header, then the line in your notes MUST be all uppercase letters 
(if there is any special characters or lower case letters, the regex I used will not convert it into a header)
if you want a  list your list must start with a -
so far this is the only functionality I needed or wanted and serves my purposes so far

Ex.
<pre>
THIS WILL BE CONVERTED TO A HEADING
This is a paragraph and 
will be formatted exactly as it
is typed as I used a pre tag to help
keep the notes I write intact as written

This is my list:
  -My list Item
  -My second list item
  -My third list item
