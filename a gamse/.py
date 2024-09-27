import random

# 5-ბგერიანი სიტყვების სია
words = ['apple', 'grape', 'peach', 'melon', 'lemon', 'mango', 'berry', 'cherry', 'plumb', 'olive']

def wordle():
    # შემთხვევითი სიტყვა სიისგან
    secret_word = random.choice(words)
    attempts = 6  # მომხმარებელს აქვს 6 მცდელობა

    print("გამარჯობა! ითამაშეთ Wordle. გამოიცანით 5-ბგერიანი სიტყვა.")

    while attempts > 0:
        guess = input(f"\nთქვენი მცდელობა ({attempts} დარჩა): ").lower()

        # ვამოწმებთ, რომ შეყვანილი სიტყვა არის 5-ბგერიანი
        if len(guess) != 5:
            print("გთხოვთ შეიყვანოთ ზუსტად 5-ბგერიანი სიტყვა.")
            continue

        if guess == secret_word:
            print(f"გილოცავთ! თქვენ სწორად გამოიცანით სიტყვა '{secret_word}'!")
            break

        # შევქმნით რეცენზიას სიტყვაზე
        feedback = []
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback.append(guess[i].upper())  # სწორად მიხვდა ბგერას და პოზიციას
            elif guess[i] in secret_word:
                feedback.append(guess[i].lower())  # ბგერა სწორია, მაგრამ არასწორ პოზიციაზეა
            else:
                feedback.append("_")  # ბგერა საერთოდ არ არის სიტყვაში

        print(" ".join(feedback))  # ვაჩვენებთ გამოხმაურებას

        attempts -= 1

    if attempts == 0:
        print(f"\nსამწუხაროდ, თქვენ ვერ გამოიცანით სიტყვა. სწორი პასუხი იყო '{secret_word}'.")

# მთავარი პროგრამის გაშვება
wordle()
