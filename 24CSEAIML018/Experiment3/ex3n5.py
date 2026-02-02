sub1=float(input("Enter marks for subject1: "))
sub2=float(input("Enter marks for subject2: "))
sub3=float(input("Enter marks for subject3: "))
sub4=float(input("Enter marks for subject4: "))
sub5=float(input("Enter marks for subject5: "))
total=sub1+sub2+sub3+sub4+sub5
per=(total / 250)*100
if(per>=90 and per<=100):
    print("Grade 'O'")
elif(per>=80 and per<90):
    print("Grade 'E'")
elif(per>=70 and per<80):
    print("Grade 'A'")
elif(per>=60 and per<70):
    print("Grade 'B'")
elif(per>=50 and per<60):
    print("Grade 'C'")
elif(per>=0 and per<50):
    print("Grade is'F'")
else:
    print("Wrong inputs")