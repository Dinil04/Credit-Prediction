Progress_Count=0
Trailer_Count=0
Retriver_Count=0
Exclude_Count=0
Progress=""
Trailer=""
Retriver=""
Exclude=""
def Data_Input():
 while True:
  try:
   global Pass_Credit
   Pass_Credit=input('Please Enter your credit at pass:')
   Pass_Credit=int(Pass_Credit)
   if Pass_Credit in(0,20,40,60,80,100,120):
     break
   else:
      print("Out of range")
      continue
  except ValueError:
    print("Integer required")

 while True:
  try:
   global Defer_Credit   
   Defer_Credit=input("Please Enter your credit at defer:")
   Defer_Credit=int(Defer_Credit)
   if Defer_Credit in(0,20,40,60,80,100,120):
     break
   else:
      print("Out of range")
      continue
  except ValueError:
    print("Integer required")
 
 while True:
  try:
   global Fail_Credit   
   Fail_Credit=input("Please Enter your credit at fail:")
   Fail_Credit=int(Fail_Credit)
   if Fail_Credit in(0,20,40,60,80,100,120):
     break
   else:
      print("Out of range")
      continue
  except ValueError:
    print("Integer required")
 global total
 total =Pass_Credit+Defer_Credit+Fail_Credit
 return total
 return Pass_Credit
 return Defer_Credit
 return Fail_Credit
 Find_Total()
   
def Find_Total(total):
 if total!=120:
      print("Total Incorrect")
      Data_Input()
 else:
      
      Find_Outcome(Pass_Credit,Defer_Credit,Fail_Credit)


def Find_Outcome(a,b,c):
    
    if Pass_Credit==120 and Defer_Credit==0 and Fail_Credit==0:
        print("Progress")
        global Progress_Count
        Progress_Count+=1
        global Progress
        Progress +='*'
        
    elif (Pass_Credit==100 and Defer_Credit==20 and Fail_Credit==0) or(Pass_Credit==100 and Defer_Credit==0 and Fail_Credit==20):
        print("Progress(Module Trailer)")
        global Trailer_Count
        Trailer_Count+=1
        global Trailer
        Trailer +='*'

    elif (Pass_Credit==80 and Defer_Credit==40 and Fail_Credit==0) or (Pass_Credit==80 and Defer_Credit==20 and Fail_Credit==20)or (Pass_Credit==80 and Defer_Credit==00 and Fail_Credit==40) or (Pass_Credit==60 and Defer_Credit==60 and Fail_Credit==0) or (Pass_Credit==60 and Defer_Credit==40 and Fail_Credit==20) or (Pass_Credit==60 and Defer_Credit==20 and Fail_Credit==40)or (Pass_Credit==60 and Defer_Credit==0 and Fail_Credit==60) or (Pass_Credit==40 and Defer_Credit==80 and Fail_Credit==0) or (Pass_Credit==40 and Defer_Credit==60 and Fail_Credit==20)or(Pass_Credit==40 and Defer_Credit==40 and Fail_Credit==40) or (Pass_Credit==40 and Defer_Credit==20 and Fail_Credit==60) or (Pass_Credit==20 and Defer_Credit==100 and Fail_Credit==0) or (Pass_Credit==20 and Defer_Credit==80 and Fail_Credit==20) or (Pass_Credit==20 and Defer_Credit==60 and Fail_Credit==40) or (Pass_Credit==20 and Defer_Credit==40 and Fail_Credit==60) or (Pass_Credit==0 and Defer_Credit==120 and Fail_Credit==0) or (Pass_Credit==0 and Defer_Credit==80 and Fail_Credit==40) or (Pass_Credit==0 and Defer_Credit==60 and Fail_Credit==60) or (Pass_Credit==0 and Defer_Credit==100 and Fail_Credit==20) :
        print("Do not Progress(Module Retriever)")
        global Retriver_Count
        Retriver_Count+=1
        global Retriver
        Retriver +='*'
    elif (Pass_Credit==40 and Defer_Credit==0 and Fail_Credit==80) or (Pass_Credit==20 and Defer_Credit==20 and Fail_Credit==80)or (Pass_Credit==20 and Defer_Credit==0 and Fail_Credit==100)or (Pass_Credit==0 and Defer_Credit==40 and Fail_Credit==80) or (Pass_Credit==0 and Defer_Credit==20 and Fail_Credit==100)or (Pass_Credit==0 and Defer_Credit==0 and Fail_Credit==120):
        print("Exclude)")
        global Exclude_Count
        Exclude_Count+=1
        global Exclude
        Exclude +='*'

    
    Select_Option()


def Select_Option():
    User_Input=input("Would you like to enter another set of data? \nEnter 'Y' for Yes or 'q' to quit and view result ")    
    while User_Input=="y":
        Data_Input()
        Find_Total(total)
        Find_Outcome(Pass_Credit,Defer_Credit,Fail_Credit)
        

    print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Horizonal Histogram ')
    print("   Progress ",Progress_Count,":",Progress, end="")
    print("\n Trailer  ",Trailer_Count, ":",Trailer,  end="")
    print("\n Retriver ",Retriver_Count,":",Retriver, end="") 
    print("\n Exclude  ",Exclude_Count, ":",Exclude,  end="")
    print('\n')
    print('\n')
    print((Progress_Count+Trailer_Count+Retriver_Count+Exclude_Count),'Outcomes in Total')
    print('\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
Data_Input()
Find_Total(total)

#dinil_20200516
    




