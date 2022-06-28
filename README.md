# pyText-Html-Script
python script to convert notes or txt files to generate a html file

As I learn new things I'm constantly writing notes (Sublime Text is my go to text editor) and I got the idea, "You know what? It would be nice to be able to view my notes in a better to read format" 
*DISCLAIMER: CSS NOT INCLUDED.

HOW TO USE TextToHtml.py on linux:
save script in /usr/local/bin
chmod +x TextToHtml.py #make sure the script is executable
[in the terminal type the following commands:]
cd /usr/local/bin
TextToHtml.py /path/to/your/document.txt nameOfYourHtmlFileYouWantToCreate.html

The Script takes 2 command line arguments the first is your path to the document you want to convert into html format, the second is the name of the html document you want it to be saved as

YOUR .txt FORMAT
if you want a header, then the line in your notes MUST be all uppercase letters (if there is any special characters or lower case letters, the regex I used will not convert it into a header)
if you want a  list your list must start with a -
so far this is the only functionality I needed or wanted and serves my purposes so far

Ex.

THIS WILL BE CONVERTED TO A HEADING
This is a paragraph and 
will be formatted exactly as it
is typed as I used a tag to help
keep the notes I write intact as written

This is my list:
  -My list Item
  -My second list item
  -My third list item
