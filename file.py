def main():
     # name=input("input your full name: ")
     # file_write=open("write.txt",'w')
     #
     # file_write.write(name)

     # file test a file reference variable
     file_test = open("write.txt", 'r')   #read only
     line = file_test.readline()     #read line
     while line != '':
          print(line, end='')
          line=file_test.readline()
     print(line)    #in data
     file_test.close()



main()