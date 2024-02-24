import sys

message = ""
result = ""

for line in sys.stdin:
    line = line.strip()

    if line == "End":
        break

    if line.isalpha():
        message += line
        if "c" in message and "o" in message and "n" in message:
            if result:
                result += " "
            word = message.replace("c", "", 1).replace("o", "", 1).replace("n", "", 1)
            result += word
            message = ""

print(result)
