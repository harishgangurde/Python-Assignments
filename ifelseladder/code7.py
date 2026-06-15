
perc = int(input("Enter percentage: "))
score = int(input("Enter score: "))

if perc >= 90 and score >= 90:
    print("Admssion in Elite program")
    
elif 80 <= perc <= 90 and 70 <= score <= 90 :
    print("Admission in Standard program")
    
elif 60 <= perc  and 50 <= score :
    print("Admission in Basic program")
else:
    print("Not eligible")
