import random

# fw = random.random()
# print(fw)
class mng:
    tick = 1
print(mng.tick)

class ai(mng):
    print("--- 시작")
    def ai_move(self):
        self.ai_tick = 0
        self.tick = mng.tick
        self.ai_fw = random.random()
        self.x = 13
        self.y = 13
        self.next_x = 0
        self.next_y = 0
        print("--- 중간")
        if self.tick > self.ai_tick:
            self.ai_tick = self.tick
            if self.ai_fw < 0.25:
                self.next_x = self.x - 1
                self.next_y = self.y
            elif self.ai_fw < 0.5:
                self.next_y = self.y - 1
                self.next_x = self.x
            elif self.ai_fw < 0.75:
                self.next_x = self.x + 1
                self.next_y = self.y
            else:
                self.next_y = self.y + 1
                self.next_x = self.x
            return self.next_x, self.next_y
        print(self.next_x, self.next_y, "--------------")

ai.ai_move
# print(x, y)