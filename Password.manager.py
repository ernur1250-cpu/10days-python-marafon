baza = {}

while True:
    print("\n--- 🔐 ҚҰПИЯ СӨЗ МЕНЕДЖЕРІ ---")
    print("1. Жаңа құпия сөз қосу")
    print("2. Барлық құпия сөздерді көру")
    print("3. Бағдарламадан шығу")
    
    tandau = input("\nӘрекетті таңдаңыз (1/2/3): ")
    
    if tandau == "1":
        sayt = input("Сайт немесе қосымша аты: ")
        parol = input("Құпия сөз: ")
        baza[sayt] = parol
        print(f"✅ {sayt} үшін құпия сөз сақталды!")
        
    elif tandau == "2":
        if not baza:
            print("📭 База әлі бос!")
        else:
            print("\n📋 СІЗДІҢ ҚҰПИЯ СӨЗДЕРІҢІЗ:")
            for sayt_aty, sayt_paroli in baza.items():
                print(f"🌐 {sayt_aty}: {sayt_paroli}")
                
    elif tandau == "3":
        print("👋 Сау болыңыз! Қауіпсіздікте болыңыз.")
        break
        
    else:
        print("❌ Қате таңдау! Тек 1, 2 немесе 3-ті басыңыз.")
      
