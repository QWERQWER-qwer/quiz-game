# main.py
# 터미널 퀴즈 게임 (주제: 게임) - 코디세이 Python 미션
import json
import os

STATE_FILE = "state.json"

def read_int_in_range(prompt, low, high):
    """low~high 범위의 정수를 받을 때까지 반복 입력받는다.
    공백 제거 / 빈 입력 / 숫자 아님 / 범위 밖 -> 안내 후 재입력."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("[!] 입력이 비어 있습니다. 숫자를 입력하세요.\n")
            continue
        if not raw.isdigit():
            print("[!] 숫자만 입력할 수 있습니다.\n")
            continue
        number = int(raw)
        if number < low or number > high:
            print(f"[!] {low}~{high} 사이의 숫자를 입력하세요.\n")
            continue
        return number

def print_menu():
    print("=" * 40)
    print("           나만의 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

class QuizGame:
    """게임 전체(퀴즈 목록·최고 점수·메뉴 흐름·저장)를 관리한다."""

    def __init__(self):
        self.quizzes = []
        self.best_score = 0

    def run(self):
        while True:
            print_menu()
            choice = read_int_in_range("선택: ", 1, 5)
            if choice == 1:
                print("\n[퀴즈 풀기] 기능은 준비 중입니다.\n")
            elif choice == 2:
                print("\n[퀴즈 추가] 기능은 준비 중입니다.\n")
            elif choice == 3:
                print("\n[퀴즈 목록] 기능은 준비 중입니다.\n")
            elif choice == 4:
                print("\n[점수 확인] 기능은 준비 중입니다.\n")
            elif choice == 5:
                print("\n게임을 종료합니다. 안녕히 가세요!")
                break

if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n[!] 입력이 중단되었습니다. 안전하게 종료합니다.")

