# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20612 박한별
# 프로젝트 주제: 사용자의 선호 부위와 제한 시간에 맞춘 운동 루틴 추천기

# ============================================================
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================
import random

exercise_db = [
    ["스쿼트", 10, 120, "하체", "초급"],
    ["런지", 8, 90, "하체", "중급"],      
    ["레그프레스", 15, 140, "하체", "상급"],
    ["푸쉬업", 5, 50, "상체", "초급"],
    ["턱걸이", 7, 80, "상체", "상급"],
    ["바벨로우", 12, 100, "상체", "중급"],  
    ["플랭크", 4, 30, "코어", "초급"],
    ["크런치", 6, 45, "코어", "중급"],       
    ["버피테스트", 12, 180, "전신", "상급"]
]

def get_user_input():
    print("=== ✨ 나만의 맞춤 운동 루틴 매니저 ✨ ===")
    
    while True:
        part = input("원하는 운동 부위를 입력하세요 (상체/하체/코어/전신): ")
        if part in ["상체", "하체", "코어", "전신"]:
            break
        print("❌ 잘못된 부위입니다. '상체', '하체', '코어', '전신' 중에서만 입력해 주세요!")
        
    # [보완] 허용 단어 목록에 '중급'을 쏙 추가했습니다!
    while True:
        level = input("원하는 운동 난이도를 입력하세요 (초급/중급/상급): ")
        if level in ["초급", "중급", "상급"]:
            break
        print("❌ 잘못된 난이도입니다. '초급', '중급', '상급'으로만 입력해 주세요!")
    
    while True:
        try:
            time = int(input("운동할 수 있는 최대 시간(분)을 입력하세요: "))
            if time <= 0:
                print("❌ 운동 시간은 0보다 커야 합니다. 다시 입력해주세요.")
                continue
            return part, level, time
        except ValueError:
            print("❌ 숫자로만 정확하게 입력해 주세요!")

def generate_easy_routine(max_time, preferred_part, preferred_level):
    filtered_exercises = [
        ex for ex in exercise_db 
        if ex[3] == preferred_part and ex[4] == preferred_level
    ]
    
    other_exercises = [
        ex for ex in exercise_db 
        if not (ex[3] == preferred_part and ex[4] == preferred_level)
    ]
    
    random.shuffle(filtered_exercises)
    random.shuffle(other_exercises)
    
    total_pool = filtered_exercises + other_exercises
    
    selected_routine = []
    current_time = 0
    
    for ex in total_pool:
        if current_time + ex[1] <= max_time:
            selected_routine.append(ex)
            current_time += ex[1]
            
    return selected_routine

def print_result(result, max_time, preferred_part, preferred_level):
    print("\n" + "="*40)
    print(f"🏃‍♂️ [{preferred_part} / {preferred_level}] 중심의 {max_time}분 맞춤 루틴")
    print("="*40)
    
    total_db_time = sum(ex[1] for ex in exercise_db)
    if max_time > total_db_time:
        print(f"💡 안내: 현재 준비된 모든 운동의 총 시간({total_db_time}분)이")
        print(f"         입력하신 시간({max_time}분)보다 적어 모든 운동을 담았습니다.")
        print("-" * 40)
    
    if not result:
        print("❌ 입력하신 시간 내에 조합할 수 있는 운동이 없습니다.")
        print("   조금 더 여유로운 운동 시간을 입력해 주세요!")
        print("="*40)
        return
        
    total_cal = 0
    
    for ex in result:
        print(f"- {ex[0]} ({ex[3]}/{ex[4]}) : {ex[1]}분 / {ex[2]}kcal")
        total_cal += ex[2]
        
    print("-" * 40)
    print(f"⏱ 실제 총 운동 시간: {sum(ex[1] for ex in result)}분")
    print(f"🔥 예상 총 소모 칼로리: {total_cal}kcal")
    print("="*40)

if __name__ == "__main__":
    user_part, user_level, user_time = get_user_input()
    routine_result = generate_easy_routine(user_time, user_part, user_level)
    print_result(routine_result, user_time, user_part, user_level)