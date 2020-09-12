import re

count_of_rows_and_total_sum = input()
count_of_rows = int(count_of_rows_and_total_sum[0:4].rstrip())
total_sum = int(count_of_rows_and_total_sum[4:].rstrip())
# price_of_one_product = []
# count_of_products = []
# total_price_of_products_in_one_row = []
mistake = 0
mistake_rows = ''
total_sum_by_all_rows = 0

for i in range(count_of_rows):
    row = input()
    row = re.split('\*|=', row)

    price_of_one_product = int(row[0])
    count_of_products = int(row[1])
    total_price_of_products_in_one_row = int(row[2])

    if price_of_one_product * count_of_products != total_price_of_products_in_one_row:
        mistake += abs(total_price_of_products_in_one_row - price_of_one_product * count_of_products)
        mistake_rows += str(i + 1) + ' '
        total_sum_by_all_rows += total_price_of_products_in_one_row
    else:
        total_sum_by_all_rows += total_price_of_products_in_one_row
print(total_sum - total_sum_by_all_rows + mistake)
print(mistake_rows)
