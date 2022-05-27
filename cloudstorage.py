import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        #link the our dropbox account to the application
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        #upload these contents to the dropbox using the files_upload() method
        dbx.files_upload(f.read(),file_to  )
def main():
    access_token = "sl.BHamJM-snrnBX8wiQgtLW-XaEusxBtXum1iqr8-ppTvHonLGbCP-q6UB9KT7ncwyycZsLj3zuNV1JqrfTri5jYbGWTcqztqPxOgAW8kWI9POAdyLaH1fUsHuH-P50oFrdI-wbFZRPnc"
     #creating object for class
    td = TransferData(access_token)
    file_from = input("Enter file name to transfer: ")
    file_to = input("Enter path to upload to dropbox: ")
    
    #function defined in the class "TransferData" is called
    td.uploadFile(file_from, file_to)
    print("Files successfully moved")
main()