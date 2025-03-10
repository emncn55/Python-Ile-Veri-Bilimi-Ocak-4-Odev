numbers = []

for i in range(5):
    num = int(input(f"Lütfen {i+1}. sayıyı giriniz: "))
    numbers.append(num)

min_num = min(numbers)
max_num = max(numbers)

print(f"En Büyük Sayı: {max_num}")
print(f"En Küçük Sayı: {min_num}")
