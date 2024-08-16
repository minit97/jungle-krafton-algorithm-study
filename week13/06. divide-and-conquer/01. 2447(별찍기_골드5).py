# 한줄씩 생각해보자!

def draw_stars(n):
    if n == 1:
        return ['*']

    points = draw_stars(n//3)
    result = []

    for star in points:
        result.append(star * 3)
    for star in points:
        result.append(star + ' ' * (n // 3) + star)
    for star in points:
        result.append(star * 3)

    return result

n = int(input())
print('\n'.join(draw_stars(n)))


