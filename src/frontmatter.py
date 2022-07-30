file = open("file.md","r")

text = file.read()

file = open("file.md","w")

first = "---\n"
line1 = "Text afegit a posteriori\n"
end = "---\n\n"

file.write(first)
file.write(line1)
file.write(end)

file.write(text)

file.close()