price = 249.5
quantity = 60
discount = 0.4
delivery1 = 100
quantity_books_for_delivery1 = 1
delivery2 = 49.5

subtotal = price * quantity
discount_amount = subtotal * discount
price_after_discount = subtotal - discount_amount
price_with_delivery1 = price_after_discount + delivery1
quantity_books_for_delivery2 = quantity - quantity_books_for_delivery1
price_with_delivery2 = quantity_books_for_delivery2 * delivery2
total_price = price_with_delivery1 + price_with_delivery2
print (total_price)