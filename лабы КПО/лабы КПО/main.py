import time
import os
from blessed import Terminal
from pick import pick
from config import (init_files, load_settings, save_current,
                    load_defaults, load_difficulties,
                    DEFAULT_DIFFICULTY, DEFAULT_DURATION)

term = Terminal()

init_files()
game_difficulty, game_duration = load_settings()
available_difficulties = load_difficulties()


def pause(message="Нажмите Enter для продолжения..."):
    with term.cbreak():
        term.inkey()


def duration_to_str(days):
    return f"{days} дней"

def str_to_duration(s):
    return int(s.split()[0])


def StartGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Игра начинается!!!(скоро появится, ожидайте обновлений)")
    pause()


def LoadGame():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Данная функция на данный момент недоступна и появится в ближайших обновлениях;)")
    pause()


def Settings():
    global game_difficulty, game_duration
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title = "НАСТРОЙКИ ИГРЫ\nИспользуйте стрелочки [↑/↓] для выбора и Enter для подтверждения\n"
        options = [
            f"Сложность (Сейчас: {game_difficulty})",
            f"Продолжительность (Сейчас: {duration_to_str(game_duration)})",
            "Сбросить настройки",
            "← Назад в главное меню"
        ]
        option, index = pick(options, title, backend="blessed", indicator="=>")

        match index:
            case 0:  #выбор сложности
                sub_title = "Выберите уровень сложности:"
                sub_options = sorted(available_difficulties) or ["Легкий", "Хард"]
                diff, _ = pick(sub_options, sub_title, backend="blessed", indicator="=>")
                game_difficulty = diff
                save_current(game_difficulty, game_duration)

            case 1:  #выбор продолжительности в днях
                sub_title = "Выберите длительность сезона:"
                sub_options = ["25 дней", "50 дней"]
                dur, _ = pick(sub_options, sub_title, backend="blessed", indicator="=>")
                game_duration = str_to_duration(dur)
                save_current(game_difficulty, game_duration)

            case 2:  #сброс настроек
                game_difficulty, game_duration = load_defaults()
                save_current(game_difficulty, game_duration)
                print("\n[!] Настройки сброшены!")
                pause()

            case 3:
                return


def GameInf():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Версия игры: 2.0\nРазрабона: Палийчук Ксения")
    pause()


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_title = "=== ГЛАВНОЕ МЕНЮ ИГРЫ ===\nУправляйте стрелочками:"
        main_options = ["🎮 Играть", "⬆️⬆ Загрузить игру", "⚙️ Настройки", "📄 Об игре", "❌ Выход"]

        option, index = pick(main_options, main_title, backend="blessed", indicator="=>")
        match index:
            case 0:
                StartGame()
            case 1:
                LoadGame()
            case 2:
                Settings()
            case 3:
                GameInf()
            case 4:
                print("До свидания!")
                time.sleep(2)
                break


if __name__ == "__main__":
    main()