import random


def get_user_move(remaining_stones):
    while True:
        try:
            user_move = int(
                input(f"Введите количество камней для взятия (1, 2 или 3). Осталось {remaining_stones} камней: "))
            if user_move not in [1, 2, 3]:
                raise ValueError("Вы можете взять только 1, 2 или 3 камня.")
            if user_move > remaining_stones:
                raise ValueError("Недостаточно камней для взятия.")
            return user_move
        except ValueError as e:
            print(e)


def computer_move_light_intelligence(remaining_stones):
    move = random.choice([1, 2, 3])
    while move > remaining_stones:
        move = random.choice([1, 2, 3])
    return move


def computer_move_medium_intelligence(remaining_stones):
    intelligence = random.randint(0, 1)
    if intelligence == 0:
        return computer_move_light_intelligence(remaining_stones)
    else:
        for move in range(1, 4):
            if (remaining_stones - move) % 4 == 0 and (remaining_stones - move) >= 0:
                return move
        return min(remaining_stones, 3)


def computer_move_high_intelligence(remaining_stones):
    for move in range(1, 4):
        if (remaining_stones - move) % 4 == 0:
            return move
    return min(remaining_stones, 3)


def play_game(difficulty):
    remaining_stones = random.randint(4, 30)
    print(f"Начальное количество камней: {remaining_stones}")
    while remaining_stones > 0:
        user_move = get_user_move(remaining_stones)
        remaining_stones -= user_move
        print(f"      Вы взяли {user_move} камня(ей) ==> осталось {remaining_stones} камней.")
        if remaining_stones == 0:
            print("Поздравляем! Вы выиграли в этой игре!")
            return
        if difficulty == "лёгкий":
            comp_move = computer_move_light_intelligence(remaining_stones)
        elif difficulty == "средний":
            comp_move = computer_move_medium_intelligence(remaining_stones)
        elif difficulty == "сложный":
            comp_move = computer_move_high_intelligence(remaining_stones)
        remaining_stones -= comp_move
        if remaining_stones < 0:
            remaining_stones = 0
        print(f"Компьютер взял {comp_move} камня(ей) ==> осталось {remaining_stones} камней.")
        if remaining_stones == 0:
            print("Компьютер выиграл! Попробуйте ещё раз сыграть.")


while True:
    difficulty = input("Выберите уровень сложности (лёгкий, средний или сложный): ")
    while difficulty not in ["лёгкий", "средний", "сложный"]:
        difficulty = input("Неверный ввод. Пожалуйста, выберите уровень сложности (лёгкий, средний или сложный): ")
    play_game(difficulty)
    play_again = input("Хотите сыграть еще раз? (да / нет): ")
    while play_again not in ["да", "нет"]:
        play_again = input("Неверный ввод. Пожалуйста, скажите хотите ли сыграть еще раз? (да / нет): ")
    if play_again == 'нет':
        print("Спасибо за игру! До свидания!")
        break
