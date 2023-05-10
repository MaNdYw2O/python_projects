#importing modules with aliases
import webbrowser as wb
import os



def workauto():   # defining function
    code_path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"   # making variable name of path which we want to run
    os.startfile(code_path)
    Chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # setting up browser path which we wanted to use 
    URLS = ("udemy.com",
            "github.com",
            "Kaggle.com",                                      #here are some of the urls we set which we are using
            "https://lms.cuonlineedu.in/Users/home",
            "linkedin.com"
            )
    for url in URLS:
        wb.get(Chrome_path).open(url)             # here we perform for loop to iterate over webs and open browser and then open url
        
workauto()    # calling function
