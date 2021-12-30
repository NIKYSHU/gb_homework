import datetime as dt

import requests

reply_dict = {}

def xml_reply_replaces(input_line=""):
    processing_text = input_line.replace("<ValCurs Date=", "")
    processing_text = processing_text.replace('<?xml version="1.0" encoding="windows-1251"?>', "")
    processing_text = processing_text.replace('" name="Foreign Currency Market">', "")
    processing_text = processing_text.replace("<Valute ID=", "#")
    processing_text = processing_text.replace("</Valute>", "")
    processing_text = processing_text.replace("><NumCode>", "--")
    processing_text = processing_text.replace("</NumCode><CharCode>", "--")
    processing_text = processing_text.replace("</CharCode><Nominal>", "--")
    processing_text = processing_text.replace("</Nominal><Name>", "--")
    processing_text = processing_text.replace("</Name><Value>", "--")
    processing_text = processing_text.replace("</Value>", "")
    processing_text = processing_text.replace("</ValCurs>", "")
    processing_text = processing_text.replace('"', "")

    dict_date = dt.datetime.strptime(processing_text.split("#")[0], "%d.%m.%Y").date()

    reply_dict["timestamp"] = dict_date
    reply_dict["last_update_dts"] = dt.datetime.now()

    for current_pair in processing_text.split("#"):

        line = current_pair.split("--")
        if len(line) > 1:

            if line[2].lower() not in reply_dict.keys():
                reply_dict[line[2].lower()] = float(line[5].replace(",", ".")) / float(line[3].replace(",", "."))
    return reply_dict


def currency_rates(currency="USD"):

    if reply_dict.get('last_update_dts', 0) == 0:
        response = xml_reply_replaces(requests.get("http://www.cbr.ru/scripts/XML_daily.asp", "").text)
    else:
        response = reply_dict

    reply = {'timestamp': response.get("timestamp", "None"), currency: response.get(currency.lower(), "None")}
    return reply



currency_array = ['uSd', 'eur', "AuD"]
for el in currency_array:

    data_info = currency_rates(el)

    print(f'Валюта {el.upper()}, курс = {data_info.get(el)} на дату: {data_info.get("timestamp")}')