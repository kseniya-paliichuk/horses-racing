import time
import os
from blessed import Terminal
from pick import pick

DEFAULT_DIFFICULTY = "Лёгкий"
DEFAULT_DURATION = "1 минута"
game_difficulty = DEFAULT_DIFFICULTY
game_duration = DEFAULT_DURATION

term = Terminal()

def pause(message="Нажмите Enter для продолжения..."):
    with term.cbreak():
        term.inkey()

def StartGame():
    #не реализовано
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Игра начинается!!!(скоро появится, ожидайте обновлений)")
    pause()
    return

def LoadGame():
    # не реализовано
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Данная функция на данный момент недоступна и появится в ближайших обновлениях;)")
    pause()
    return

def Settings():
    global game_difficulty, game_duration
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title = "НАСТРОЙКИ ИГРЫ\nИспользуйте стрелочки [↑/↓] для выбора и Enter для подтверждения\n"
        options = [
            f"Сложность (Сейчас: {game_difficulty})",
            f"Продолжительность (Сейчас: {game_duration})",
            "Сбросить настройки",
            "← Назад в главное меню"
        ]
        option, index = pick(options, title, backend="blessed", indicator="=>")
        
        match index:
            case 0:  #выбор сложности
                sub_title = "Выберите уровень сложности:"
                sub_options = ["Легкий", "Хард"]
                diff, _ = pick(sub_options, sub_title, backend="blessed", indicator="=>")
                game_difficulty = diff
                
            case 1:  #выбор продолжительности
                sub_title = "Выберите время матча:"
                sub_options = ["30 секунд", "1 минута", "3 минуты"]
                dur, _ = pick(sub_options, sub_title, backend="blessed", indicator="=>")
                game_duration = dur
                
            case 2:  #сброс настроек
                game_difficulty = DEFAULT_DIFFICULTY
                game_duration = DEFAULT_DURATION
                print("\n[!] Настройки сброшены!")
                pause()
                
            case 3: 
                return


def GameInf():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Версия игры: 1.0\nРазрабона: Палийчук Ксения")
    pause()
    return

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