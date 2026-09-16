# Creating a file name "sample.txt" with "w" (write mode parameter). 
# And assigning it to "file", which will return a file object.

file = open("sample.txt", "w")

# Writing text-lines to a file.
file.write("Hello World!\n")
file.write("This is the new text file.")