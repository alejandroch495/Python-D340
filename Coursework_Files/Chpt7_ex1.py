# Alejandro Chavez
# Chapter 7 exercise 1
# Error log reader
from io import TextIOWrapper # Imported to declare type in functions

line_count: int = 0
error_count: int = 0
error_lines: list[str] = []

def main():
    "Main"
    file = findfile() # find file
    getErrors(file) # pull errors
    print(f"Total lines = {line_count}") # print total lines
    for line in error_lines: # print any errors found
        print(line)
    print(f"errorLines count = {error_count}") # print total errors found
    exportErrors(error_lines)   # export into file
    file.close()    # close file found

def get_user_input() -> str:
    "Used to get user input and remove trailing spaces"
    user_input = input('enter the error log file name : ').strip()
    return user_input

def findfile() -> TextIOWrapper:
    "Returns the file if it is found else it will ask for a different file name."
    file_found = False
    while file_found == False:
        user_input = get_user_input()
        try:
            file = open(user_input, "r")
            file_found = True
        except:
            print(f"'{user_input}' does not exist.\n Possible spelling error?")
    return file

def getErrors(file : TextIOWrapper):
    "reads through the file passed through and counts line that are not empty. counts 'error' lines and stores them"
    global line_count
    global error_count
    global error_lines
    for line in file:
        line = line.strip()
        if line != "":
            line_count += 1
            if "error" in line.lower():
                error_count += 1
                error_lines.append(line)

def exportErrors(error_list):
    "opens/creates a file called 'reportError.txt' with the total lines, total errors, and the error lines."
    error_file = open("reportError.txt","w")
    error_file.write(f"Total lines count :{line_count}\nError Count :{error_count}\n")
    for line in error_list:
        error_file.write(line+"\n")
    error_file.close()



if __name__ == "__main__":
    main()

    """
    Output
enter the error log file name : error.log
'error.log' does not exist.
 Possible spelling error?
enter the error log file name : error.txt
'error.txt' does not exist.
 Possible spelling error?
enter the error log file name : errorlog.txt
Total lines = 108
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018]
"""