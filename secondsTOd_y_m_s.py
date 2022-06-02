# Перевод секунд в формат "д:ч:м:с"

seconds = int(input('Введите секунды: '))
days = seconds // (60 * 60 * 24)
hours = (seconds - days * (60 * 60 * 24)) // (60 * 60)
minutes = (seconds - days * (60 * 60 * 24) - hours * (60 * 60))

res_seconds = seconds - days
print('Результат: ' +str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))