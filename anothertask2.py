from datetime import datetime

print(f'The Moscow Times — {datetime.strptime('Wednesday, October 2, 2002', "%A, %B %d, %Y")}')
print(f'The Guardian — {datetime.strptime('Friday, 11.10.13', "%A, %d.%m.%y")}')
print(f'Daily News — {datetime.strptime('Thursday, 18 August 1977', "%A, %d %B %Y")}')
