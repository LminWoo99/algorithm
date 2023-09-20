from abc import ABC, abstractmethod
#subjecy
class Observable(ABC):
    def __init__(self):
        self.subscribers = []
    #옵서버 등록
    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)
    #옵서버 알림
    def notify_subscribers(self, weather_info):
        for subscriber in self.subscribers:
            subscriber.update(weather_info)

class Weather(Observable):
    def set_weather_info(self, weather_info):
        self.notify_subscribers(weather_info)
#옵서버
class Subscriber:
    def update(self, weather_info):
        pass
#옵서버 상속
class WeatherSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, weather_info):
        print(f"구독자{self.name}: {weather_info}")

# 클라이언트 코드
weather_station = Weather()
subscriber1 = WeatherSubscriber(1)
subscriber2 = WeatherSubscriber(2)
subscriber3 = WeatherSubscriber(3)

weather_station.add_subscriber(subscriber1)
weather_station.add_subscriber(subscriber2)
weather_station.add_subscriber(subscriber3)

weather_station.set_weather_info("현재 온도 25도 , 습도 70%")
weather_station.set_weather_info("현재 온도 28도 , 습도 65%")

weather_station.remove_subscriber(subscriber2)

weather_station.set_weather_info("현재 온도 30도 , 습도 75%")


