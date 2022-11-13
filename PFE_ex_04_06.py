def computepay(hrs, rate):
    if hrs > 40:
        othr = int(hrs) - 40
        reghours = hrs - othr
        pay = float(reghours) * f_rate
        otrate = float(rate) * 1.5
        otpay = float(othr) * float(otrate)
        return pay + otpay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
f_hrs = float(hrs)
f_rate = float(rate)
p = computepay(f_hrs, f_rate)
print("Pay", p)