# Расчет прибыли от депозита

amount = float(input('Введите сумму: '))
years = int(input('Введите кол-во лет: '))
final_amount = amount * (1.1 ** years)
print('Сумма снятия вклада за '+ str(years) + ' год(лет) составит: ', round(final_amount, 2))
print('Прибыль за '+ str(years) + ' год(лет) составит: ', round(final_amount - amount, 2))