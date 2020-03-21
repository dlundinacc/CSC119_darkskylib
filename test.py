from darksky import forecast
from datetime import date, timedelta

# https://github.com/lukaskubis/darkskylib

CASTLEROCK = 39.3722, 104.8561

weekday = date.today()
with forecast('c8ccf8f10bba3e04957e088a67ced911', *CASTLEROCK) as CASTLEROCK:
    print(CASTLEROCK.daily.summary, end='\n---\n')
    for day in CASTLEROCK.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax
                   )
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
        weekday += timedelta(days=1)