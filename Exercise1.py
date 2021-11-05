N=int(input("Please enter a number:"))
sum_odd = 0
sum_even = 0
even_number_count = 0
for i in range(1,(N+1)):
    if i%2==0:
        sum_even=sum_even+i
        even_number_count = even_number_count +1
    else:
        sum_odd = sum_odd+i
average_even = sum_even/even_number_count
print("Sum of odd numbers is:" , sum_odd , "\nAverage of even numbers is:", average_even)