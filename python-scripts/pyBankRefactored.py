import csv

def pyBank(csv_file):
    unique_month_count, net_total, average_change = calculate_unique_months_net_total_and_average_change(csv_file)
    greatest_profit, greatest_loss, greatest_profit_date, greatest_loss_date = calculate_greatest_profit_and_greatest_loss(csv_file)
    print("=============================================================")
    print(f"Unique months               : {unique_month_count}")
    print(f"Total                       : ${net_total}")
    print(f"Average change              : ${round(average_change ,2)}")
    print(f"Greatest increase in profits: {greatest_profit_date} ($ {str(greatest_profit)} )")
    print(f"Greatest decrease in profits: {greatest_loss_date} ($ {str(greatest_loss)} )")
    print("=============================================================")

def calculate_unique_months_net_total_and_average_change(csv_file):
    with open(csv_file, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)
        previous_amount = int(next(data)[1])
        unique_months = set()
        net_total = 0
        chg_sum = 0
        row_count = 0
        for row in data:
            row_count += 1
            unique_months.add(row[0])
            net_total = net_total + int(row[1])
            current_amount = int(row[1])
            chg_sum += (current_amount - previous_amount)
            previous_amount = current_amount
        unique_month_count = len(unique_months)
        average_change = chg_sum / (row_count - 1)
    return unique_month_count, net_total, average_change


def calculate_greatest_profit_and_greatest_loss(csv_file):
    with open(csv_file, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)
        previous_amount = int(next(data)[1])
        current_max_inc = 0
        current_max_dec = 0
        current_max_inc_date = ""
        current_max_dec_date = ""
        for row in data:
            current_amount = int(row[1])
            change = current_amount - previous_amount
            date = row[0]
            if (current_amount > previous_amount) and (change > current_max_inc):
                current_max_inc = change
                current_max_inc_date = date
            if (current_amount < previous_amount) and (change < current_max_dec):
                current_max_dec = change
                current_max_dec_date = date
            previous_amount = current_amount
        greatest_profit = current_max_inc
        greatest_profit_date = current_max_inc_date
        greatest_loss = current_max_dec
        greatest_loss_date = current_max_dec_date
    return greatest_profit, greatest_loss, greatest_profit_date, greatest_loss_date