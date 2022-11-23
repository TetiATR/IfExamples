try:
    Money = int(input("How Much Do You Make Mr?"))
    Kid = int(input("How Many Kids Do You Have Mr?"))
except ValueError:
    print("Don't Be Schewpid")
gross = Money
if Money < 1000:
    Money = Money - Money * 0.10
elif Money < 2000:
    Money = Money - Money * 0.12
elif Money < 4000:
    Money = Money - Money * 0.14
else:
    Money = Money - Money * 0.18

if gross < 2000:
    Net = Money + gross * Kid * 0.01
if gross > 2000:
    Net = Money + gross * Kid * 0.005
print("You Make ", gross,"$ Per Month With No Tax", sep="")
print("You Make ", Net, "$ Per Month", sep="")