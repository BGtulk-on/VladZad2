Задачи за самостоятелна работа
Задача 1: Животни
Създай йерархия от класове за различни видове животни:

Родителски клас Animal с метод speak().
Child класове Dog, Cat, Bird, които наследяват Animal и предефинират метода speak().
Добави метод eat(), който да е общ за всички животни.
Примерен изход:

Buddy barks.
Whiskers meows.
Tweety chirps.
Buddy is eating.
Задача 2: Геометрични фигури
Създай класове за геометрични фигури:

Родителски клас Shape с метод area().
Детелни класове Circle, Rectangle, Triangle, които наследяват Shape и имплементират метода area().
Добави метод perimeter() за всяка фигура.
Примерен изход:

Area of Circle: 78.54
Perimeter of Circle: 31.42
Area of Rectangle: 20
Perimeter of Rectangle: 18
Задача 3: Транспортни средства
Създай йерархия за транспортни средства:

Родителски клас Vehicle с атрибути brand и year и метод start().
Детелни класове Car, Bicycle, Motorcycle, които наследяват Vehicle и добавят специфични методи (напр. drive() за колата и pedal() за велосипеда).
Добави метод stop(), който да е общ за всички транспортни средства.
Примерен изход:

Toyota (2020) is starting.
Toyota is driving.
Bicycle is pedaling.
Toyota is stopping.
Задача 4: Служители в компания
Създай класове за служители в компания:

Родителски клас Employee с атрибути name, salary и метод work().
Детелни класове Manager, Developer, Intern, които наследяват Employee и предефинират метода work().
Добави метод take_break(), който да е общ за всички служители.
Примерен изход:

John (Manager) is managing the team.
John is taking a break.
Alice (Developer) is writing code.
Bob (Intern) is learning.
Задача 5: Банкови сметки
Създай класове за банкови сметки:

Родителски клас BankAccount с атрибути account_number и balance и методи deposit() и withdraw().
Детелни класове SavingsAccount и CheckingAccount, които наследяват BankAccount.
SavingsAccount трябва да има метод add_interest(), който добавя лихва към баланса.
CheckingAccount трябва да има метод deduct_fees(), който удържа такси от баланса.
Savings Account (12345) balance: 1050.0
Checking Account (67890) balance: 900.0
Бонус задача: Множествено наследяване
Създай класове, които използват множествено наследяване:

Родителски класове ElectricAppliance и SmartDevice.
Детелен клас SmartTV, който наследява и двата класа.
Добави методи turn_on() и connect_to_wifi().
Примерен изход:

SmartTV is turning on.
SmartTV is connecting to Wi-Fi.
