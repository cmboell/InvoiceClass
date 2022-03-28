"""
Assignment name: Invoice class assignment
Program: invoice.py
Author: Colby Boell
Last date modified: 03/27/2022

The purpose of this program is to use a class to take in information and store it and then call
functions to create and display an invoice of items.
"""


class Invoice:
    # invoice class
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price=None):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        if items_with_price is None:
            self.items_with_price = dict()
        else:
            self.items_with_price = items_with_price

    # function to add items to the dictionary
    def add_item(self, item):
        key = list(item.keys())[0]
        self.items_with_price[key] = item[key]

    # function to create and print out invoice
    def create_invoice(self):
        total = 0
        for item, cost in self.items_with_price.items():
            total += cost
            print(str(item) + ".....$" + str(cost))
        tax = total * .06
        total += tax
        print("Tax.........$" + str(round(tax, 2)))
        print("Total.......$" + str(round(total, 2)))


# Driver code
if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()



