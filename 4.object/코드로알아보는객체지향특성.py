"""객체지향특성
    참고자료: https://yansfil.github.io/awesome-class-materials/3.object-oriented/5.%20%EC%BD%94%EB%93%9C%EB%A1%9C%20%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94%20%EA%B0%9D%EC%B2%B4%20%EC%A7%80%ED%96%A5%EC%9D%98%20%ED%8A%B9%EC%84%B1.html
    
    주요내용
    
    객체지향의 특성 4가지:
        1. 상속
        2. 추상화
        3. 다형성
        4. 캡슐화: 객체 내부의 데이터나 메서드의 구체적인 로직을 외부에서 모르고 사용해도 문제가 없도록 하는 특성
    
    객체지향의 설계 5원칙 (SOLID)
        1. SRP(Single Responsibility Principle)
            - 하나의 객체는 하나의 책임만 가지도록 설계하는 것이 일반적으로 좋다.
        2. OCP(Open-Close Principle)
            - 소프트웨어는 확장에 대해 열려 있어야 하고, 수정에 대해서는 닫혀 있어야 한다는 원칙입니다.
            - 쉽게 말해, 요구사항이 바뀌어 기존 코드를 변경해야 할 때, 기존 코드를 수정하지 않고 새로운 코드를
              추가하는 것이 좋다는 것입니다.
    책임주도 설계: 객체들의 인스턴스, 메써드보다 객체들의 책임부터 정의하고 시스템을 설계한다.
"""

# 책임
class User:
    def __init__(self) -> None:
        pass

    def drive(self) -> None:
        pass


class MorningCar:
    def __init__(self) -> None:
        pass

    def accelerate(self) -> None:
        pass

    def decelerate(self) -> None:
        pass


# 협력
class User:
    def __init__(self) -> None:
        self.car = MorningCar()  # User는 MorningCar를 의존하고 있습니다.

    def drive(self) -> None:
        self.car.accelerate()  # User는 MorningCar가 제공하는 공개 메서드를 사용합니다.


class MorningCar:
    def __init__(self):
        self.speed = 0
        self._fuel = 0  # 파이썬 특성상 private을 _ prefix를 붙여 암묵적으로 사용함

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class PorscheCar:
    def __init__(self):
        self.speed = 0
        self._fuel = 0

    def accelerate(self):
        self.speed += 3

    def decelerate(self):
        self.speed -= 3


# 추상화: 추상화가 없을 때
class User:
    def __init__(self, car_name: str) -> None:
        if car_name == "morning":
            self.car = MorningCar()
        elif car_name == "porsche":
            self.car = PorscheCar()

    def drive(self):
        self.car.accelerate()


print("추상화 미적용")

m = User("morning")
p = User("porsche")

m.drive()
print(f"모닝 속도: {m.car.speed}")
p.drive()
print(f"포르쉐 속도: {p.car.speed}")

# 추상화: 추상화가 있을 때

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def decelerate(self) -> None:
        pass


class MorningCar(Car):
    def __init__(self) -> None:
        self.speed = 0
        self._fuel = 0

    def accelerate(self) -> None:
        self.speed += 1

    def decelerate(self) -> None:
        self.speed -= 1


class PorscheCar(Car):
    def __init__(self) -> None:
        self.speed = 0
        self._fuel = 0

    def accelerate(self) -> None:
        self.speed += 3

    def decelerate(self) -> None:
        self.speed -= 3


class User:
    def __init__(self, car: Car) -> None:  # 클래스를 받는 것을 이런식으로 표현하는 구나, 배우고 간다.
        self.car = car

    def drive(self):
        self.car.accelerate()


# 다형성
print("추상화 적용")

# 모닝 차량을 운전하고 싶을 때
user = User(MorningCar())
user.drive()
print(f"모닝 속도: {user.car.speed}")

# 포르쉐 차량을 운전하고 싶을 때
user = User(PorscheCar())
user.drive()
print(f"포르쉐 속도: {user.car.speed}")

# 캡슐화
# - 객체 내부의 데이터나 메서드의 구체적인 로직을 외부에서 모르고 사용해도 문제가 없도록 하는 특성
print("캡술화 예제: 캡슐화하지 않을 때")


class MorningCar:
    def __init__(self, fuel: int) -> None:
        self.speed = 0
        self._current_fuel = fuel
        self.max_fuel = 50
        if fuel > self.max_fuel:
            raise Exception(f"최대로 넣을 수 있는 기름은 {self.max_fuel}L 입니다")

    def accelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 기름이 없습니다")
        self.speed += 1
        self._current_fuel -= 1

    def decelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 기름이 없습니다")
        self.speed -= 1
        self._current_fuel -= 1


# 차량 생성
car = MorningCar(50)

for i in range(45):
    print(f"현재 속도는 {car.speed}입니다.")
    car.accelerate()

car._current_fuel += 50
print(car._current_fuel)

print(f"남은 기름은 {round(car._current_fuel / car.max_fuel * 100, 1)} % 입니다.")

# 캡슐화
print("캡술화 예제: 캡슐화 했을 때")


class MorningCar:
    def __init__(self, fuel: int) -> None:
        self.speed = 0
        self._current_fuel = fuel  # 비공개형 변수로 바꿉니다.
        self._max_fuel = 50  # 비공개형 변수로 바꿉니다.
        if fuel > self._max_fuel:
            raise Exception(f"최대로 넣을 수 있는 기름은 {self._max_fuel}L 입니다!")

    def accelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 기름이 없습니다!")
        self.speed += 1
        self._current_fuel -= 1

    def decelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 기름이 없습니다!")
        self.speed -= 1
        self._current_fuel -= 1

    # 차량에 주유할 수 있는 기능을 메서드로 제공하고, 구체적인 로직은 객체 외부에서 몰라도 되도록 메서드 내에 둡니다.
    def refuel(self, fuel: int) -> None:
        if self._current_fuel + fuel > self._max_fuel:
            raise Exception(
                f"추가로 더 넣을 수 있는 최대 연료는 {self._max_fuel - self._current_fuel}L 입니다!"
            )
        self._current_fuel += fuel

    # 차량의 남은 주유랑을 퍼센트로 확인하는 기능을 메서드로 제공합니다.
    def get_current_fuel_percentage(self) -> str:
        return f"{self._current_fuel / self._max_fuel * 100} %"


car = MorningCar(50)

for i in range(45):
    print(f"현재 속도는 {car.speed}입니다.")
    car.accelerate()
    print(car.get_current_fuel_percentage())

try:
    car.refuel(50)
except Exception as e:
    print(e)

car.refuel(30)

print(car.get_current_fuel_percentage())
