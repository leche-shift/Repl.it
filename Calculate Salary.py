salaryCount = int(0)
salarySum = 0.0 
salaryAvg = 0.0
hoursWorked = 0.0
pay = 0.0
ovtPay = 0.0
regPay = 0.0
payrate = 0.0
payrate = float(input("\nEnter payrate {Negative number to stop}: "))
while payrate > 0:
  hoursWorked = float(input("\nEnter hours worked: "))
  if hoursWorked > 40:
    ovtPay = (hoursWorked - 40) * (payrate * 1.5)
    regPay = 40 * payrate
  else:
    ovtPay = 0.0
    regPay = hoursWorked * payrate
  pay = regPay + ovtPay
  salarySum += pay
  salaryCount += 1 
  print("\nThe salary of this week week = $",round(pay,2))
  payrate = float(input("/nEnter payrate {Negative number to stop} :"))
if salaryCount > 0:
  salaryAvg = salarySum / salaryCount
  print("\nThe average salary for this week was $",round(salaryAvg,2))
print("\nEnd of Program!\n")