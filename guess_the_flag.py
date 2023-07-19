import random
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

countries = [
     "Afghanistan",    "Albania",    "Algeria",    "Andorra",    "Angola",    "Antigua and Barbuda",    "Argentina",    "Armenia",    "Australia",    "Austria",    "Azerbaijan",    "Bahamas",    "Bahrain",    "Bangladesh",    "Barbados",    "Belarus",    "Belgium",    "Belize",    "Benin",    "Bhutan",    "Bolivia",    "Bosnia and Herzegovina",    "Botswana",    "Brazil",    "Brunei",    "Bulgaria",    "Burkina Faso",    "Burundi",    "Cabo Verde",    "Cambodia",    "Cameroon",    "Canada",    "Central African Republic",    "Chad",    "Chile",    "China",    "Colombia",    "Comoros",    "Congo",    "Costa Rica",    "Croatia",    "Cuba",    "Cyprus",    "Czech Republic",    "Denmark",    "Djibouti",    "Dominica",    "Dominican Republic",    "Ecuador",    "Egypt",    "El Salvador",    "Equatorial Guinea",    "Eritrea",    "Estonia",    "Eswatini",    "Ethiopia",    "Fiji",    "Finland",    "France",    "Gabon",    "Gambia",    "Georgia",    "Germany",    "Ghana",    "Greece",    "Grenada",    "Guatemala",    "Guinea",    "Guinea-Bissau",    "Guyana",    "Haiti",    "Honduras",    "Hungary",    "Iceland",    "India",    "Indonesia",    "Iran",    "Iraq",    "Ireland",    "Israel",    "Italy",    "Jamaica",    "Japan",    "Jordan",    "Kazakhstan",    "Kenya",    "Kiribati",    "Kuwait",    "Kyrgyzstan",    "Laos",    "Latvia",    "Lebanon",    "Lesotho",    "Liberia",    "Libya",    "Liechtenstein",    "Lithuania",    "Luxembourg",    "Madagascar",    "Malawi",    "Malaysia",    "Maldives",    "Mali",    "Malta",    "Marshall Islands",    "Mauritania",    "Mauritius",    "Mexico",    "Micronesia",    "Moldova",    "Monaco",    "Mongolia",    "Montenegro",    "Morocco",    "Mozambique",    "Myanmar",    "Namibia",    "Nauru",    "Nepal",    "Netherlands",    "New Zealand",    "Nicaragua",    "Niger",    "Nigeria",    "North Korea",    "North Macedonia",    "Norway",    "Oman",    "Pakistan",    "Palau",    "Palestine",    "Panama",    "Papua New Guinea",    "Paraguay",    "Peru",    "Philippines",    "Poland",    "Portugal",    "Qatar",    "Romania",    "Russia",    "Rwanda",    "Saint Kitts and Nevis",    "Saint Lucia",    "Saint Vincent and the Grenadines",    "Samoa",    "San Marino",    "Sao Tome and Principe",    "Saudi Arabia",    "Senegal",    "Serbia",    "Seychelles",    "Sierra Leone",    "Singapore",    "Slovakia",    "Slovenia",    "Solomon Islands",    "Somalia",    "South Africa",    "South Korea",    "South Sudan",    "Spain",    "Sri Lanka",    "Sudan",    "Suriname",    "Sweden",    "Switzerland",    "Syria",    "Taiwan",    "Tajikistan",    "Tanzania",    "Thailand",    "Timor-Leste",    "Togo",    "Tonga",    "Trinidad and Tobago",    "Tunisia",    "Turkey",    "Turkmenistan",    "Tuvalu",    "Uganda",    "Ukraine",    "United Arab Emirates",    "United Kingdom",    "United States",    "Uruguay",    "Uzbekistan",    "Vanuatu",    "Vatican City",    "Venezuela",    "Vietnam",    "Yemen",    "Zambia",    "Zimbabwe"
]

country_codes = {
     "Afghanistan": "AF",
    "Albania": "AL",
    "Algeria": "DZ",
    "Andorra": "AD",
    "Angola": "AO",
    "Antigua and Barbuda": "AG",
    "Argentina": "AR",
    "Armenia": "AM",
    "Australia": "AU",
    "Austria": "AT",
    "Azerbaijan": "AZ",
    "Bahamas": "BS",
    "Bahrain": "BH",
    "Bangladesh": "BD",
    "Barbados": "BB",
    "Belarus": "BY",
    "Belgium": "BE",
    "Belize": "BZ",
    "Benin": "BJ",
    "Bhutan": "BT",
    "Bolivia": "BO",
    "Bosnia and Herzegovina": "BA",
    "Botswana": "BW",
    "Brazil": "BR",
    "Brunei": "BN",
    "Bulgaria": "BG",
    "Burkina Faso": "BF",
    "Burundi": "BI",
    "Cabo Verde": "CV",
    "Cambodia": "KH",
    "Cameroon": "CM",
    "Canada": "CA",
    "Central African Republic": "CF",
    "Chad": "TD",
    "Chile": "CL",
    "China": "CN",
    "Colombia": "CO",
    "Comoros": "KM",
    "Congo": "CG",
    "Costa Rica": "CR",
    "Croatia": "HR",
    "Cuba": "CU",
    "Cyprus": "CY",
    "Czech Republic": "CZ",
    "Denmark": "DK",
    "Djibouti": "DJ",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Ecuador": "EC",
    "Egypt": "EG",
    "El Salvador": "SV",
    "Equatorial Guinea": "GQ",
    "Eritrea": "ER",
    "Estonia": "EE",
    "Eswatini": "SZ",
    "Ethiopia": "ET",
    "Fiji": "FJ",
    "Finland": "FI",
    "France": "FR",
    "Gabon": "GA",
    "Gambia": "GM",
    "Georgia": "GE",
    "Germany": "DE",
    "Ghana": "GH",
    "Greece": "GR",
    "Grenada": "GD",
    "Guatemala": "GT",
    "Guinea": "GN",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Haiti": "HT",
    "Honduras": "HN",
    "Hungary": "HU",
    "Iceland": "IS",
    "India": "IN",
    "Indonesia": "ID",
    "Iran": "IR",
    "Iraq": "IQ",
    "Ireland": "IE",
    "Israel": "IL",
    "Italy": "IT",
    "Jamaica": "JM",
    "Japan": "JP",
    "Jordan": "JO",
    "Kazakhstan": "KZ",
    "Kenya": "KE",
    "Kiribati": "KI",
    "Kuwait": "KW",
    "Kyrgyzstan": "KG",
    "Laos": "LA",
    "Latvia": "LV",
    "Lebanon": "LB",
    "Lesotho": "LS",
    "Liberia": "LR",
    "Libya": "LY",
    "Liechtenstein": "LI",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Malaysia": "MY",
    "Maldives": "MV",
    "Mali": "ML",
    "Malta": "MT",
    "Marshall Islands": "MH",
    "Mauritania": "MR",
    "Mauritius": "MU",
    "Mexico": "MX",
    "Micronesia": "FM",
    "Moldova": "MD",
    "Monaco": "MC",
    "Mongolia": "MN",
    "Montenegro": "ME",
    "Morocco": "MA",
    "Mozambique": "MZ",
    "Myanmar": "MM",
    "Namibia": "NA",
    "Nauru": "NR",
    "Nepal": "NP",
    "Netherlands": "NL",
    "New Zealand": "NZ",
    "Nicaragua": "NI",
    "Niger": "NE",
    "Nigeria": "NG",
    "North Korea": "KP",
    "North Macedonia": "MK",
    "Norway": "NO",
    "Oman": "OM",
    "Pakistan": "PK",
    "Palau": "PW",
    "Palestine": "PS",
    "Panama": "PA",
    "Papua New Guinea": "PG",
    "Paraguay": "PY",
    "Peru": "PE",
    "Philippines": "PH",
    "Poland": "PL",
    "Portugal": "PT",
    "Qatar": "QA",
    "Romania": "RO",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saint Kitts and Nevis": "KN",
    "Saint Lucia": "LC",
    "Saint Vincent and the Grenadines": "VC",
    "Samoa": "WS",
    "San Marino": "SM",
    "Sao Tome and Principe": "ST",
    "Saudi Arabia": "SA",
    "Senegal": "SN",
    "Serbia": "RS",
    "Seychelles": "SC",
    "Sierra Leone": "SL",
    "Singapore": "SG",
    "Slovakia": "SK",
    "Slovenia": "SI",
    "Solomon Islands": "SB",
    "Somalia": "SO",
    "South Africa": "ZA",
    "South Korea": "KR",
    "South Sudan": "SS",
    "Spain": "ES",
    "Sri Lanka": "LK",
    "Sudan": "SD",
    "Suriname": "SR",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Syria": "SY",
    "Taiwan": "TW",
    "Tajikistan": "TJ",
    "Tanzania": "TZ",
    "Thailand": "TH",
    "Timor-Leste": "TL",
    "Togo": "TG",
    "Tonga": "TO",
    "Trinidad and Tobago": "TT",
    "Tunisia": "TN",
    "Turkey": "TR",
    "Turkmenistan": "TM",
    "Tuvalu": "TV",
    "Uganda": "UG",
    "Ukraine": "UA",
    "United Arab Emirates": "AE",
    "United Kingdom": "GB",
    "United States": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vanuatu": "VU",
    "Vatican City": "VA",
    "Venezuela": "VE",
    "Vietnam": "VN",
    "Yemen": "YE",
    "Zambia": "ZM",
    "Zimbabwe": "ZW"
}

def display_flag(country):
    country_code = country_codes.get(country)
    flag_url = f"https://flagsapi.com/{country_code}/flat/64.png"

    response = requests.get(flag_url)
    if response.status_code == 200:
        flag_image = Image.open(BytesIO(response.content))
        flag_image = flag_image.resize((264, 264))  # Resize the image to desired dimensions
        flag_photo = ImageTk.PhotoImage(flag_image)

        flag_label.configure(image=flag_photo)
        flag_label.image = flag_photo
    else:
        print(f"Failed to fetch flag for {country}")

def check_answer():
    response = answer_entry.get().strip()
    if chosen_country == response:
        result_label.configure(text="WELL DONE!", fg="green")
    else:
        result_label.configure(text=f"Wrong answer, correct answer was: {chosen_country}", fg="red")

random_number = random.randint(0, len(countries)-1)
chosen_country = countries[random_number]

window = tk.Tk()
window.title("Guess the Flag")
window.geometry("400x400")

flag_label = tk.Label(window, width=264, height=264)
flag_label.pack(pady=20)

display_flag(chosen_country)

answer_entry = tk.Entry(window, width=30)
answer_entry.pack(pady=10)

check_button = tk.Button(window, text="Check", command=check_answer)
check_button.pack()

result_label = tk.Label(window, text="", fg="green")
result_label.pack(pady=10)

window.mainloop()



