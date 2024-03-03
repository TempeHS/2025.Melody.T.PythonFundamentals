#  prompts the user for the name of a file and then outputs that file’s media type
# .gif .jpg .jpeg .png .pdf .txt .zip
# no suffix at all: output application/octet-stream

file = input("Input file here: ").lower().strip()

if file.endswith(".gif"):
    print("image/gif")

elif file.endswith(".jpg"):
    print("image/jpeg")

elif file.endswith(".jpeg"):
    print("image/jpeg")

elif file.endswith(".png"):
    print("image/png")

elif file.endswith(".pdf"):
    print("application/pdf")

elif file.endswith(".txt"):
    print("text/plain")

elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
