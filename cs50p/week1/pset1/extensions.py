"""This program gives the extension of a file base on the last letter of tis name"""
x = input("File name:")
if ".gif" in x.lower().strip()[-5:]:
    print("image/gif")
elif ".jpg" in x.lower().strip()[-5:] or ".jpeg" in x.lower().strip()[-5:] :
    print("image/jpeg")
elif ".pdf" in x.lower().strip()[-5:]:
    print("application/pdf")
elif ".png" in x.lower().strip()[-5:]:
    print("image/png")
elif ".txt" in x.lower().strip()[-5:]:
    print("text/plain")
elif ".zip" in x.lower().strip()[-5:]:
    print("application/zip")
else:
    print("application/octet-stream")