#Character.py
import numpy as np
import time

class Character:
    def __init__(self):
        self.health = 100  # 체력
        self.study = 0     # 공부량
        self.tasks = 0
    
    def recover_health(self, amount):
        # 체력 회복
        self.health += amount
        if self.health > 100:
            self.health = 100
            
    def increase_study(self, amount):
        # 공부량 증가
        self.study += amount
        
    def complete_tasks(self):
            # 과제 완료 처리
        self.tasks += 1
        
    