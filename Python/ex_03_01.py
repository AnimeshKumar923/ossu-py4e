hrs = input("Enter Hours:")
rate = input("Enter rate:")
fh = float(hrs)
fr = float(rate)
if fh > 40 :
    # print ("Overtime")
    reg = fr * fh
    otp = (fh-40.0) * (fr * 0.5)
    # print(reg,otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr

print("Pay:", xp)