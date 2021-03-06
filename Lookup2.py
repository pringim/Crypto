from tkinter import *
import requests
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime, date

os.system('cls')
root = Tk()
root.iconbitmap("Python.ico")
root.title('Portfolio App')
root.geometry("885x180+345+100")

# global row_x
# row_x = 2

def red_green(amount):
    if amount < 0:
        return 'red'
    else:
        return 'green'


header_name = Label(root, text=' Name ', bg="white", font="Verdana 8 bold")
header_name.grid(row=0, column=0, pady=10, sticky=N + S + E + W)

header_rank = Label(root, text='Rank', bg="silver", font="Verdana 8 bold")
header_rank.grid(row=0, column=1, pady=10, sticky=N + S + E + W)

header_holding = Label(root, text='Holding', bg="white", font="Verdana 8 bold")
header_holding.grid(row=0, column=2, pady=10, sticky=N + S + E + W)

header_current_price = Label(root, text='Current Price', bg="silver", font="Verdana 8 bold")
header_current_price.grid(row=0, column=3, pady=10, sticky=N + S + E + W)

header_price_paid = Label(root, text='Price Paid', bg="white", font="Verdana 8 bold")
header_price_paid.grid(row=0, column=4, pady=10, sticky=N + S + E + W)

header_coin_cost = Label(root, text='Investment Cost', bg="silver", font="Verdana 8 bold")
header_coin_cost.grid(row=0, column=5, pady=10, sticky=N + S + E + W)

header_1_hr_change = Label(root, text='1 Hr Change', bg="white", font="Verdana 8 bold")
header_1_hr_change.grid(row=0, column=6, pady=10, sticky=N + S + E + W)

header_24_hr_change = Label(root, text='24 Hr Change', bg="silver", font="Verdana 8 bold")
header_24_hr_change.grid(row=0, column=7, pady=10, sticky=N + S + E + W)

header_7_day_change = Label(root, text='7 Day Change', bg="white", font="Verdana 8 bold")
header_7_day_change.grid(row=0, column=8, pady=10, sticky=N + S + E + W)

header_current_value = Label(root, text='Current Value', bg="silver", font="Verdana 8 bold")
header_current_value.grid(row=0, column=9, pady=10, sticky=N + S + E + W)

header_profit_loss_total = Label(root, text='Profit Loss', bg="white", font="Verdana 8 bold")
header_profit_loss_total.grid(row=0, column=10, pady=10, sticky=N + S + E + W)


# "percent_change_1h":-0.00533761, "percent_change_24h":1.38556215,"percent_change_7d":3.58384493,
def lookup():
    ########################################################################################################################
    # CoinMarketCap.com
    prices_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=56a4fd0b-671e-4bb2-85f3-924f108f54b5&start=1&limit=5000&convert=GBP"
    # Cryptocompare.com
    # prices_url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,EOS,STEEM&tsyms=GBP&api_key=eb6b307109e93942aff7abb7ba16b48b58eda01affbfc4a65955d301b956b851'
    prices_request = requests.get(prices_url)
    prices_response = json.loads(prices_request.content)

    # ,ETH,XRP,BCH,EOS,LTC,ADA,XLM,MIOTA,USDT,TRX
    #########################################################################################################################
    data = prices_response['data']
    syms = ["XRP", "EOS", "STEEM", 'BTC','BCH',"MIOTA"]

    my_portfolio = [
        {"sym": "MIOTA",
         "amount_owned": "500",
         "price_paid_24july20": 0.21
         },
        {"sym": "EOS",
         "amount_owned": "500",
         "price_paid_24july20": 2.05
         },
        {"sym": "XRP",
         "amount_owned": "500",
         "price_paid_24july20": 0.16
         },
        {"sym": "XTZ",
         "amount_owned": "33",
         "price_paid_24july20": 2.44
         }
    ]

    portfolio_profit_loss = 0
    portfolio_outlay = 0
    total_current_value = 0
    global row_x
    row_x = 1
    pie = []
    pie_size = []
    for x in range(0, len(data)):
        # for y in syms:
        for coin in my_portfolio:
            temp_data = data[x]
            if temp_data['symbol'] == coin['sym']:
                total_paid = float(coin['amount_owned']) * float(coin['price_paid_24july20'])
                current_value = float(coin['amount_owned']) * (float(temp_data['quote']['GBP']['price']))
                profit_loss = current_value - total_paid
                # profit_loss_per_coin = (float(temp_data['quote']['GBP']['price'])) - float(coin['price_paid_24july20'])
                portfolio_outlay += total_paid
                portfolio_profit_loss += profit_loss
                total_current_value += current_value
                pie.append(temp_data['name'])
                pie_size.append(current_value)

                name = Label(root, text=temp_data['name'], bg="white")
                name.grid(row=row_x, column=0, sticky=N + S + E + W)

                rank = Label(root, text=str(temp_data['cmc_rank']), bg="silver")
                rank.grid(row=row_x, column=1, sticky=N + S + E + W)

                holding = Label(root, text=str(float(coin['amount_owned'])), bg="white")
                holding.grid(row=row_x, column=2, sticky=N + S + E + W)

                current_price = Label(root, text=('£{0:.3f}'.format(float(temp_data['quote']['GBP']['price']))),
                                      bg="silver")
                current_price.grid(row=row_x, column=3, sticky=N + S + E + W)

                price_paid = Label(root, text=('£{0:.3f}'.format(float(coin['price_paid_24july20']))), bg="white")
                price_paid.grid(row=row_x, column=4, sticky=N + S + E + W)

                coin_cost = Label(root, text=('£{0:.3f}'.format(float(total_paid))), bg="silver")
                coin_cost.grid(row=row_x, column=5, sticky=N + S + E + W)

                one_hr_change = Label(root,
                                      text=('{0:.2f}%'.format(float(temp_data['quote']['GBP']['percent_change_1h']))),
                                      bg="white", fg=red_green(float(temp_data['quote']['GBP']['percent_change_1h'])))
                one_hr_change.grid(row=row_x, column=6, sticky=N + S + E + W)

                tf_hr_change = Label(root,
                                     text=('{0:.2f}%'.format(float(temp_data['quote']['GBP']['percent_change_24h']))),
                                     bg="silver", fg=red_green(float(temp_data['quote']['GBP']['percent_change_24h'])))
                tf_hr_change.grid(row=row_x, column=7, sticky=N + S + E + W)

                seven_day_change = Label(root, text=('{0:.2f}%'.format(float(temp_data['quote']['GBP']['percent_change_7d']))), bg="white",
                                         fg=red_green(float(temp_data['quote']['GBP']['percent_change_7d'])))
                seven_day_change.grid(row=row_x, column=8, sticky=N + S + E + W)

                current_value = Label(root, text=('£{0:.3f}'.format(current_value)), bg="silver")
                current_value.grid(row=row_x, column=9, sticky=N + S + E + W)

                profit_loss_total = Label(root, text=('£{0:.3f}'.format(profit_loss)), bg="white",
                                          fg=red_green(profit_loss))
                profit_loss_total.grid(row=row_x, column=10, sticky=N + S + E + W)

                row_x += 1
    day_of_year = datetime.now().timetuple().tm_yday
    day_of_year2 = date(2020, 7, 24).timetuple().tm_yday
    no_days = day_of_year - day_of_year2
    total_profit_loss = (float(portfolio_profit_loss))
    daily_profit = total_profit_loss / no_days
    root.title("Crypto Currency Portfolio - Value: £{0:.2f}".format(float(total_current_value))
               + " --Investment: £" + str(portfolio_outlay) + " --Total Profit/Loss: " + "£{0:.2f}".format(float(portfolio_profit_loss))
               + " = £{0:.2f}".format(float(daily_profit)) + " per day -- StartDate 24/07/20")

    update_button = Button(root, text="Update Prices", command=lookup)
    update_button.grid(row=row_x, column=10, padx=10, pady=10, sticky=E + S)

    # Pie Chart
    def graph(labels, pie_size):
        labels = pie
        sizes = pie_size
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    graph_button = Button(root, text="Pie Chart", command= lambda: graph(pie, pie_size))
    graph_button.grid(row=row_x, column=8, padx=10, pady=10, sticky=E + S)


    def records():
        path = "C:/Users/Ian/PycharmProjects/Gui/Docs/"
        top = Toplevel()
        top.title(" Porfolio Records of Transaction --- Start Date 24/7/20")
        text_file = open(path + "sample.txt", 'r')
        stuff = text_file.read()

        my_text = Text(top, width=100, height=15, font=('helvetica', 10))
        my_text.pack(pady=20)

        my_text.insert(END, stuff)
        text_file.close()

        def save_text():
            text_file = open(path + "sample.txt", 'w')
            text_file.write(my_text.get(1.0, END))
            top.destroy()


        save_button = Button(top, text="Save & Exit", command=save_text)
        save_button.pack(pady=20)

    record_button = Button(root, text="Portfolio Records", command=records)
    record_button.grid(row=row_x, column=5, pady=10, sticky=E + S)


lookup()
mainloop()

########################################################################################################################