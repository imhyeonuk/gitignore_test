import random
import time

def generate_random_number():
    return random.randint(1, 100)

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def play_game():
    score = 0  # 점수 초기화
    start_time = time.time()  # 게임 시작 시간 기록
    game_duration = 30  # 게임 제한 시간 (30초)
    
    # 제한 시간 동안 게임 진행
    while time.time() - start_time < game_duration:
        number = generate_random_number()  # 랜덤 숫자 생성
        print(f"숫자: {number}")  # 숫자 출력
        
        # 사용자 입력 받기
        user_input = input("짝수인지 홀수인지 맞추세요 (even/odd): ").strip().lower()
        
        # 정답 체크
        correct_answer = check_even_odd(number)  # 정답 판별
        if user_input == correct_answer:
            score += 1  # 정답이면 점수 증가
            print("정답입니다!")
        else:
            print(f"오답입니다. 정답은 {correct_answer}입니다.")
            break  # 오답이면 게임 종료
    
    # 게임 종료 후 최종 점수 출력
    print(f"게임 종료! 최종 점수: {score}")

if __name__ == "__main__":
    play_game()