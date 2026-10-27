def calculate_simple_interest(principal,rate,time):
    return (principal*rate*time)/180


if __name__== "__main__":
 principle = float(input("enter the principle amount:"))
 rate= float(input("enter the rate of interst:"))
 time = loat(input("enter the time in years:"))

 interest= calculate_simple_interest(principal,rate,time)
 print("Simple interest=", simple_interest)
