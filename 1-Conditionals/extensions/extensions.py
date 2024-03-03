#  prompts the user for the name of a file and then outputs that file’s media type
# .gif .jpg .jpeg .png .pdf .txt .zip
# no suffix at all: output application/octet-stream

file = input("Input file here: ").lower().strip()

match file:
    case ".gif":
        print("PLACEHOLDER")
    case ".jpg" | "jpeg":
        print("PLACEHOLDER")
    case ".png":
        print("PLACEHOLDER")
    case ".pdf":
        print("PLACEHOLDER")
    case ".txt":
        print("PLACEHOLDER")
    case ".zip":
        print("PLACEHOLDER")
    case _:
        print("application/octet-stream")
