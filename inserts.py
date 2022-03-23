def insertEquipment(eq):
    return f"INSERT INTO equipments (name, brandName, size, isRental, isOnShelf, price, inStock) VALUES (" + "'" + eq.name + "', '" + eq.brandName + "', '" + str(
        eq.size) + "', " + str(eq.isRental) + ", " + str(eq.isOnShelf) + ", " + str(eq.price) + ", " + str(
        eq.inStock) + ");"


def insertCashier(ca):
    return f"INSERT INTO cashiers (pesel, name, surname, dateOfEmployment) VALUES ('{ca.pesel}', " + "'" + str(
        ca.name) + "', '" + str(ca.surname) + "', '" + str(ca.dateOfEmployment) + "');"


def insertBill(bill):
    return f"INSERT INTO bills (cashierID, amount, paymentDatetime) VALUES ({bill.cashierID}, {bill.amount}, " + "'" + str(
        bill.paymentDatetime) + "');"


def insertEquipmentBill(equipmentbill):
    return f"INSERT INTO equipmentsbills (billNumber, equipmentID, amountPaid) VALUES ({equipmentbill.billNumber}, {equipmentbill.equipmentID}, {equipmentbill.amountPaid});"


def insertRental(rt):
    return f"INSERT INTO rental (name, surname, billNumber, isReturned) VALUES ('{rt.name}', '{rt.surname}', {str(rt.billNumber)}, {str(rt.isReturned)});"


def insertSpecificRental(specificrental):
    return f"INSERT INTO specificrentals (rentalID, equipmentID, startDatetime, plannedEndDatetime, actualEndDatetime, moneyOwed) VALUES ({specificrental.rentalID}, {specificrental.equipmentID}, " + "'" + \
           str(specificrental.startDatetime).replace("T", " ").split(".")[0] + "', '" + \
           str(specificrental.plannedEndDatetime).replace("T", " ").split(".")[0] + "', '" + \
           str(specificrental.actualEndDatetime).replace("T", " ").split(".")[0] + "', " + str(
        specificrental.moneyOwed) + ");"