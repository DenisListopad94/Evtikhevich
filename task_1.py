import math
# 1
print(17 / 2 * 3 + 2)

print(2 + 17 / 2 * 3)

print(19 % 4 + 15 / 2 * 3)

print(15 + 6 - 10 * 4)

print(17 / 2 % 2 * 3 ** 3)

# 2
print(17 / 2 * (3 + 2))

print((2 + 17) / 2 * 3)

print(19 % (4 + 15) / 2 * 3)

print((15 + 6 - 10) * 4)

print(17 / 2 % (2 * 3 ** 3))

# 3
print(11 - 3 * 1.5)

# 4
ann_apple = 2
pol_apple = 2

print('Ann has', ann_apple, 'apples. ' "Pol has", pol_apple, 'apples.')

# 5
days = 5
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('days =', days)
print(days, 'days =', hours, 'hours =', minutes, 'minutes =', seconds, 'seconds')

# 6
days = 182
full_weeks = days // 7
print(full_weeks, "full weeks passed in", days, 'days')

# 7
side_1 = 150
side_2 = 65

squares_number = side_1 // 30 * side_2 // 30

print(squares_number)

# 8
seconds = 4000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
left_seconds = (seconds % 3600) % 60

print('', hours, 'hours', '\n', minutes, 'minutes', '\n', left_seconds, 'seconds')

# 9
cash = 589
hundred = cash // 100
fifty_dollar = (cash % 100) // 50
ten_dollar = ((cash % 100) % 50) // 10
one_dollar = ((cash % 100) % 50) % 10
print(hundred, '$100 bills')
print(fifty_dollar, '$50 bills')
print(ten_dollar, '$10 bills')
print(one_dollar, '$1 bills')

# 10
h = 10
x = 5
y = 3
days = math.ceil((h - x) / (x - y)) + 1
print('On day', days, 'the snail will crawl to the top of', h, 'meters long pole')

# 11
road_length = 56
biker_velocity = 90
time_hours = 1
time_minutes = 30

stop_point = (biker_velocity * (time_hours + time_minutes / 60)) % road_length
print('Biker will stop at the', stop_point, 'kilometer point in', time_hours, 'hours', time_minutes, 'minutes')

