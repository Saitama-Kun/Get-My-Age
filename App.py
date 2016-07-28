
import datetime # It says all i think
def main():
   yearnow = datetime.datetime.now().year #Getting Actual Year Using the date time library declared in the top of code
   put=input("Enter Your Birthday Year : ") #The Input message 
   age = yearnow-int(put) #Converting The input Value to Integer
   print("Your Age is : {} Years Old".format(age))  
   print("") 
   print("Thanks For Using My App! ^_^")



if __name__ == '__main__':main()
