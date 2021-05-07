import requests
from datetime import datetime,timedelta

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

def find_vaccine(pin_code,time_gap=None):
    next_slot = datetime.now()
    default_date_gap = time_gap or f"{next_slot.day}-{next_slot.month}-{next_slot.year}"
    url = f"{base_url}?pincode={pin_code}&date={default_date_gap}"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    resp = requests.get(url,headers=headers).json()
    centers = resp.get('centers')
    print("*"*50)
    if not centers:
        print("No Vaccination center found near you.".ljust(50," "))
    else:
        print("Available vaccination center near you.".ljust(50," "))
        print("*"*50)
        for data in centers:
            print(f"Center id: {data['center_id']}           Center Name: {data['name']}")
            print(f"District: {data['district_name']}, Block Name: {data['block_name']}, Pin Code: {data['pincode']}")
            print(f"Timings from {data['from']} to {data['to']}")
            print(f" Free hai ya paise lenge? {data['fee_type']}")
            sessions = data['sessions']
            for session in sessions:
                print("="*20," Vaccine sessions slots","="*20)
                print(f"Slot date {session['date']} & Vaccine Name(if available): {session['vaccine']} ")
                print(f"Vaccine daily available capacity {session['available_capacity']} & Min Age Limit {session['min_age_limit']}")
                print(f"Daily working slots: ")
                for slot in session["slots"]:
                    print(slot)
            print("*"*50)


    print("*"*50)
    return resp


if __name__=="__main__":
    pin_code = int(input("Enter your pincode"))
    print("Enter you date in dd-mm-yyyy format. Slot within 7 days will be shown")
    date = str(input("Leave it empty if you want nearest.. just press enter"))
    find_vaccine(pin_code,date)

    