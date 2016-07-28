
import datetime

def main():
   yearnow = datetime.datetime.now().year
   put=input("Enter Your Birthday Year : ")
   age = yearnow-int(put)
   print("Your Age is : {} Years Old".format(age))
   print("")
   print("Thanks For Using My App! ^_^")



if __name__ == '__main__':main()