import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        #link the our dropbox account to the application
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for i in files:
                localpath = os.path.join(root, i)
                relativepath = os.path.relpath(localpath, file_from)
                dropboxpath = os.path.join(file_to, relativepath)
               # upload the file
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxpath, mode=WriteMode('overwrite'))


def main():
    access_token = "sl.BHZuld6mNcoFSIRg7vvSfqpLgh496-Rky2aOgM4RrkLri0fyDEFahfIaEQCjmUawfgfbIPVSfto7nSwstidYVca0k-k_lBTaqJdes3rYBHt6SwQPAHoyBzPR7nChW7Nvo360G4WyBVU"
     #creating object for class
    td = TransferData(access_token)
    file_from = input("Enter file name to transfer: ")
    file_to = input("Enter path to upload to dropbox: ")
    
    #function defined in the class "TransferData" is called
    td.uploadFile(file_from, file_to)
    print("Files successfully moved")
main()