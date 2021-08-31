#An online retailer sells two products. widgets and gizmos. Each widget weighs 75 grams, while each gizmo weighs 112 grams.
#Write a program that displays the total weight of an order, in kilograms, given two variables containing the number of widgets
#and gizmos.

#Solution

# 1 widget = 75g
# 1 gizmos = 112g
# 1000g = 1kg
CustomerName = input('Kindly provide your name ')
try:
    Widget_quantity_ordered = float(input('How many quantities of widgets do you need? '))
    Gizmos_quantity_ordered = float(input('How many quantities of gizmos do you want? '))
    Total_Widget_weight_in_grams = Widget_quantity_ordered * 75
    Total_Gizmos_weight_in_grams = Gizmos_quantity_ordered * 112
    Total_weight_of_an_order_in_grams = Total_Widget_weight_in_grams + Total_Gizmos_weight_in_grams
    Total_weight_of_an_order_in_kilograms = Total_weight_of_an_order_in_grams / 1000
    print(f"Dear {CustomerName}, you have just ordered {Total_weight_of_an_order_in_kilograms}kg of widgets and gizmos")
except:
    print('Quantities should be in whole numbers')
finally:
    print(f"Thank you {CustomerName} for doing business with us")