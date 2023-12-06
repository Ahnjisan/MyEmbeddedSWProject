#Event.py
import random
import time
from Character import Character
from Joystick import Joystick
from PIL import ImageFont, ImageDraw, Image


class Event:
    def __init__(self, character, joystick):
        self.character = character
        self.joystick = joystick
        self.event4_count = 0
        self.event5_count = 0
        self.event7_count = 0
        
    def display_text(self, text):
        image = Image.new("RGB", (240, 240), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((10, 10), text, font=font, fill=(255, 255, 255))
        self.joystick.disp.image(image)
        time.sleep(2)
            
    def event2(self):
        self.display_text("Would you like to have a meal? A : YES, B : NO")
        # 사용자 응답 받기
        user_answer = self.get_user_answer()

        # "예"를 선택한 경우
        if user_answer:
            self.character.recover_health(10)
            self.display_text("My health has recovered by 10")
            time.sleep(1)  # 1초 동안 대기

        else:
            self.display_text("You didn't eat.")
            time.sleep(1)  # 1초 동안 대기
        # 이벤트 2에 대한 처리 로직
    
    def event3(self, joystick):
        self.character.health -= 10
        quiz_data = [
            {"question" : "1 + 1 = ?", "options" : ["cutie", "2", "3", "4"], "answer": "2"},
            {"question" : "What is the biggest planet in the solar system?", "options" : ["Earth", "Jupiter", "Mars", "Venus"], "answer": "Jupiter"},
            {"question" : "What is the name of the professor in this lecture?", "options" : ["Choi Cha-bong", "Choi Bul-Am", "Choi Dong-won", "The best"], "answer": "Choi Cha-bong"},
            {"question" : "Which team won the KBO League in the 2023 season?", "options" : ["LG Twins", "Kiwom Heroes", "SSG Landers", "KT Wiz"], "answer": "LG Twins"},
            {"question" : "What is the name of the station that will change?", "options" : ["Hwajeong Station", "Hoejeon Station", "Hoejeong Station", "Korea Aerospace University Station"], "answer": "Korea Aerospace University Station"},
            {"question" : "What is the name of the person who made this game?", "options" : ["Ahn ji-san", "Ahn tae-san", "Ahn san", "Ahn jiri-san"], "answer": "Ahn ji-san"}
        ]
        selected_quiz = random.choice(quiz_data)
        options = selected_quiz["options"]
        selected_index = 0
        
        while True:
            self.display_quiz(joystick, selected_quiz["question"], options, selected_index)
            if not joystick.button_U.value:
                selected_index = max(0, selected_index - 1)
            elif not joystick.button_D.value:
                selected_index = min(len(options) - 1, selected_index + 1)
            elif not joystick.button_A.value:
                break
            time.sleep(0.2)
            
        if options[selected_index] == selected_quiz["answer"]:
            self.character.increase_study(1)
            self.display_text("That's correct! Your study has increased.")
        else:
            self.display_text("Incorrect.")
        # 이벤트 3에 대한 처리 로직
    
    def event4(self):
        if self.event4_count < 2:  # event4가 2회 미만으로 실행되었는지 확인
            self.display_text("Would you like to take a special lecture?")
            self.display_text("A : YES, B : NO ")
            user_answer = self.get_user_answer()

            if user_answer:
                self.character.increase_study(5)
                self.character.health -= 20
                self.display_text("Your Study has increased significantly.")
                time.sleep(1)  # 2초 동안 대기
            else:
                self.character.health -= 20
                self.display_text("You didn't take a special lecture.")
                time.sleep(1)  # 2초 동안 대기

            self.event4_count += 1  # event4 실행 횟수 증가
        else:
            self.display_text("You can't take any more special lectures.")
            time.sleep(1)  # 2초 동안 대기
        # 이벤트 4에 대한 처리 로직
    
    def event5(self):
        if self.event5_count < 7:  # event5가 5회 미만으로 실행되었는지 확인
            self.display_text("Would you like to attend?")
            self.display_text("A : YES, B : NO ")
            user_answer = self.get_user_answer()

            if user_answer:
                self.character.increase_study(1)
                self.character.health -= 10
                self.display_text("Your study has increased.")
                time.sleep(1)  # 2초 동안 대기
            else:
                self.display_text("You didn't take the class.")
                time.sleep(1)  # 2초 동안 대기

            self.event5_count += 1  # event5 실행 횟수 증가
        else:
            self.display_text("You can't take any more class.")
            time.sleep(1)  # 2초 동안 대기
        # 이벤트 5에 대한 처리 로직
    
    def event6(self):
        self.display_text("Do you want to conduct the midterm exam?")
        self.display_text("A : YES, B : NO ")
        user_answer = self.get_user_answer()
        if user_answer:
            if self.character.study >= 10 and self.character.tasks >= 1:
                self.display_text("You took my midterm exam. Fighting until the end of the semester!!")
                time.sleep(1)  # 1초 동안 대기
            else:
                self.display_text("You need to study more.")
                time.sleep(1)  # 1초 동안 대기
        else:
            self.display_text("You need to study more.")
            time.sleep(1)  # 1초 동안 대기
        # 이벤트 6에 대한 처리 로직
    
    def event7(self):
        if self.event7_count == 0:
            self.display_text("Do you want to submit Task 1?  A : YES")
            user_answer = self.get_user_answer()
            if user_answer:
                if self.character.study >= 5:
                    self.display_text("Task 1 has been submitted.")
                    self.character.health -= 20
                    self.character.complete_tasks()
                    self.event7_count += 1
                    time.sleep(1)  # 1초 동안 대기
                else:
                    self.display_text("Unable to submit Task.")
                    time.sleep(1)  # 1초 동안 대기
        elif self.event7_count == 1:
            self.display_text("Do you want to submit Task 2?  A : YES")
            user_answer = self.get_user_answer()
            if user_answer:
                if self.character.study >= 10:
                    self.display_text("Task 2 has been submitted.")
                    self.character.health -= 20
                    self.character.complete_tasks()
                    self.event7_count += 1
                    time.sleep(1)  # 1초 동안 대기
            else:
                self.display_text("Unable to submit Task.")
                time.sleep(1)  # 1초 동안 대기
        elif self.event7_count == 2:
            self.display_text("Do you want to submit Task 3?  A : YES")
            user_answer = self.get_user_answer()
            if user_answer:
                if self.character.study >= 15:
                    self.display_text("Task 3 has been submitted.")
                    self.character.health -= 20
                    self.character.complete_tasks()
                    self.event7_count += 1
                    time.sleep(1)  # 1초 동안 대기
                else:
                    self.display_text("Unable to submit Task.")
                    time.sleep(1)  # 1초 동안 대기
            
        # 이벤트 7에 대한 처리 로직
        
    def event8(self):
        self.display_text("Do you want to conduct the final exam?")
        self.display_text("A : YES, B : NO ")
        user_answer = self.get_user_answer()
        if user_answer:
            if self.character.study >= 20 and self.character.tasks >= 3:
                self.display_text("You took the final exam. NICE!!")
                time.sleep(1)  # 1초 동안 대기
                return True  # 게임 종료 신호 반환
            else:
                self.display_text("You need to study more.")
                time.sleep(1)  # 1초 동안 대기
                return False
            # 이벤트 8에 대한 처리 로직
        else:
            self.display_text("You need to study more.")
            time.sleep(1)  # 1초 동안 대기
                  
    def get_user_answer(self):
        # 조이스틱 입력을 기다림
        while True:
            if not self.joystick.button_A.value:  # A 버튼을 누르면 "예"로 간주
                return True
            elif not self.joystick.button_B.value:  # B 버튼을 누르면 "아니오"로 간주
                return False
        
            
    def display_quiz(self, joystick, question, options, selected_index):
        image = Image.new("RGB", (240, 240), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # 퀴즈 질문 표시
        draw.text((10, 10), question, font=font, fill=(255, 255, 255))

        # 퀴즈 선택지 및 선택 표시
        y_pos = 40
        for i, option in enumerate(options):
            if i == selected_index:
                draw.ellipse((5, y_pos - 5, 25, y_pos + 15), outline=(255, 255, 255), fill=(255, 255, 255))
            draw.text((30, y_pos), f"{i+1}. {option}", font=font, fill=(255, 255, 255))
            y_pos += 30

        joystick.disp.image(image)