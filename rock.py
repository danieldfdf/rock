import random

def play_game():
    # 고를수 있는 옵션선택
    options = ["가위", "바위", "보"]

    # 승부를 알수있는 카운트를 내기위한 코드
    wins, losses, draws = 0, 0, 0

    while True:
        # 내가 입력할수있는것
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user_choice not in options:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue

        # 컴퓨터의 선택
        computer_choice = random.choice(options)
        print(f"당신의 선택: {user_choice}, 컴퓨터의 선택: {computer_choice}")

        # 결과 결정
        if user_choice == computer_choice:
            print("비겼습니다!")
            draws += 1
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            print("당신이 이겼습니다!")
            wins += 1
        else:
            print("컴퓨터가 이겼습니다!")
            losses += 1

        # 다시 할 것인지 묻기
        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != "y":
            print(f"\n최종 스코어: 승리 {wins}회, 패배 {losses}회, 무승부 {draws}회")
            break

if __name__ == "__main__":
    play_game()
