import ast
class Bank:
    def __init__(self):
        with open('bank.txt', 'r', encoding='utf-8') as file:
            self.lines = file.read()
            file.close()

    def add_new_client(self, nam, account, qty_money):
        new_client = {}
        new_client_info = {}

        new_client_info.update({
            "Имя клиента": nam,
            "Сумма на счете, $": f'{qty_money}'
        })

        new_client.update({
            "Номер счета": account,
            "client_info": new_client_info
        })

        with open('bank.txt', 'a', encoding='utf-8') as file:
            file.write(str(new_client))
            file.write("\n")
            file.close()
        return


    def make_transaction(self):
        with open('bank.txt', 'r', encoding='utf-8') as file:
            self.lines = file.readlines()
            while True:
                try:
                    num_acc = int(input("Введите номер счета: "))
                    sum_transaction = int(input("Введите сумму перевода: "))
                    current_client = ast.literal_eval(self.lines[num_acc])
                    if int(current_client['client_info']['Сумма на счете, $']) < sum_transaction:
                        print(f"У {current_client['client_info']['Имя клиента']} не хватает суммы на счете")
                    else:
                        print(f"Операция выполнена! Остаток на счете у {current_client['client_info']['Имя клиента']}: {int(current_client['client_info']['Сумма на счете, $']) - sum_transaction}$")
                        print(self.lines[num_acc])
                        self.lines = self.lines.remove(self.lines[num_acc])
                    break
                except IndexError:
                    print("Нет клиента с таким номером счета")
                except ValueError:
                    print("Введите правильно сумму перевода")
            file.close()



file = Bank()
# file.add_new_client('Bob9', 11, 400)
file.make_transaction()
