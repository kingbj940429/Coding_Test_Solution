''' 1340번 연도 진행바 '''

def yunYearCheck(year):
    if((year%400 == 0 or year%4 == 0) and year%100 != 0):
        return True
    else:
        return False


if __name__ == "__main__":
    #January, February, March, April, May, June, July, August, September, October, November, December
    month_dic = {"January" : "1", "February" : "2", "March" : "3", "April" : "4",
    "May" : "5", "June" : "6", "July" : "7", "August" : "8",
    "September" : "9", "October" : "10", "November" : "11", "December" : "12"}

    day_dic = {"1" : "31", "2" : "28", "3" : "31", "4" : "30",
    "5" : "31", "6" : "30", "7" : "31", "8" : "31",
    "9" : "30", "10" : "31", "11" : "30", "12" : "31"}

    input_data = input().split(" ")
    
    #기본 변수 세팅    
    year = int(input_data[2])
    month = int(month_dic.get(input_data[0]))
    day = int(input_data[1].replace(",",""))
    time = input_data[3].split(":")
    hour = int(time[0])
    minute = int(time[1])
    
    #윤년이면
    if(yunYearCheck(year) == True):
        day_dic["2"] = "29"

    basic_total_minute = 365 * 24 * 60#1년을 분으로 했을 경우

    sum_day = 0

    for i in range(1, month):
        sum_day += int(day_dic.get(str(i)))
    
    sum_day += day#월 일의 합
    #print(sum_day)
    sum_minute = sum_day * 24 * 60 + hour*60 + minute#월 일의 합은 분으로 통합
    #print(sum_minute)
    print(sum_minute/basic_total_minute * 100)
    
        


