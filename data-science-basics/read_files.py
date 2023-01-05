

# with -> cierra automaticamente el file al final
# abrir el archivo como "r" y usar funcion read(). 
# La función readlines() lo imprime como si fuera una lista. 
# La función readline() imprime una sola línea
# La función readlines(x) imprime los primeros x caraqcteres del archivo para cada linea

import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

## Download Example file
# !wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt

with open(filename, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)



# Read first four characters
with open(filename, "r") as file1:
    print(file1.read(4))


# Read certain amount of characters
with open(filename, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))


# Read one line
with open(filename, "r") as file1:
    print("first line: " + file1.readline())

with open(filename, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# Iterate through the lines
with open(filename,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list
with open(filename, "r") as file1:
    FileasList = file1.readlines()