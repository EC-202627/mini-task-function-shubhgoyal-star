def calculate_fine(book_title,days_overdue,daily_rate=5.00,max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


book_title = input()
days_overdue = int(input())

fine = calculate_fine(book_title,days_overdue)

print("book:",book_title)
print("days overdue:", days_overdue)
print("fine: Rs.",float(fine))