class OrderService:
    def place_order(self,items):
        print(f"품목 주문: {items}")

class PaymentService:
    def process_payment(self,amount):
        print(f'결제: {amount}')

class DeliveryService:
    def schedule_delivery(self,address):
        print(f'배달 예약 주소: {address}')

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class OrderFacade:
    def __init__(self):
        self.order_service=OrderService()
        self.payment_service=PaymentService()
        self.delivery_service=DeliveryService()

    def place_order(self,items,address):
        self.order_service.place_order(items)
        self.payment_service.process_payment(self.calculate_total_cost(items))
        self.delivery_service.schedule_delivery(address)
        print('주문 완료')

    def calculate_total_cost(self,items):
        if not items:
            return 0
        return sum(Item.price for Item in items)

facade = OrderFacade()

items=[
    Item("Apple",1.0),
    Item("Banana",0.5),
    Item("Orange",0.75)]
address = '대한민국'

facade.place_order(items,address)
