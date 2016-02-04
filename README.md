# nudi
This is a HTML parser for Telugu crossword puzzle

This program needs python on your computer. If you don't have python, you can visit the following page and download the same.
https://www.python.org/downloads/

How to check if Python is present on your computer?
===================================================

Windows
--------
Go to command prompt and type the command "python"

Linux/Mac
--------
Open up your terminal and run the command "python"

If they open up a prompt with >>> then you already have python installed on your computer!

How to use it?
==========================================
You need two inputs for this program. 
One is the key file. A sample file (*key.txt*) is present in the same directory. This is actually the correct answers for each cell seperated by a new line

Another is the HTML input file, which can be generated from the mail that you send. Open the RAW HTML format for your email. If you are using gmail, you can click on the right side button and click "Show original". Detailed steps at https://support.google.com/mail/answer/22454?hl=en

A sample HTML file (*input.html*) is present in this repository.

Finally run the following command

*python nudi.py key.txt input.html*



