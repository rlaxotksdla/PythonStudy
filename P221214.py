import sys

# 들여쓰기 개념을 잘몰라서 엄청 헤맸음 자바처럼 For문을 사용하려 했으나 사용처가 다른거같아서 while로 대체함
def calc(inputData, arrayData,arraylengthData):
    sum = 0
    n = 0
    i = 0

    arrayData=[x.upper() for x in arrayData]
    
    if arrayData[0]=='0':
       if arrayData[1]=='X':
        n=16
        i=2
       else:
        n=8
        i=1
                 
    while i <arraylengthData:
        
        if   arrayData[i]=='1':
            sum=sum +n**(arraylengthData-i-1)*1
        elif arrayData[i]=='2':
            sum=sum +n**(arraylengthData-i-1)*2
        elif arrayData[i]=='3':
            sum=sum +n**(arraylengthData-i-1)*3
        elif arrayData[i]=='4':
            sum=sum +n**(arraylengthData-i-1)*4
        elif arrayData[i]=='5':
            sum=sum +n**(arraylengthData-i-1)*5
        elif arrayData[i]=='6':
            sum=sum +n**(arraylengthData-i-1)*6
        elif arrayData[i]=='7':
            sum=sum +n**(arraylengthData-i-1)*7
        elif arrayData[i]=='8':
            sum=sum +n**(arraylengthData-i-1)*8
        elif arrayData[i]=='9':
            sum=sum +n**(arraylengthData-i-1)*9
        elif arrayData[i]=='0':
            sum=sum +n**(arraylengthData-i-1)*0
        elif arrayData[i]=='A':
            sum=sum +n**(arraylengthData-i-1)*10
        elif arrayData[i]=='B':
            sum=sum +n**(arraylengthData-i-1)*11
        elif arrayData[i]=='C':
            sum=sum +n**(arraylengthData-i-1)*12
        elif arrayData[i]=='D':
            sum=sum +n**(arraylengthData-i-1)*13
        elif arrayData[i]=='E':
            sum=sum +n**(arraylengthData-i-1)*14
        elif arrayData[i]=='F':
            sum=sum +n**(arraylengthData-i-1)*15
        i=i+1
    if   n==16:
        print("[It's a Hexadecimal Number] - Convert ot Decimal Result : ",sum)

    elif n==8: 
        print("[It's a Octal Number] - Convert ot Decimal Result : ",sum)
                
    else :
        print("[It's a Decimal Number] - No need to Convert. Result : ",inputData)
                

inputString=sys.argv[1]
# print(len(sys.argv))
# print(inputString)
if len(sys.argv)==2:
   print("Data Recieved")  
   charArray=list(inputString)
   arraylength=len(charArray)
   print("Input Data : ",inputString)
   calc(inputString, charArray, arraylength)
else:
    print("Only one data can be entered")





