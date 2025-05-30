try:
    file1 = open('E:\Python\sample.txt','r')
    read_file = file1.read()
    print(read_file)
    file1.close()
except:
    print("Error: The file sample.txt was not found")
