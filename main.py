import random
import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime

# Variables:
equipmentN = 1000
cashiersN = 50
chanceForQuestionnaire = 50  # in percents
rentalPriceS1 = [15, 5, 15, 10, 10]
rentalPriceS2 = [20, 6, 20, 10, 8]
rentalPriceS3 = [25, 7, 15, 12, 11]
biggestEquipmentPrice = 1500
minimumEquipmentPrice = 50
thunderProbability = 2  # procentowo
badWeatherProbability = 10  # procentowo
peopleFactor = 1  # Mnożnik ludzi - ~200k insertów overall to 1
maxEquipmentTransactionsPerPerson = 5

# ---
# Loading lists
# -----
period = pd.read_excel('Sezony_datyABC.xlsx')
# EQUIPMENTS
# Lists
equipmentName = ["Ski", "Ski Poles", "Ski Boots", "Ski Helmets", "Ski Goggles"]
brandName = ["4FRNT", "Black Crows", "Fischer", "Head", "Rossignol", "Salomon", "Slatnar", "Liberty Skis"]
size = ["XS", "S", "M", "L", "XL", "XXL"]
isRental = [0, 1]
isOnShelf = [0, 1]
price = range(minimumEquipmentPrice, biggestEquipmentPrice, 25)
inStock = range(0, 11)


# Class
class Equipment:
    def __init__(self, ID, season=1):
        whichName = random.randint(0, len(equipmentName) - 1)
        self.name = equipmentName[whichName]
        self.ID = ID
        if "Boots" in self.name:
            self.size = str(random.randint(30, 49))
        else:
            self.size = random.choice(size)
        self.brandName = random.choice(brandName)
        self.isRental = random.choice(isRental)
        self.isOnShelf = random.choice(isOnShelf)
        if self.isRental:
            if season == 1:
                self.price = rentalPriceS1[whichName]
            elif season == 2:
                self.price = rentalPriceS2[whichName]
            elif season == 3:
                self.price = rentalPriceS3[whichName]
            else:
                print("ERROOOOR")
        else:
            self.price = random.choice(price)
        self.inStock = random.choice(inStock)

    def setID(self, ID):
        self.ID = ID

    def __str__(self):
        return f"Equipment: {self.name}, {self.brandName}, {self.size}, {self.price} : {self.inStock} sztuk"


# CASHIERS
def pesel():
    year = random.randint(1970, 2004)
    if year <= 1999:
        month = random.randint(1, 12)
    elif year >= 2000:
        month = random.randint(1, 12) + 20
    odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    even_months = (4, 6, 9, 11, 24, 26, 29, 31)
    if month in odd_months:
        day = random.randint(1, 31)
    elif month in even_months:
        day = random.randint(1, 30)
    else:
        if year % 4 == 0 and year != 1900:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    four_random = random.randint(1000, 9999)
    four_random = str(four_random)
    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day
    a = y[0]
    a = int(a)
    b = y[1]
    b = int(b)
    c = m[0]
    c = int(c)
    d = m[1]
    d = int(d)
    e = dd[0]
    e = int(e)
    f = dd[1]
    f = int(f)
    g = four_random[0]
    g = int(g)
    h = four_random[1]
    h = int(h)
    i = four_random[2]
    i = int(i)
    j = four_random[3]
    j = int(j)
    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (check % 10)
    result = ""
    result += '%02d' % (year % 100)
    result += '%02d' % month
    result += '%02d' % day
    result += four_random
    return result


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


# Lists
cashierPesels = [pesel() for i in range(cashiersN)]
names = open("names.txt", "r").readlines()
random.shuffle(names)
surnames = open("surnames.txt", "r").readlines()
random.shuffle(surnames)
cashierNames = [i.strip() for i in names][:cashiersN]
cashierSurnames = [i.strip() for i in surnames][:cashiersN]
d1 = datetime.strptime('1/1/2016 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
datesOfEmployment = [random_date(d1, d2) for i in range(cashiersN)]


# Class
class Cashier:
    def __init__(self):
        self.pesel = pesel()
        self.name = cashierNames.pop()
        self.surname = cashierSurnames.pop()
        self.dateOfEmployment = datesOfEmployment.pop()


# BILLS
# Lists
billsCashierIDs = range(1, cashiersN)


# Class
class Bill:
    def __init__(self, amount, timestamp):
        self.cashierID = random.choice(billsCashierIDs)
        self.amount = amount
        self.paymentDatetime = timestamp


# EQUIPMENTSBILLS
# Class
class EquipmentsBills:
    def __init__(self, billNumber, equipmentID, amountPaid):
        self.billNumber = billNumber
        self.equipmentID = equipmentID
        self.amountPaid = amountPaid


# RENTAL
class Rental:
    def __init__(self, billNumber):
        self.name = names[random.choice(range(0, len(names)))][:-1]
        self.surname = surnames[random.choice(range(0, len(surnames)))][:-1]  # <3
        self.billNumber = billNumber
        self.isReturned = 1


# SPECIFIC RENTALS
class SpecificRental:
    def __init__(self, rentalID, equipmentID, startDatetime, plannedEndDatetime, actualEndDatetime, howManyMinutesLate):
        self.rentalID = rentalID
        self.equipmentID = equipmentID
        self.startDatetime = startDatetime
        self.plannedEndDatetime = plannedEndDatetime
        self.actualEndDatetime = actualEndDatetime
        self.moneyOwed = (howManyMinutesLate // 10) * 5

    def __str__(self):
        return f"EqID: {self.equipmentID} do RentalID: {self.rentalID}"


# QUESTIONNAIRE
# Lists
rating = range(1, 11)


def whichName(name):
    idx = 0
    for item in equipmentName:
        if item == name:
            return idx
        idx += 1
    return 0


# Class

class Questionnaire:
    def __init__(self, season, name, brandName, fulfillmentDate):
        if season == 1:
            self.fulfillmentDate = fulfillmentDate
            self.price = rentalPriceS1[whichName(name)]
        elif season == 2:
            self.fulfillmentDate = fulfillmentDate
            self.price = rentalPriceS2[whichName(name)]
        elif season == 3:
            self.fulfillmentDate = fulfillmentDate
            self.price = rentalPriceS3[whichName(name)]
        self.name = name
        self.brandName = brandName
        self.comfort = random.choice(rating)
        self.rentPrice = random.choice(rating)
        self.visage = random.choice(rating)
        self.overall = random.choice(rating)
        self.eqGeneralRating = 0.3 * self.comfort + 0.2 * self.rentPrice + 0.1 * self.visage + 0.4 * self.overall


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


resetThunders = open("wasthunderPeriod1.txt", "w").close()
resetThunders = open("wasthunderPeriod2.txt", "w").close()
resetInsert = open("insertsPeriod1.txt", "w").close()
resetInsert = open("insertsPeriod2.txt", "w").close()
p1thunders = open("wasthunderPeriod_tmp.txt", "w").close()
toInsert = open("insertsPeriod_tmp.txt", "w").close()
# reset excela dodać

# good bad thunder

equipmentsS1 = [Equipment(i, 1) for i in
                range(equipmentN)]  # pytanie jak z cenami i czy nie lepiej zrobic jedna tablice sprzetu po prostu
equipmentsS2 = [Equipment(i + equipmentN, 2) for i in range(equipmentN)]
equipmentsS3 = [Equipment(i + 2 * equipmentN, 3) for i in range(equipmentN)]


def main():
    p1thunders = open("wasthunderPeriod1.txt", "a")
    toInsert = open("insertsPeriod1.txt", "a")
    for i in range(equipmentN):
        toInsert.write(insertEquipment(equipmentsS1[i]) + '\n')
    for i in range(1, cashiersN):
        toInsert.write(insertCashier(Cashier()) + '\n')
    # Żeby mieć pusty dataframe
    questionnaireExcel = pd.DataFrame(columns=(
    'fulfillment_date', 'price', 'name', 'brand_name', 'comfort', 'rentPrice', 'visage', 'overall',
    'equipment_general_rating'))

    billID = 1  # Kolejne indeksy bill
    rentalID = 1  # Kolejne indeksy rentalID
    season = 1
    for day in period.values:
        print(day[0], period.values[-1][0])
        currentDay = day[0]
        if str(currentDay)[:10] == '2019-12-01':
            season = 2
        elif str(currentDay)[:10] == '2020-12-01':
            season = 3
            p1thunders = open("wasthunderPeriod_tmp.txt", "a")
            toInsert.close()
            toInsert = open("insertsPeriod_tmp.txt", "a")
            questionnaireExcel.to_excel('questionnairePeriod1.xlsx', index=False)
            questionnaireExcel = pd.DataFrame(columns=(
                'fulfillment_date', 'price', 'name', 'brand_name', 'comfort', 'rentPrice', 'visage', 'overall',
                'equipment_general_rating'))
        isThunder = random.randint(0, 100) > 100 - thunderProbability
        isBadWeather = isThunder or random.randint(0, 100) > 100 - badWeatherProbability
        isGoodWeather = not (isThunder or isBadWeather)
        p1thunders.write(str(currentDay) + " thunder: " + str(isThunder) + " isBadWeather: " + str(
            isBadWeather) + " wasGoodWeather: " + str(isGoodWeather) + "\n")

        if isThunder:
            nofp = random.randint(0, 8 * peopleFactor)
        elif isBadWeather:
            nofp = random.randint(40 * peopleFactor, 107 * peopleFactor)
        else:
            nofp = random.randint(120 * peopleFactor, 200 * peopleFactor)

        for i in range(nofp):
            howManyEquipments = random.randint(1, maxEquipmentTransactionsPerPerson)
            equipmentsToRent = []
            equipmentsToBuy = []
            shopAmount = 0
            rentAmount = 0
            for j in range(howManyEquipments):
                tempEq = random.choice(equipmentsS1)
                if tempEq.isOnShelf and tempEq.isRental:
                    # For renting
                    equipmentsToRent.append(tempEq)
                    rentAmount += tempEq.price
                elif not tempEq.isRental and tempEq.isOnShelf:
                    # For shop
                    equipmentsToBuy.append(tempEq)
                    shopAmount += tempEq.price
                else:
                    # In storage
                    pass
            # Tworzenie class dla sprzedaży
            if len(equipmentsToBuy) > 0:
                startDatetime = np.datetime64(
                    str(currentDay)[:-18] + str(random.randint(8, 18)).zfill(
                        2) + ":" +
                    str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ".000000000")
                timestamp = pd.Timestamp(startDatetime)
                bill = Bill(shopAmount, timestamp)
                toInsert.write(insertBill(bill) + '\n')
                for eq in equipmentsToBuy:
                    equipmentbill = EquipmentsBills(billID, eq.ID, eq.price)
                    toInsert.write(insertEquipmentBill(equipmentbill) + '\n')
                billID += 1

            # Tworzenie class dla wynajmu
            if len(equipmentsToRent) > 0:
                startDatetime = np.datetime64(
                    str(currentDay)[:-18] + str(random.randint(8, 18)).zfill(
                        2) + ":" +
                    str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ".000000000")
                timestamp = pd.Timestamp(startDatetime)
                bill = Bill(rentAmount, timestamp)
                toInsert.write(insertBill(bill) + '\n')
                rental = Rental(billID)
                toInsert.write(insertRental(rental) + '\n')
                # szansa ze wzial wszystko naraz:
                startDatetime = np.datetime64(
                    str(currentDay)[:-18] + str(random.randint(8, 18)).zfill(2) + ":" +
                    str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ".000000000")
                shouldRandomiseStart = random.randint(0, 100) > 10
                for eq in equipmentsToRent:
                    if shouldRandomiseStart:
                        startDatetime = np.datetime64(
                            str(currentDay)[:-18] + str(random.randint(8, 18)).zfill(2) + ":" +
                            str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(
                                2) + ".000000000")
                    equipmentbill = EquipmentsBills(billID, eq.ID, eq.price)
                    toInsert.write(insertEquipmentBill(equipmentbill) + '\n')
                    howManyMinutesLate = 0
                    timestamp = pd.Timestamp(startDatetime)
                    # do dwudziestej mozna max oddac
                    startHour = timestamp.hour
                    plannedEndHour = random.randint(startHour + 1, 20)
                    if plannedEndHour == 20:
                        plannedEndDatetime = np.datetime64(
                            str(startDatetime)[:-18] + str(plannedEndHour).zfill(2) + ":00:00.000000000")
                    else:
                        plannedEndDatetime = np.datetime64(
                            str(startDatetime)[:-18] + str(plannedEndHour).zfill(2) + ":" + str(
                                startDatetime)[14:])
                    if plannedEndHour != 20 and random.randint(0, 100) < 10:
                        howManyMinutesLate = random.choice(
                            range(10, (20 - pd.Timestamp(plannedEndDatetime).hour) * 60, 10))
                        actualEndDatetime = plannedEndDatetime + np.timedelta64(howManyMinutesLate, 'm')
                    else:
                        # is on time
                        actualEndDatetime = plannedEndDatetime

                    specificrental = SpecificRental(rentalID, eq.ID, startDatetime, plannedEndDatetime,
                                                    actualEndDatetime, howManyMinutesLate)
                    toInsert.write(insertSpecificRental(specificrental) + '\n')
                    if random.randint(0, 100) > (100 - chanceForQuestionnaire):
                        q = Questionnaire(season, eq.name, eq.brandName, actualEndDatetime)
                        qData = pd.DataFrame([[q.fulfillmentDate, q.price, q.name, q.brandName, q.comfort, q.rentPrice,
                                               q.visage, q.overall, q.eqGeneralRating]], columns=(
                        'fulfillment_date', 'price', 'name', 'brand_name', 'comfort', 'rentPrice', 'visage', 'overall',
                        'equipment_general_rating'))
                        questionnaireExcel = pd.concat([questionnaireExcel, qData])
                billID += 1
                rentalID += 1
    toInsert.close()
    print("Petla skonczona; zaczynam excele:")
    # Questionnaire zapis
    questionnaire1 = pd.read_excel('questionnairePeriod1.xlsx')
    questionnaireExcel = pd.concat([questionnaire1, questionnaireExcel])
    questionnaireExcel.to_excel(r'questionnairePeriod2.xlsx', index=False)

    p1thunders2 = open("wasthunderPeriod2.txt", "a")
    p1thunders1 = open("wasthunderPeriod1.txt", "r")
    p1thunders_tmp = open("wasthunderPeriod_tmp.txt", "r")

    toInsert1 = open("insertsPeriod1.txt", "r")
    toInsert2 = open("insertsPeriod2.txt", "a")
    toInsert_tmp = open("insertsPeriod_tmp.txt", "r")
    for row in p1thunders1:
        p1thunders2.write(row)
    for row in p1thunders_tmp:
        p1thunders2.write(row)

    for row in toInsert1:
        toInsert2.write(row)
    for row in toInsert_tmp:
        toInsert2.write(row)

    p1thunders1.close()
    p1thunders2.close()
    p1thunders_tmp.close()
    toInsert1.close()
    toInsert2.close()
    toInsert_tmp.close()


if __name__ == "__main__":
    main()
