'''A bakery sells loaves of bread for 185 rupees each. Day old bread is discounted by 60 
percent. Write a program that begins by reading the number of loaves of day old bread being 
purchased from the user. Then your program should display the regular price for the bread, 
the discount because it is a day old, and the total price. All of the values should be displayed 
using two decimal places, and the decimal points in all of the numbers should be aligned 
when reasonable values are entered by the user.
'''

new_count=int(input("Enter the Number of new loaves purchased : "))
old_count=int(input("Enter the Number of old loaves purchased : "))
rate_old=(185-(0.6*185))*old_count
rate_new=185*new_count
print("Regular Price : Rs. 185")
print("Old loaves Amount : Rs. ",rate_old)
print("New loaves Amount : Rs. ",rate_new)
print("Total Amount : Rs. ",rate_old+rate_new)
