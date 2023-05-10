import webbrowser as wb
import os
def workauto():
    code_path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
    os.startfile(code_path)
    Chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = ("udemy.com",
            "github.com",
            "Kaggle.com",
            "https://lms.cuonlineedu.in/Users/home",
            "linkedin.com"
            )
    for url in URLS:
        wb.get(Chrome_path).open(url)
workauto()