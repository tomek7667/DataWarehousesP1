import random
import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime
from inserts import *

# Variables:
equipmentN = 1000
equipmentN2 = 150
cashiersN = 50
chanceForQuestionnaire = 0  # in percents
chanceForNotTakingAllEquipment = 90 # 100 - always with himself
chanceForPriceChangeInPeriod2 = 30 #nie dotyczy rentali bo tam kazde sie zmienia
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
inStockP2 = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

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
        return f"Equipment: {self.name}, {self.brandName}, {self.size}, {self.price} : {self.inStock} sztuk | Availlability: {self.isOnShelf}"


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


resetThunders = open("P1_WAS_THUNDER.txt", "w").close()
resetThunders = open("P2_WAS_THUNDER.txt", "w").close()
resetInsert = open("P1_INSERTS.txt", "w").close()
resetInsert = open("P2_INSERTS.txt", "w").close()
thunders = open("TMP_thunder.txt", "w").close()
toInsert = open("TMP_in.txt", "w").close()
toInsertEq = open("TMP_eqP1.txt", "w").close()
toInsertEq = open("TMP_eqP2.txt", "w").close()
insertP1_withoutEq = open("TMP_p1.txt", "w").close()
# reset excela dodać

# good bad thunder

equipmentsS1 = [Equipment(i, 1) for i in range(1, equipmentN + 1)]
equipmentsS2 = [Equipment(i + equipmentN, 3) for i in range(1, equipmentN2 + 1)]
# equipmentsS3 = [Equipment(i + 2 * equipmentN2, 3) for i in range(1, equipmentN + 1)]


def main():
    thunders = open("P1_WAS_THUNDER.txt", "a")
    toInsert = open("TMP_p1.txt", "a")
    toInsertEq = open("TMP_eqP1.txt", "a")
    for i in range(equipmentN):
        toInsertEq.write(insertEquipment(equipmentsS1[i]) + '\n')
    toInsertEq.close()

    ########## ZMIANA CEN I ILOSCI EQUIPMENTU PO PERIODZIE 1 DLA P2

    equipmentsS1_P2 = equipmentsS1
    for i in range(len(equipmentsS1_P2)):
        if equipmentsS1_P2[i].isRental:
            equipmentsS1_P2[i].price = rentalPriceS3[whichName(equipmentsS1_P2[i].name)]
        elif random.randint(0, 100) > chanceForPriceChangeInPeriod2:
            equipmentsS1_P2[i].price = random.choice(price)

        equipmentsS1_P2[i].inStock = random.choice(inStockP2)
        if equipmentsS1_P2[i].inStock == 0:
            equipmentsS1_P2[i].isOnShelf = 0
        else:
            equipmentsS1_P2[i].isOnShelf = random.choice(isOnShelf)

    ##########

    equipmentsP2 = equipmentsS1_P2 + equipmentsS2

    toInsertEq = open("TMP_eqP2.txt", "a")
    for i in range(equipmentN + equipmentN2): #ilosc equipmentu z periodu1 + ten nowo wygenerowany na period2
        toInsertEq.write(insertEquipment(equipmentsP2[i]) + '\n')
    toInsertEq.close()
    for i in range(1, cashiersN):
        toInsert.write(insertCashier(Cashier()) + '\n')
    # Żeby mieć pusty dataframe
    questionnaireExcel = pd.DataFrame(columns=(
    'fulfillment_date', 'price', 'name', 'brand_name', 'comfort', 'rentPrice', 'visage', 'overall',
    'equipment_general_rating'))

    billID = 1  # Kolejne indeksy bill
    rentalID = 1  # Kolejne indeksy rentalID
    season = 1
    equipmentsS = equipmentsS1 #bierzemy najpierw eq na period1 potem w warunku zmieni sie na ten zmergowany
    for day in period.values:
        print(day[0], period.values[-1][0])
        currentDay = day[0]
        if str(currentDay)[:10] == '2019-12-01':
            season = 2
        elif str(currentDay)[:10] == '2020-12-01':
            season = 3
            equipmentsS = equipmentsP2 #Period2
            thunders.close()
            thunders = open("TMP_thunder.txt", "a")
            toInsert.close()
            toInsert = open("TMP_in.txt", "a")
            questionnaireExcel.to_excel('questionnairePeriod1.xlsx', index=False)
            questionnaireExcel = pd.DataFrame(columns=(
                'fulfillment_date', 'price', 'name', 'brand_name', 'comfort', 'rentPrice', 'visage', 'overall',
                'equipment_general_rating'))
        isThunder = random.randint(0, 100) > 100 - thunderProbability
        isBadWeather = isThunder or random.randint(0, 100) > 100 - badWeatherProbability
        isGoodWeather = not (isThunder or isBadWeather)
        thunders.write(str(currentDay) + " thunder: " + str(isThunder) + " isBadWeather: " + str(
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
                tempEq = random.choice(equipmentsS)
                if tempEq.isOnShelf == 1 and tempEq.isRental == 1:
                    # For renting
                    equipmentsToRent.append(tempEq)
                    rentAmount += tempEq.price
                elif tempEq.isOnShelf == 1 and tempEq.isRental == 0:
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
                timestamp = pd.Timestamp(startDatetime)
                startHour = timestamp.hour
                plannedEndHour = random.randint(startHour + 1, 20)
                shouldRandomiseStart = random.randint(0, 100) > chanceForNotTakingAllEquipment
                for eq in equipmentsToRent:
                    if shouldRandomiseStart:
                        startDatetime = np.datetime64(
                            str(currentDay)[:-18] + str(random.randint(8, 18)).zfill(2) + ":" +
                            str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(
                                2) + ".000000000")
                        timestamp = pd.Timestamp(startDatetime)
                        # do dwudziestej mozna max oddac
                        startHour = timestamp.hour
                        plannedEndHour = random.randint(startHour + 1, 20)
                    equipmentbill = EquipmentsBills(billID, eq.ID, eq.price)
                    toInsert.write(insertEquipmentBill(equipmentbill) + '\n')
                    howManyMinutesLate = 0
                    if plannedEndHour == 20:
                        plannedEndDatetime = np.datetime64(
                            str(startDatetime)[:-18] + str(plannedEndHour).zfill(2) + ":00:00.000000000")
                    else:
                        plannedEndDatetime = np.datetime64(
                            str(startDatetime)[:-18] + str(plannedEndHour).zfill(2) + ":" + str(
                                startDatetime)[14:])
                    if not shouldRandomiseStart and plannedEndHour != 20 and random.randint(0, 100) < 10:
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

    print("Petla skonczona; zaczynam excele:")
    # Questionnaire zapis
    questionnaire1 = pd.read_excel('questionnairePeriod1.xlsx')
    questionnaireExcel = pd.concat([questionnaire1, questionnaireExcel])
    questionnaireExcel.to_excel(r'questionnairePeriod2.xlsx', index=False)

    thunders.close()
    toInsert.close()

    thunders1 = open("P1_WAS_THUNDER.txt", "r")
    thunders2 = open("P2_WAS_THUNDER.txt", "a")
    thunders_tmp = open("TMP_thunder.txt", "r")

    toInsert1 = open("P1_INSERTS.txt", "a")
    toInsert2 = open("P2_INSERTS.txt", "a")
    insertP1_withoutEq = open("TMP_p1.txt", "r")
    toInsert_tmp = open("TMP_in.txt", "r")

    toInsertEquipment1 = open("TMP_eqP1.txt", "r")
    toInsertEquipment2 = open("TMP_eqP2.txt", "r")

    for row in thunders1:
        thunders2.write(row)
    for row in thunders_tmp:
        thunders2.write(row)

    for row in toInsertEquipment1:
        toInsert1.write(row)
    for row in toInsertEquipment2:
        toInsert2.write(row)
    for row in insertP1_withoutEq:
        toInsert1.write(row)
        toInsert2.write(row)
    for row in toInsert_tmp:
        toInsert2.write(row)

    thunders1.close()
    thunders2.close()
    thunders_tmp.close()
    toInsert1.close()
    toInsert2.close()
    toInsert_tmp.close()
    toInsertEquipment1.close()
    toInsertEquipment2.close()
    insertP1_withoutEq.close()


if __name__ == "__main__":
    main()
