import converter_helper as ch

ans = True
while(ans):
    print("What would you like to do?")

    print("""
    1. Fahrenheit to Celsius
    2. Celsius to Fahrenheit
    3. USD to JPY
    4. JPY to USD
    5. Exit""")

    ans = input()

    if(ans == "1"):
        print(ch.f2c())
    elif(ans == "2"):
        print(ch.c2f())
    elif(ans == "3" ):   
        print("Current exchange rate is: " + str(ch.EXCHANGE_RATE) + " USD -> JPY")
        print(ch.usd2jpy())
    elif(ans == "4"):
        print("Current exchange rate is: " + str(ch.EXCHANGE_RATE) + " USD -> JPY")
        print(ch.jpy2usd())
    elif(ans == "5"):
        print("Bye!")
        exit(0)







