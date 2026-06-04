# Write your solution here
gift = int(input("Value of gift: "))
if gift >= 1_000_000:
  print(f"Amount of tax: {(142_100 + (gift - 1_000_000) * 0.17)}")
elif gift >= 200_000 and gift < 1_000_000:
  print(f"Amount of tax: {(22_100 + (gift - 200_000) * 0.15)}")
elif gift >= 55000 and gift < 200_000:
  print(f"Amount of tax: {(4700 + (gift - 55000) * 0.12)}")
elif gift >= 25000 and gift < 55000:
  print(f"Amount of tax: {(1700 + (gift - 25000) * 0.10)}")
elif gift >= 5000 and gift < 25000:
  print(f"Amount of tax: {(100 + (gift - 5000) * 0.08)}")
else:
  print("No tax!")