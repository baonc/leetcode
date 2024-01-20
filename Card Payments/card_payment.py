def solution(a, d, n):
    monthly_transaction = {}
    month_in_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    
    # Initialize transaction for each month.
    for i in range(len(month_in_year)):
        monthly_transaction[month_in_year[i]] = []
    
    print("montly transaction ", monthly_transaction)
    for i in range(n):
        trans_amount = a[i]
        trans_month = d[i].split("-")[1]
        trans = monthly_transaction[trans_month]
        trans.append(trans_amount)
        monthly_transaction[trans_month] = trans
    print("montly transaction ", monthly_transaction)
    final_balance = 0
    for k, v in monthly_transaction.items():
        final_balance = final_balance - check_fee(v)
        for tran in v:
            final_balance = final_balance + tran
    return final_balance

def check_fee(trans):
    fee = 5
    total_amount = 0
    total_trans = 0
    for tran in trans:
        if tran < 0:
            total_amount = total_amount + tran
            total_trans = total_trans + 1
    if total_trans >=3 and total_amount <= -100:
        fee = 0
    return fee

print("Solution: ", solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"], 4))
print("Solution: ", solution([180, -50, -25, -25], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"], 4))
print("Solution: ", solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"], 5))
print("Solution: ", solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"], 5))
print("Solution: ", solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"], 4))