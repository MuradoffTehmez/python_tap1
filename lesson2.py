import re

def alfabetik_sirala(ifade):
    sozler = re.findall(r'\w+', ifade)
    duzgun_sozler = [''.join(sorted(soz.lower())) for soz in sozler]
    duzgun_cumle = ' '.join(duzgun_sozler)
    return duzgun_cumle

istifadeci_ifadesi = input("İfadəni daxil edin: ")
netice = alfabetik_sirala(istifadeci_ifadesi)
print(f"Əlifba sırası ilə sıralanmış ifadə: {netice}")
