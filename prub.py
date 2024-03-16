from datetime import date, datetime
today = date.today()
ahora = datetime.now()
print(f"Hora actual: {ahora.strftime('%H:%M')}")