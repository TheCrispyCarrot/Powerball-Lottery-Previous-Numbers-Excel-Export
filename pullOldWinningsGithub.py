import requests
from bs4 import BeautifulSoup
import pandas as pd


def createSheet(year):
    #accesses the lottery website with your personal browser headers
    URL = 'https://www.lottery.net/powerball/numbers/' + year
    #headers can be found by typing 'What is my user agent' into your browser and copying the result
    headers = {"User-Agent": '''Insert your headers here!!!'''}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    balls = soup.find(class_="prizes archive").get_text().split()      #pulls all the winning numbers and the dates in text format and puts them into a list
    balls.remove('Result')                                             #removeing the first three words from the list of winning numbers that are irrelavant
    balls.remove('Date')
    balls.remove('Numbers')

    #creating a dictionary of winning attributes
    oldWinDictionary = { "weekday"  : balls[0::11],
                         "month"    : balls[1::11],
                         "day"      : balls[2::11],
                         "year"     : balls[3::11],
                         "ball_1"   : balls[4::11],
                         "ball_2"   : balls[5::11],
                         "ball_3"   : balls[6::11],
                         "ball_4"   : balls[7::11],
                         "ball_5"   : balls[8::11],
                         "powerBall": balls[9::11],
                         "powerPlay": balls[10::11]
                         }
    #exports the winning numbers as an excel spreadsheet
    dataFrame = pd.DataFrame(data=oldWinDictionary)
    print(dataFrame)
    writer = pd.ExcelWriter(year + "winningNumbers.xlsx")
    dataFrame.to_excel(writer, year)
    writer.save()

    #notifies you that the spreadsheet has been saved and the code funcioned properly
    print(year + " spreadsheet has been saved")

#uses the function to make a spreadsheet of all the winning numbers in 2019
createSheet(2019)