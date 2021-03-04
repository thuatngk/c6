def main():
    file_test =open('write.txt', 'r')
    line= file_test.readline()
    count =0
    sum=0
    while line != '':
        count =count +1
        sum += int(line)
        line=file_test.readline()

    aver =sum/count
    file_test.close()
    print(aver)
main()