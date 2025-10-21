import random

secret_number = random.randint(1, 100)

print("Познай числото, което съм избрал (между 1 и 100).")

attempts = 0  # Брой опити

while True:
    guess = int(input("Твоето предположение: "))
    attempts += 1

    if guess < secret_number:
        print("Моето число е по-голямо.")
    elif guess > secret_number:
        print("Моето число е по-малко.")
    else:
        print("Браво! Позна числото {secret_number} за {attempts} опита.")
        break
