def main():
    file_name = input("File name: ").strip().lower()
    if file_name[-5:] == ".jpeg":
        print ("image/jpeg")
    elif file_name[-4:] == ".gif":
        print("image/gif")
    elif file_name[-4:] == ".jpg":
        print("image/jpeg")
    elif file_name[-4:] == ".png":
        print("image/png")
    elif file_name[-4:] == ".pdf":
        print("application/pdf")
    elif file_name[-4:] == ".txt":
        print("text/plain")
    elif file_name[-4:] == ".zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()
