# fv=amount*(1+rate)^period
amount = float(input('จำนวนเงินที่ลงทุน:'))
rate = float(input('อัตราค่าดอกเบี้ย :'))
period = float (input('ช่วงเวลา:'))
total1 = pow((1+rate),period)
print('`test',format(total1,','))
total2 = total1*amount
print('เงินที่ได้ :',format(total2,','))

