from sys import argv

script, filename = argv

print(f"Here are the contents of {filename}:\n")

file = open(filename)
txt = file.read()

print(txt)

file.close()
