
# with -> cierra automaticamente el file al final
# abrir el archivo como "w" y usar funcion write(). 
# Cada vez que se llama a la función write se escribe una línea.

# Abrir un archivo con "w" colocará el cursor al inicio del archivo y empezará a escribir borrando todo lo que tiene.
# Abrir el archivo con "a" colocará el cursor al final y empezará a escribir a partir del final.

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# However, note that setting the mode to "w" overwrites all the existing data in the file.
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# We can write to files without losing any of the existing data as follows by setting the mode argument to append: "a".  you can append a new line as follows:
# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# Otros modos para usar en los archivos:
# r+ -> lee y escribe. No puede trucar (cortar por los extremos) el file 
# w+ -> Escribe y lee. Puede truncar
# a+ -> Abrir un archivo con "a" escribe/añade y lee el archivo

with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())


# El método tell() retorna la posición del cursor en bytes.
# El método truncate() se suele usar cuando se pone r+, reducirá el archivo borrando todo lo que sigue a partir de cuanod se ponga
# El método seek(offset, from) cambian la posición por offset bytes respecto el from. El inicio sería 0,1,2, seguido de la current posición y el final
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)