filename = input("Please input the name of your file: ").strip().lower()

if filename.endswith(".jpeg") or filename.endswith("jpg"):
    print("image/jpeg")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
