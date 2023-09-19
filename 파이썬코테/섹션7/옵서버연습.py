class WeatherStation:
    def __init__(self):
        self.subscribers=[]
    def add(self, subscriber):
        self.subscribers.append(subscriber)
    def remove(self, subscriber):
        self.subscribers.remove(subscriber)
    def notify(self, temp, hum):
        for subscriber in self.subscribers:
            subscriber.update(temp, hum)
class Subscriber:
    def __init__(self, name):
        self.name=name
    def update(self, temp, hum):
        print(f"{self.name} : 현재 온도 {temp}도, 습도 {hum}%")
weatherStation=WeatherStation()
subscriber1=Subscriber("구독자1")
subscriber2=Subscriber("구독자2")
subscriber3=Subscriber("구독자3")
weatherStation.add(subscriber1)
weatherStation.add(subscriber2)
weatherStation.add(subscriber3)
weatherStation.notify(25,70)
weatherStation.notify(28,65)

weatherStation.remove(subscriber2)
weatherStation.notify(30, 80)