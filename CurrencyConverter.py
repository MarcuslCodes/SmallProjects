import time

currency_list_input = ['AUD', 'USD', 'EUR', 'GBP', 'DKK']
currency_list_output = ['AUD', 'USD', 'EUR', 'GBP', 'DKK']

print("Hi there!\n"
      "You can choose between five different currencies:\n"
      "AUD - the Australian dollar\n"
      "USD - the American dollar\n"
      "EUR - the European currency\n"
      "GBP - the British pound\n"
      "DKK - the Danish krone\n")

time.sleep(5)

currency1 = input("Which currency would you like to convert from?: ").upper()
currency2 = input("Which currency would you like to convert into?: ").upper()

while True:
    if currency1 == 'AUD' and currency2 == 'USD':
        print("You have chosen to convert from AUD to USD")
        sum_aud_usd = int(input("Please write the total sum in AUD: "))
        result = sum_aud_usd * 0.62
        round_number = round(result, 2)
        print(f"${round_number}")
    elif currency1 == 'AUD' and currency2 == 'EUR':
        print("You have chosen to convert from AUD to EUR")
        sum_aud_eur = int(input("Please write the total sum in AUD: "))
        result = sum_aud_eur * 0.60
        round_number = round(result, 2)
        print(f"€{round_number}")
    elif currency1 == 'AUD' and currency2 == 'GBP':
        print("You have chosen to convert from AUD to GBP")
        sum_aud_gbp = int(input("Please write the sum in AUD: "))
        result = sum_aud_gbp * 0.5
        round_number = round(result, 2)
        print(f"£{round_number}")
    elif currency1 == 'AUD' and currency2 == 'DKK':
        print("You have chosen to convert from AUD to DKK")
        sum_aud_dkk = int(input("Please write the sum in AUD: "))
        result = sum_aud_dkk * 4.49
        round_number = round(result, 2)
        print(f"{round_number} kr")

    if currency1 == 'USD' and currency2 == 'AUD':
        print("You have chosen to convert from USD to AUD")
        sum_usd_aud = int(input("Please write the total sum in USD: "))
        result = sum_usd_aud * 1.6
        round_number = round(result, 2)
        print(f"AUD {round_number}")
    elif currency1 == 'USD' and currency2 == 'EUR':
        print("You have chosen to convert from USD to EUR")
        sum_usd_eur = int(input("Please write the total sum in USD: "))
        result = sum_usd_eur * 0.96
        round_number = round(result, 2)
        print(f"€{round_number}")
    elif currency1 == 'USD' and currency2 == 'GBP':
        print("You have chosen to convert from USD to GBP")
        sum_usd_gbp = int(input("Please write the sum in USD: "))
        result = sum_usd_gbp * 0.8
        round_number = round(result, 2)
        print(f"£{round_number}")
    elif currency1 == 'USD' and currency2 == 'DKK':
        print("You have chosen to convert from USD to DKK")
        sum_usd_dkk = int(input("Please write the sum in USD: "))
        result = sum_usd_dkk * 7.2
        round_number = round(result, 2)
        print(f"{round_number} kr")

    if currency1 == 'EUR' and currency2 == 'AUD':
        print("You have chosen to convert from EUR to AUD")
        sum_eur_aud = int(input("Please write the total sum in EUR: "))
        result = sum_eur_aud * 1.66
        round_number = round(result, 2)
        print(f"AUD {round_number}")
    elif currency1 == 'EUR' and currency2 == 'USD':
        print("You have chosen to convert from EUR to EUR")
        sum_eur_usd = int(input("Please write the total sum in EUR: "))
        result = sum_eur_usd * 1.04
        round_number = round(result, 2)
        print(f"${round_number}")
    elif currency1 == 'EUR' and currency2 == 'GBP':
        print("You have chosen to convert from EUR to GBP")
        sum_eur_gbp = int(input("Please write the sum in EUR: "))
        result = sum_eur_gbp * 0.83
        round_number = round(result, 2)
        print(f"£{round_number}")
    elif currency1 == 'EUR' and currency2 == 'DKK':
        print("You have chosen to convert from EUR to DKK")
        sum_eur_dkk = int(input("Please write the sum in EUR: "))
        result = sum_eur_dkk * 7.46
        round_number = round(result, 2)
        print(f"{round_number} kr")

    if currency1 == 'GBP' and currency2 == 'AUD':
        print("You have chosen to convert from GBP to AUD")
        sum_gbp_aud = int(input("Please write the total sum in GBP: "))
        result = sum_gbp_aud * 2
        round_number = round(result, 2)
        print(f"AUD {round_number}")
    elif currency1 == 'GBP' and currency2 == 'USD':
        print("You have chosen to convert from GBP to EUR")
        sum_gbp_usd = int(input("Please write the total sum in GBP: "))
        result = sum_gbp_usd * 1.25
        round_number = round(result, 2)
        print(f"${round_number}")
    elif currency1 == 'GBP' and currency2 == 'EUR':
        print("You have chosen to convert from GBP to EUR")
        sum_gbp_eur = int(input("Please write the sum in GBP: "))
        result = sum_gbp_eur * 1.21
        round_number = round(result, 2)
        print(f"€{round_number}")
    elif currency1 == 'GBP' and currency2 == 'DKK':
        print("You have chosen to convert from GBP to DKK")
        sum_gbp_dkk = int(input("Please write the sum in GBP: "))
        result = sum_gbp_dkk * 17.99
        round_number = round(result, 2)
        print(f"{round_number} kr")

    if currency1 == 'DKK' and currency2 == 'AUD':
        print("You have chosen to convert from DKK to AUD")
        sum_dkk_aud = int(input("Please write the total sum in DKK: "))
        result = sum_dkk_aud * 1.66
        round_number = round(result, 2)
        print(f"AUD {round_number}")
    elif currency1 == 'DKK' and currency2 == 'USD':
        print("You have chosen to convert from DKK to EUR")
        sum_dkk_usd = int(input("Please write the total sum in DKK: "))
        result = sum_dkk_usd * 1.04
        round_number = round(result, 2)
        print(f"${round_number}")
    elif currency1 == 'DKK' and currency2 == 'EUR':
        print("You have chosen to convert from DKK to EUR")
        sum_dkk_eur = int(input("Please write the sum in DKK: "))
        result = sum_dkk_eur * 0.83
        round_number = round(result, 2)
        print(f"€{round_number}")
    elif currency1 == 'DKK' and currency2 == 'GBP':
        print("You have chosen to convert from DKK to GBP")
        sum_dkk_gbp = int(input("Please write the sum in DKK: "))
        result = sum_dkk_gbp * 7.46
        round_number = round(result, 2)
        print(f"£{round_number} kr")

    print("Would you like to convert another currency?: ")
    ans = input().lower()

    if ans == 'yes':
        print("Okay, lets go:)\n")
    elif ans == 'no':
        break


