class Pharmacy:
    def __init__(self,pharmacy_name,pharmacy_address) -> None:
        self.pharmacy_name = pharmacy_name
        self.pharmacy_address = pharmacy_address
        self.pharmacy_medicines = {}
        self.pharmacy_cash_balance = 0.0

    def get_medicines_info(self) -> str:
        for i in self.pharmacy_medicines:
            print(f"{i} - {self.pharmacy_medicines[i]['price']} so'm, {self.pharmacy_medicines[i]['quantity']} dona")

    def add_medecine(self, medicine: str, price: float, quantity: int) -> None:
        self.pharmacy_medicines.setdefault(medicine,{'price':price,'quantity':quantity})

    def remove_medicine(self, medicine: str) -> bool:
        if medicine in self.pharmacy_medicines:
            self.pharmacy_medicines.pop(medicine)
            return True
        return False

    def add_money(self,amount: float) -> str:
        self.pharmacy_cash_balance+=amount

    def sell_medicine(self, medicine: str, quantity: int) -> bool:
        if medicine in self.pharmacy_medicines:
            self.pharmacy_medicines[medicine]['quantity']-=quantity
            dorixona.add_money(self.pharmacy_medicines[medicine]['price']*quantity)
            return True
        return False

    def update_medicine_price(self, medicine: str, new_price: float) -> None:
            self.pharmacy_medicines[medicine]['price']=new_price

    def check_medicine_stock(self, medicine: str) -> int:
        return self.pharmacy_medicines[medicine]['quantity']

    def total_medicines_value(self) -> float:
        count = 0
        for i in self.pharmacy_medicines:
            count+=self.pharmacy_medicines[i]['price']*self.pharmacy_medicines[i]['quantity']
        return count

dorixona = Pharmacy("Shifokor Dorixonasi","Toshkent, O'zbekiston")

# dorixona.add_money(550.4)

dorixona.add_medecine("Paracetamol",2000,50)
print("50 dona Paracetamol dori qo'shildi.\n")

dorixona.add_medecine("Ibufen",3000,30)
print("30 dona Ibufen dori qo'shildi.\n")

dorixona.get_medicines_info()

if dorixona.sell_medicine("Paracetamol",10):
    print("\n10 dona Paracetamol dori sotildi. Jami: 20000 so'm\nHisobga 20000 so'm pul qo'shildi. Joriy balans: 20000 so'm\n")

dorixona.get_medicines_info()

if dorixona.remove_medicine("Ibufen"):
    print("Ibufen dori o'chirildi.\n")
else:
    print("Bunday dori turi mavjud emas!\n")

dorixona.get_medicines_info()

dorixona.update_medicine_price("Paracetamol",2500)
print("\nParacetamol dori narxi yangilandi. Yangi narx 2500 so'm\n")

print(dorixona.check_medicine_stock("Paracetamol"))

print(f"\nDorixonadagi jammi dorilar qiymati: {dorixona.total_medicines_value()} so'm")