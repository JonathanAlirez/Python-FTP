from ftplib import FTP
from check import CheckCommand #get my check method
import getpass
import sys
import os

def MainConnection():
    #Check if command line arguments have been given for connections
    if (len(sys.argv) == 2): #if only python, website
        ftpWebsiteConnection = sys.argv[1] 
        ftpUsername = input("Username: ") #need username
    elif (len(sys.argv) == 3): #if python, website, username
        ftpWebsiteConnection = sys.argv[1]
        ftpUsername = sys.argv[2]
    else:
        #No arg given for website ask for it here
        ftpWebsiteConnection = input("FTP Connection: ")
        print("Connecting to: ", ftpWebsiteConnection)
        #Get username and password variables
        ftpUsername = input("Username: ")
    #Always going to need to ask for password
    ftpPassword = getpass.getpass("Password: ")
    FtpConnect(ftpWebsiteConnection, ftpUsername, ftpPassword)

def FtpConnect(ftpWebsite, ftpUsername, ftpPassword):
    try :
        #try to connect, if error it will give error
        #or else it will print the servers welcome message
        ftp = FTP(ftpWebsite)
        ftp.login(ftpUsername, ftpPassword)
        print(ftp.getwelcome())
        ConnectedToServer(ftp)
    except :
        End()

#loops until the user types in bye or exit
def ConnectedToServer(ftp):
    try :
        notExit = False
        while (notExit == False):
            cmd = input(">> ")
            if (cmd == "bye" or cmd =="exit"):
                notExit = True
            else:
                #method from Check.py that takes a FTP and string
                CheckCommand(ftp, cmd)
    except :
        try :
            #double check if the connection is still open
            ftp.voidcmd("NOOP")
            #connection is still open, so error command has been typed in
            ErrorCmd()
        except :
            #message to show timeout has occurred
            Timeout()

def ErrorCmd():
    print("Error, wrong command entered...")
    
def Timeout():
    print("Connection has timed out...")

def End():
    print("ERROR: wrong credentials have been given...");
    MainConnection()

MainConnection()
