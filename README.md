# Python-FTP
Using python to FTP into remote servers

#Use
Python-FTP is used by allow someone to use FTP to transfer files to a remote server.
it supports all commands normally used in a FTP session. this program does allow for up to 2 command line arguments<br />
1st argument always has to be the website (first argument)<br />
2nd argument can only be the username for the website
```
python pftp.py www.example.com
python pftp.py www.example.com user
NOTICE: cannot switch argument location
Do not do:
python pftp.py user www.example.com
```

#List of Commands
```
ls/dir - give a list of the current working directory
pwd - print the path of the current working directory
bye/exit - exit the server
cd (string location) - change the current working directory
chd (string) - change the current home directory
getchd - display the current home directory
grab (string filename )- download a file to the current home directory
put (string filename) - upload a file to the current working directory from the current home directory
mkdir (string directoryname) create a new directory in the current working directory
del (string filename/directoryname) - deletes either a file or directory depending on what is passed through
rename (string oldfile, string newfile) - renames the oldfile with the newfile
mv (string oldpath, string newpath) - moves the file at the oldpath to the newpath
```

# Considerations for further implementations
I would like to this this application get a way to allow for sftp,
as well as one day get a GUI application part so that people will have an easier time using this application.
