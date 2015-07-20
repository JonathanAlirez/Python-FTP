from ftplib import FTP
import progressbar #progressbar 2.3
import os

#check the command the user has typed in and see if it fits any
def CheckCommand(ftp, command):
    if(command == "ls" or command == "dir"):
        ftp.retrlines('LIST')
    elif(command == "pwd"):
        print(ftp.pwd())
    elif(command == "bye" or command == "exit"):
        ftp.quit();
    #command[0:2] splits up string
    elif(command[0:2] == "cd"):
        try :
            ftp.cwd(command[3:len(command)])
        except :
            Error()
    #chd - current home directory
    elif(command[0:3] == "chd"):
        try :
            os.chdir(command[4:len(command)])
        except :
            Error()
    elif(command[0:6] == "getchd"):
        try :
            print(os.getcwd())
        except :
            Error()
    elif(command[0:4] == "grab"):
         try :
            filename = command[5:len(command)]
            fileSize = ftp.size(filename)
            progress = progressbar.AnimatedProgressBar(end=fileSize, width=50)
            with open(filename, 'wb') as f:
                def callback(chunk):
                    f.write(chunk)
                    progress + len(chunk)
                    progress.show_progress()
                ftp.retrbinary('RETR ' + filename, callback)
            print()
         except :
            Error()
    elif(command[0:3] == "put"):
        try :
            filename = command[4:len(command)]
            ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
        except :
            error()
    elif(command[0:5] == "mkdir"):
        try :
            ftp.mkd(command[6:len(command)])
        except :
            Error()
    elif(command[0:3] == "del"):
        # try and delete as a file, if not...
        try :
            ftp.delete(command[4:len(command)])
        except :
            #try and delete as a directory
            try :
                ftp.rmd(command[4:len(command)])
            except :
                print("Directory not empty")
    elif(command[0:6] == "rename"):
        try :
            rest = command.split()
            ftp.rename(rest[1], rest[2])
        except :
            Error()
    elif(command[0:2] == "mv"):
        try :
            rest = command.split()
            ftp.rename(rest[1], rest[2])
        except :
            Error()
    else:
        Error()
            
def Error():
    print("Wrong command has been typed")
