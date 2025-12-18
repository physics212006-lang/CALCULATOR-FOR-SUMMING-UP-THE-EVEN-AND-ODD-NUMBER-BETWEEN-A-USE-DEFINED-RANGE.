#taking input of the range from user
print("range is defined by [a,b]")
start=int(input("Enter  the value of a : "))
end=int(input("Enter the value of b : "))
#intialize the value of total =0
total=0
for l in range(start,end+1,1):
# if the value of l is an odd number then only l is added with the total variable.
 if l%2!=0:
#after every cycle of the loop the value of l is added with total .
    total+=l
print(f"SUM  OF THE ALL ODD NUMBER BETWEEN {start} and {end} is:={total}")






