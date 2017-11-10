import shutil, os

def combine_files(abfolder):
    extensions = ["mp3", "wma"]
    i = 1

    os.chdir(abfolder)
    if not os.path.exists(abfolder + "\\" + "All"):
        os.makedirs(abfolder + "\\" + "All")
    for folderName, subfolders, filenames in os.walk(abfolder):
        for filename in filenames:
            if filename[-3:] in extensions:
                print(abfolder + "\\" + "All" + "\\" + "%03d" % i + " - " + filename)
                shutil.copy(os.path.join(folderName, filename),
                                abfolder + "\\" + "All" + "\\" + "%03d" % i + " - " + filename)
                i += 1
    print("Successfully combined " + str(i) + "files into " + abfolder + "\\" + "All")

combine_files("E:\Books (Audio and eBooks)\Audio Books\Gift of Fear")