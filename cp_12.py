# 음료 클래스 정의
class Beverage:
    # 생성자 메서드 음료 이름과 가격의 매개변수 생성
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #  주어진 수량에 따른 총 가격 계산
    def calculate(self, quantity):
        return self.price * quantity

# 메인 함수 정의
def main():
    # 음료 객체 생성
    coffee = Beverage("커피", 3000)
    green_tea = Beverage("녹차", 2500)
    ice_tea = Beverage("아이스티", 3000)

    # 첫 번째 사용자 입력 받기
    selected_beverage = input("주문할 음료를 선택하세요 (커피/녹차/아이스티): ")

    # 입력이 올바른지 확인
    if selected_beverage not in ["커피", "녹차", "아이스티"]:
        print("잘못된 음료를 선택하셨습니다.")
        return

    # 선택된 음료 객체 찾기
    beverage = None
    if selected_beverage == "커피":
        beverage = coffee
    elif selected_beverage == "녹차":
        beverage = green_tea
    else:
        beverage = ice_tea

    # 두 번째 사용자 입력 받기
    try:
        quantity = int(input("수량을 입력하세요: "))
    except ValueError:
        print("잘못된 수량 입력입니다.")
        return

    # 총 가격 계산 및 출력문
    total_price = beverage.calculate(quantity)
    print(f"{beverage.name} {quantity}개의 총 가격은 {total_price}원입니다.")

if __name__ == "__main__":
    main()
