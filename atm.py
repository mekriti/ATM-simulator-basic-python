def deposit(amount,dep ):
 print "Total balance of Rs ",amount, "available before depositing.";
 amount=(amount+dep);
 print " Total balance of Rs " ,amount, "available after depositing ",dep,".";
am= int(raw_input("enter amount"));
def withdraw(amount,wid):
 print "Total balance of Rs ",amount, "available before withdrawal.";
 amount=(amount-wid);
 print " Total balance of Rs " ,amount, "available after withdrawing ",dep,".";
 
 
dp=int(raw_input("enter amount to be deposited"));
deposit(am,dp);


wid=int(raw_input("enter amount to be withdrawn"));
withdraw(am,wid);

