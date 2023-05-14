class Food:
   def __init__(self):
        print("음식 주문")
   def __isAvailable(self): # 예약 가능 확인 메소드
        print("음식 주문 가능 한가요?")
        return True
   def bookFood(self):
        if self.__isAvailable():
            print("주문이 완료되었습니다 \n\n")
            
class Service:
   def __init__(self):
        print("배송 서비스")
   def __isAvailable(self): # 예약 가능 확인 메소드
        print("이제품 배송 가능한가요")
        return True
   def bookService(self):
        if self.__isAvailable():
            print("배송 예약이 완료되었습니다 \n\n")
class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    def arrange(self):
        self.food = Food()
        self.food.bookFood()
        self.service = Service()
        self.service.bookService()
        
class You(object):
    def __init__(self):
        print("You:: 음식 주문과 배송서비스입니다")
    def askEventManager(self):
        print("You:: 이벤트 매니저 만나볼게요. \n\n")
        em = EventManager()
        em.arrange()
you = You()
you.askEventManager()
