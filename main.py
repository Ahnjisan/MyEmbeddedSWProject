import time
from PIL import ImageFont, ImageDraw, Image
from Character import Character
from Event import Event
from Joystick import Joystick

def display_game_finish_screen(joystick):
        image = Image.new("RGB", (240, 240), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((10, 10), "Game Finish", font=font, fill=(255, 255, 255))
        joystick.disp.image(image)
        time.sleep(3)  # 3초 동안 게임 종료 화면 표시
        
def main():
    # 조이스틱 및 캐릭터 객체 초기화
    joystick = Joystick()
    character = Character()
    event = Event(character, joystick)
    selected_event_index = 0

    def display_game_screen(selected_event_index):
        image = Image.new("RGB", (240, 240), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        # 제목 그리기
        draw.text((10, 10), "Beautiful KAU Software Students Life", font=font, fill=(255, 255, 255))

        # 캐릭터 상태 그리기
        draw.text((10, 30), f"health: {character.health}", font=font, fill=(255, 255, 255))
        draw.text((10, 50), f"study: {character.study}", font=font, fill=(255, 255, 255))
        draw.text((10, 70), f"tasks: {character.tasks}", font=font, fill=(255, 255, 255))

        # 이벤트 메뉴 그리기
        events = ["1. Meal", "2. Study", "3. Special lecture", "4. lecture", "5. Midterm Exam", "6. Task", "7. Final Exam"]
        y_pos = 100
        for i, event in enumerate(events):
            if i == selected_event_index:
                draw.ellipse((5, y_pos - 5, 25, y_pos + 15), outline=(255, 255, 255), fill=(255, 255, 255))
            draw.text((30, y_pos), event, font=font, fill=(255, 255, 255))
            y_pos += 20

        joystick.disp.image(image)

    # 이벤트 선택 및 실행
    def run_event(selected_event_index):
        event_number = selected_event_index
        while True:
            display_game_screen(event_number)
            if not joystick.button_U.value:
                event_number = max(0, event_number - 1)
            elif not joystick.button_D.value:
                event_number = min(6, event_number + 1)
            elif not joystick.button_L.value:
                break
            time.sleep(0.2)

        if event_number == 0:
            return event.event2()
        elif event_number == 1:
            return event.event3(joystick)
        elif event_number == 2:
            return event.event4()
        elif event_number == 3:
            return event.event5()
        elif event_number == 4:
            return event.event6()
        elif event_number == 5:
            return event.event7()
        elif event_number == 6:
            return event.event8()

    # 메인 게임 루프
    while True:
        display_game_screen(selected_event_index)
        result = run_event(selected_event_index)
        if result:  # event8 함수에서 True 반환 시
            display_game_finish_screen(joystick)  # 게임 종료 화면 표시 함수 호출
            break  # 게임 루프 종료
        print(result)
        time.sleep(2)

if __name__ == "__main__":
    main()