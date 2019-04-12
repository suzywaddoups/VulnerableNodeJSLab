#!/usr/bin/python3

#pip install colorama
import requests
import smtplib
from colorama import Fore, Style
import time
import base64

#TO CHANGE PASSWORD: base64 encoded new email password
emailAccount = '<<Enter New Email Address>>'
emailPassword = <<Enter New base64 Encoded Email Password>>

#Email that will recieve the students' scores on the hard Difficulty
hardDifficultySubmit = '<<Enter New Email Address>>'

#TO CHANGE PASSWORD: base64 encoded new passwords for easy & normal difficulty settings
#default password for easy difficulty mode = enableEasy
easyDifficultyPassword = <<Enter New base64 Encoded Easy Difficulty Password>>
#default password for normal difficulty mode = enableNormal
normalDifficultyPassword = <<Enter New base64 Encoded Normal Difficulty Password>>


def gradeSQLi(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 31)
    print("Grading SQLi usersearch page...")
    print("=" * 31 + Style.NORMAL)

    url = "http://localhost:8080/usersearch"
    try:
        #Make Web Request
        data = {"login": "' UNION SELECT password, login from Users where login='davidc'-- //"}
        r= requests.post(url, data=data)
        body_data =r.text

        #Search for username in output
        if (body_data.find('davidc') !=-1):
            result=body_data.find('davidc')
            username=True
        else:
            username=False

        if (body_data.find('e10adc3949ba59abbe56e057f20f883e') !=-1):
            result=body_data.find('e10adc3949ba59abbe56e057f20f883e')
            hash=True
        else:
            hash=False

        message = "-" * 40 + '\n'
        message = message + "Grade for Usersearch: \n"
        message = message + "-" * 40 + '\n'

        if(username & hash):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SQL Injection Vulnerability was NOT fixed')

            message = message + "(0/1) FAIL: SQL Injection Vulnerability was NOT fixed. \n"

            if (difficulty == "1"):
                print("  HINT: Edit the query for the 'userSearch' module in core/appHandler.js")
                print("    (use 'db.User.find' instead of 'var query = SELECT ...')")


        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SQL Injection Vulnerability is fixed')
            message = message + "(1/1) PASS: SQL Injection Vulnerability was fixed! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to successfully make HTTP Request')
        message = 'Error: Failed to successfully make HTTP Request\n'
    return message



def gradeXSS(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 28)
    print("Grading XSS products page...")
    print("=" * 28 + Style.NORMAL)

    url = "http://localhost:8080/products"

    try:
        #Make Web Request
        data = {"name": "<script>alert('xss')</script>"}
        r= requests.post(url, data=data)
        body_data =r.text
        request_header = r.headers
        request_header = str(request_header)

        if (body_data.find('&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;') !=-1):
            if (difficulty == "1" or difficulty == "2"):
                print (Fore.GREEN + 'PASS: '+ Fore.WHITE +"XSS Vulnerability was successfully fixed" )
            vulnfixed=True

        elif (body_data.find("<script>alert('xss')</script>") !=-1):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +"XSS Vulnerabiltiy still exists")
            vulnfixed=False

            if (difficulty == "1"):
                print("  HINT: Edit the products.ejs view to escape 'output' expressions")
                print("    (use '<%=')\n" )

        else:
            print(Fore.RED + 'ERROR: '+ Fore.WHITE + "An Error occurred and the script could not determine if the XSS Vulnerability was fixed or not")
            return

        #check if x-xss header is enabled
        if (request_header.find("X-XSS-Protection': '1; mode=block") !=-1):
            if (difficulty == "1" or difficulty == "2"):
                print (Fore.GREEN + 'PASS: '+ Fore.WHITE +"X-XSS Protection Header was enabled")
            headerfixed=True
        elif (body_data.find("X-XSS-Protection': '1; mode=block") ==-1):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE + "X-XSS Protection Header was NOT enabled")
            headerfixed=False

            if (difficulty == "1"):
                print("  HINT: Edit the script.js file to include the xxs protection module")
                print("    (require 'x-xss-protection' and set the xxs protection header using 'app.use')\n" )

        else:
            Print(Fore.RED + 'FAIL: '+ Fore.WHITE +"An Error occurred and the script could not determine if the XSS Protection Header was enabled or not")
            return

        message = "-" * 40 + '\n'
        message = message + "Grade for Products: \n"
        message = message + "-" * 40 + '\n'

        if(vulnfixed == False):
            message = message + "(0/1) FAIL: XSS Vulnerability was NOT fixed. \n"

        if(vulnfixed == True):
            message = message + "(1/1) PASS: XSS Vulnerability was fixed! \n"

        if(headerfixed == False):
            message = message + "(0/1) FAIL: XSS Protection Header was NOT enabled. \n"

        if(headerfixed == True):
            message = message + "(1/1) PASS: XSS Protection Header was enabled! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to successfully make HTTP Request')
        message = 'Error: Failed to successfully make HTTP Request\n'
    return message



def sendEmail(emailRecipient, subject, message):
    # smtplib module send mail
    TO = emailRecipient
    SUBJECT = subject
    TEXT = subject + '\n' + message

    # Gmail Sign In
    gmail_sender = emailAccount

    passEncoded = emailPassword
    passDecoded = base64.b64decode(passEncoded)
    passDecodedStr = passDecoded.decode("utf-8")

    gmail_passwd = passDecodedStr


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(gmail_sender, gmail_passwd)
    except:
        print(Fore.RED + 'ERROR: '+ Fore.WHITE + "Could not login to Mail Server")

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('\nEmail was successfully sent to ' + emailRecipient)
    except:
        print (Fore.RED + 'ERROR: '+ Fore.WHITE +'Could not send email')

    print("\nExiting in 5 seconds...")
    time.sleep(5)
    server.quit()

def main():
    emailMessage = ""

    difficultyMenu = True
    while (difficultyMenu == True):
        print("\n" +"-" *77)
        difficulty = input("Welcome to the Cyber Tower Defense Grader.  Please select a difficulty level: \
                            \n (1) Easy - Hints Provided & Unlimited Number of Tries \
                            \n (2) Normal - No Hints & Unlimited Number of Tries \
                            \n\n (3) Hard - No Hints & Limited Number of Tries \
                            \n\n To Exit Program (exit) \
                            \n \nEnter 1, 2, or 3: ")
        print("\n\n")

        if(difficulty == "1"):
            #User must enter password to use easier modes
            easyModePassword = input("Please Enter Password to use this Mode: ")
            easyModePassword = easyModePassword.encode()
            userInputEncoded = base64.b64encode(easyModePassword)

            if (userInputEncoded == easyDifficultyPassword):
                print("\n\n")
                emailMessage = "(Difficulty: Easy) \n"
                difficultyMenu = False
            else:
                print(Fore.RED + "\nInvalid Password\n\n"+ Fore.WHITE)
                continue

        elif(difficulty == "2"):
            #User must enter password to use easier modes
            normalModePassword = input("Please Enter Password to use this Mode: ")
            normalModePassword = normalModePassword.encode()
            userInputEncoded = base64.b64encode(normalModePassword)

            if (userInputEncoded == normalDifficultyPassword):
                print("\n\n")
                emailMessage = "(Difficulty: Normal) \n"
                difficultyMenu = False
            else:
                print(Fore.RED + "\nInvalid Password\n\n"+ Fore.WHITE)
                continue

        elif(difficulty == "3"):
            emailMessage = "(Difficulty: Hard) \n"
            difficultyMenu = False

        elif(difficulty in ("4", "Exit", "EXIT", "exit", "e", "E", "Ex", "EX", "ex")):
            return

        else:
            print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
            continue

    graderMenu = True
    while (graderMenu == True): # repeat forever unless it reaches "break" or "return"
        print("-" *44)
        grader = input("Select which module would you like to grade: \
                        \n\n (1) Grade Usersearch for SQLi \
                        \n\n (2) Grade Products for XSS \
                        \n\n (3) Grade both Usersearch and Products \
                        \n\nEnter 1, 2, or 3: ")

        print("\n\n")

        #HARD difficulty: gather email info before grading
        if (difficulty == "3"):
            #User input for student Name
            studentName = input("Your Full Name(s): ")
            #user input for where to email results
            emailRecipient = hardDifficultySubmit
            print("\n\n")

        if(grader == "1"):
            subject = "'s SQLi Grade"
            emailMessage = emailMessage + gradeSQLi(difficulty)
            graderMenu = False

        elif(grader == "2"):
            subject = "'s XSS Grade"
            emailMessage = emailMessage + gradeXSS(difficulty)
            graderMenu = False

        elif(grader == "3"):
            subject = "'s SQLi & XSS Grade"
            emailMessage = emailMessage + gradeSQLi(difficulty)
            emailMessage = emailMessage + gradeXSS(difficulty)
            graderMenu = False

        else:
            print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
            continue

        #EASY/NORMAL Difficulty: Ask if Student would like to submit/email results and Send if True
        if (difficulty == "1" or difficulty == "2"):
            emailMenu = True
            while (emailMenu == True): # repeat forever unless it reaches "break" or "return"
                print("\n" + "-" *41)
                studentSubmitResponse = input("Would you like to submit results? (Y/N): ")

                if(studentSubmitResponse in ("Y", "y", "YES", "Yes", "yes")):
                    #User input for student Name
                    studentName = input("Your Full Name(s): ")
                    #user input for where to email results
                    emailRecipient = input("Email To Send Results To: ")
                    #email subject
                    subject = studentName + subject
                    #send results to email
                    sendEmail(emailRecipient, subject, emailMessage)
                    return
                elif(studentSubmitResponse in ("N", "n", "NO", "No", "no")):
                    print("Exiting without Submitting...")
                    return
                else:
                    print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
                    continue

        if (difficulty == "3"):
            #Auto send Results
            #email subject
            subject = studentName + subject
            #send results to email
            sendEmail(emailRecipient, subject, emailMessage)
            return


if __name__ == "__main__":
    main()
