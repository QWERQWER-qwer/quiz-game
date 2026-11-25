# main.py
# 터미널 퀴즈 게임 (주제: 게임) - 코디세이 Python 미션
import json
import os

STATE_FILE = "state.json"

DEFAULT_QUIZZES = [
    {"question": "해적왕을 꿈꾸며 고무 몸을 가진 루피가 주인공인 애니메이션은?",
     "choices": ["원피스", "나루토", "블리치", "페어리테일"], "answer": 1},
    {"question": "닌자 세계에서 호카게를 꿈꾸는 소년이 주인공인 애니메이션은?",
     "choices": ["블리치", "나루토", "원펀맨", "학원 묵시록"], "answer": 2},
    {"question": "거인과 싸우는 인류를 그린, 엘런이 주인공인 애니메이션은?",
     "choices": ["도쿄 구울", "진격의 거인", "강철의 연금술사", "데스노트"], "answer": 2},
    {"question": "남녀의 몸이 뒤바뀌는 신카이 마코토 감독의 극장판 애니메이션은?",
     "choices": ["너의 이름은.", "날씨의 아이", "목소리의 형태", "스즈메의 문단속"], "answer": 1},
    {"question": "탄지로가 여동생을 되돌리려 도깨비와 싸우는 애니메이션은?",
     "choices": ["주술회전", "귀멸의 칼날", "체인소맨", "도로헤도로"], "answer": 2},
    {"question": "소년이 '데스노트'로 범죄자를 심판하는 이야기의 애니메이션은?",
     "choices": ["코드 기어스", "데스노트", "사이코패스", "몬스터"], "answer": 2},
]

class Quiz:
    """개별 퀴즈 하나(문제·선택지·정답)를 표현한다."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_input):
        return user_input == self.answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])

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

    def load(self):
        self.quizzes = [Quiz.from_dict(d) for d in DEFAULT_QUIZZES]
        self.best_score = 0

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.\n")
            return
        print(f"\n퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)\n")
        correct = 0
        for idx, quiz in enumerate(self.quizzes, 1):
            print("-" * 40)
            print(f"[문제 {idx}]")
            quiz.show()
            answer = read_int_in_range("정답 입력(1-4): ", 1, 4)
            if quiz.is_correct(answer):
                print("[O] 정답입니다!\n")
                correct += 1
            else:
                print(f"[X] 오답입니다. 정답은 {quiz.answer}번.\n")
        total = len(self.quizzes)
        score = int(correct / total * 100)
        print("=" * 40)
        print(f"결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        print("=" * 40 + "\n")

    def run(self):
        while True:
            print_menu()
            choice = read_int_in_range("선택: ", 1, 5)
            if choice == 1:
                self.play()
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
    game.load()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n[!] 입력이 중단되었습니다. 안전하게 종료합니다.")

