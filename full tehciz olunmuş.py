# Sadə qeydiyyat və giriş sistemi

import datetime

# İstifadəçi məlumatlarını saxlayan dictionary
users = {}
roles = {}  # Hər istifadəçinin rolunu saxlamaq üçün dictionary
activity_log = []  # İstifadəçi fəaliyyətlərini qeyd etmək üçün siyahı

def log_activity(username, action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    activity = f"{timestamp} - {username}: {action}"
    activity_log.append(activity)
    print(activity)  # Hər fəaliyyəti ekrana da çap edirik

def register_user():
    try:
        username = input("Qeydiyyat üçün istifadəçi adı daxil edin: ")
        if not username:
            raise ValueError("İstifadəçi adı boş ola bilməz!")
        
        passcode = input("Qeydiyyat üçün şifrə daxil edin: ")
        if not passcode:
            raise ValueError("Şifrə boş ola bilməz!")
        
        role = input("İstifadəçi rolu seçin (admin/user): ").strip().lower()
        if role not in ["admin", "user"]:
            raise ValueError("Yanlış rol! Yalnız 'admin' və ya 'user' seçilə bilər.")
        
        users[username] = passcode
        roles[username] = role
        log_activity(username, "qeydiyyatdan keçdi")
        print("Qeydiyyat uğurla tamamlandı!\n")
    except ValueError as e:
        print(f"Xəta: {e}")

def login_user():
    try:
        username_login = input("Daxil ol: İstifadəçi adınızı daxil edin: ")
        passcode_login = input("Daxil ol: Şifrənizi daxil edin: ")
        
        if not username_login or not passcode_login:
            raise ValueError("İstifadəçi adı və ya şifrə boş ola bilməz!")
        
        if username_login in users and users[username_login] == passcode_login:
            print(f"Xoş gəldiniz, {username_login}! Sizin rolunuz: {roles[username_login]}")
            log_activity(username_login, "sistemə daxil oldu")
        else:
            print("İstifadəçi adı və ya şifrə səhvdir!")
    except ValueError as e:
        print(f"Xəta: {e}")

def delete_account():
    try:
        username = input("Silinəcək hesabın adını daxil edin: ")
        if username in users:
            del users[username]
            del roles[username]
            log_activity(username, "hesabını sildi")
            print(f"{username} adlı istifadəçi uğurla silindi!")
        else:
            print("Bu adla istifadəçi tapılmadı!")
    except Exception as e:
        print(f"Xəta baş verdi: {e}")

def admin_panel():
    print("\n*** Admin Paneli ***")
    if not any(role == "admin" for role in roles.values()):
        print("Admin mövcud deyil!")
        return
    
    while True:
        try:
            print("\n1. İstifadəçiləri göstər")
            print("2. İstifadəçi sil")
            print("3. Fəaliyyət loglarını göstər")
            print("4. Admin panelindən çıx")
            choice = input("Seçiminizi daxil edin: ")
            
            if choice == "1":
                print("\nİstifadəçilər:")
                for user, role in roles.items():
                    print(f"İstifadəçi: {user}, Rol: {role}")
            elif choice == "2":
                user_to_delete = input("Silinəcək istifadəçini daxil edin: ")
                if user_to_delete in users:
                    del users[user_to_delete]
                    del roles[user_to_delete]
                    log_activity(user_to_delete, "admin tərəfindən silindi")
                    print(f"{user_to_delete} istifadəçi bazadan silindi!")
                else:
                    print("Bu adla istifadəçi tapılmadı!")
            elif choice == "3":
                print("\nFəaliyyət Logları:")
                for log in activity_log:
                    print(log)
            elif choice == "4":
                print("Admin panelindən çıxılır...")
                break
            else:
                raise ValueError("Yanlış seçim! 1, 2, 3 və ya 4 seçin.")
        except ValueError as e:
            print(f"Xəta: {e}")

def main():
    while True:
        try:
            print("\n1. Qeydiyyat")
            print("2. Giriş")
            print("3. Hesabı sil")
            print("4. Admin Paneli")
            print("5. Çıxış")
            choice = input("Seçiminizi daxil edin: ")
            
            if choice == "1":
                register_user()
            elif choice == "2":
                login_user()
            elif choice == "3":
                delete_account()
            elif choice == "4":
                admin_panel()
            elif choice == "5":
                print("Sistemdən çıxılır...")
                break
            else:
                raise ValueError("Yanlış seçim! Zəhmət olmasa 1, 2, 3, 4 və ya 5 seçin.")
        except ValueError as e:
            print(f"Xəta: {e}")

if __name__ == "__main__":
    main()
