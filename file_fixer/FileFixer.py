import os
def createFile(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def moveFile(folders,files):
    for file in files:
        os.replace(file, f"{folders}/{file}")
files=os.listdir()
files.remove("FileFixer.py")
createFile("Images")
createFile("Videos") #TODO: you can make a new folder as your own requirement
createFile("Documents")
createFile("Web Development")
createFile("Python File")
createFile("Others")
ImgExtensions=[".jpg",".png",".jpeg"]
Images = [file for file in files if os.path.splitext(file)[1].lower() in ImgExtensions]
VidExtensions=[".mp3",".mp4",".flv"]
Videos = [file for file in files if os.path.splitext(file)[1].lower() in VidExtensions]
DocExtensions=[".txt",".doc",".docx",".pdf",".csv"]
Documents=[file for file in files if os.path.splitext(file)[1].lower() in DocExtensions]
HtmlExtension=[".html",".css",".js"]
WebDevelopment=[file for file in files if os.path.splitext(file)[1].lower() in HtmlExtension]
pyExtensions=[".py"]
PythonFile=[file for file in files if os.path.splitext(file)[1].lower() in pyExtensions]
other=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in ImgExtensions) and (ext not in VidExtensions) and (ext not in DocExtensions) and (ext not in HtmlExtension) and (ext not in pyExtensions) and os.path.isfile(file):
        other.append(file)
print(other)
moveFile("Images",Images)
moveFile("Videos",Videos)
moveFile("Documents",Documents)
moveFile("Web Development",WebDevelopment)
moveFile("Python File",PythonFile)
moveFile("Others",other)