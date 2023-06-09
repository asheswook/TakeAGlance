users = []

def select_menu():
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 종료")
    menu = input("메뉴를 선택하세요 : ")
    return int(menu)

def register():
    id = input("아이디 : ")
    password = input("비밀번호 : ")

    user = {"id": id, "password": password}
    users.append(user)

    print("회원가입이 완료되었습니다.")

def login():
    id = input("아이디 : ")
    password = input("비밀번호 : ")

    for user in users:
        if user["id"] == id and user["password"] == password:
            print("로그인에 성공했습니다.")
            return user["id"]

    print("로그인에 실패했습니다.")

def main():
    while True:
        menu = select_menu()

        if menu == 1:
            register()
        elif menu == 2:
            name = login()
            if name != None:
                print(name, "님 환영합니다.")
                break
        elif menu == 3:
            break
        else:
            print("잘못된 메뉴입니다.")


main()