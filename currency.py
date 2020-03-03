from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    result = requests.get("https://www.cbr.ru/scripts/XML_daily.asp", {"date_req": date})
    soup = BeautifulSoup(result.content, 'xml')

    rate ={}

    for n in soup('Valute'):
        rate[n.CharCode.string]=(Decimal(n.Value.string.replace(',','.')),int(n.Nominal.string))

    rate['RUR'] = (Decimal(1), 1)
 
    result = amount * rate[cur_from][0] * rate[cur_to][1] / rate[cur_from][1] / rate[cur_to][0]
    return result.quantize(Decimal('.0001'))
