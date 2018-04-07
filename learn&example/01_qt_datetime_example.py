#reference and further details
#http://zetcode.com/gui/pyqt5/datetime/

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

#date
date = QDate.currentDate()
xmas = QDate(2018, 12, 24)
print( date.toString(                       Qt.ISODate))                 #2018-03-27
print( date.toString(                       Qt.DefaultLocaleLongDate))   #March 27, 2561 BE
print("Days in month: {0}".format(          date.daysInMonth()))
print("Days in year: {0}".format(           date.daysInYear()))
print("Days diff until X-Mas: {0}".format(  date.daysTo(xmas)))
print()

#datetime
datetime = QDateTime.currentDateTime()
print(datetime.toString())                      #Tue Mar 27 09:52:31 2018
print("The offset from UTC is: {0} seconds".format(datetime.offsetFromUtc()))   #The offset from UTC is: 25200 seconds
print()

#time
time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))  #9:52:31 AM GMT+7
print()
