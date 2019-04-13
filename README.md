# Cyber Tower Defense: Vulnerable NodeJS Lab
The purpose of this NodeJS web application is to help you gain experience modifying source code to harden a website against some of the most common web vulnerabilities.  The vulnerable web application contains three pages: a homepage, a page susceptible to SQL injection (SQLi), and a page susceptible to cross-site scripting (XSS).  


To help instruct on what must be done to secure the vulnerable web application, we have created a lab scenario document, as well as a lab walkthrough for the following web vulnerabilities:

      1. SQL Injection (SQLi) 
      2. Cross-Site Scripting (XSS)

The vulnerable web application's setup, scenario, and lab walkthrough documents can be downloaded using the following link: 
https://byu.box.com/s/cjuwu57xqxbvqomevmyurat0a37drqif 


The lab scenario document contains a background story for why the vulnerable web application must be fixed.  The document also contains instructions for how to run the grading script which will check if the web vulnerabilities have properly been fixed.  


The web application lab’s grading script is written in Python and will run two scripted attacks.  The first will check if the SQL injection vulnerability has been fixed, and the second will check if the XSS vulnerability has been fixed.  In the repository's "grading_scritps" folder is a python grading script called "auto_grader.py".  After editing the source code to fix the two vulnerabilities, the python grading script should be used to check that the web app vulnerabilities were appropriately fixed.


We have also created a vulnerable VM that already contains the vulnerable NodeJS application.  The packaged vulnerable web application VM can be downloaded using the following link: 
https://byu.box.com/s/gbqv2ddhdy7v1pjc5wcy7sstunuwmvbc  

