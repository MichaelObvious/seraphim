from sys import argv
from datetime import date, timedelta
from merger import merge_bible_citations
from liturgical_calendar import LiturgicalCalendars
from pathlib import Path

cals = LiturgicalCalendars()

YEAR = date.today().year
if len(argv) > 1:
    try:
        YEAR = int(argv[1])
    except:
        pass

START_DATE = date(YEAR, 1, 1)
END_DATE = date(YEAR+1, 1, 1)


def day_title(d: date, sd: date) -> str:
    day_name = cals.get_day_name(d)
    color = cals.get_day_color(d)
    return f"""
<h1 style="color: {color}">{day_name}</h1>
"""


def morning(d: date, sd: date) -> str:
    # gospel = merge_bible_citations(get_gospel_of_day(d, sd, True))
    return f"""
<p>Padre nostro</p>
<p>Ave, o Maria</p>
<p>Credo</p>

<p>[GOSPEL]</p>
"""


def midday(d: date, sd: date) -> str:
    return f"""
<p>Padre nostro</p>
<p>Ave, o Maria</p>
<p>Credo</p>

<p>[APOSTLE]</p>
"""

def evening(d: date, sd: date) -> str:
    return f"""
<p>Padre nostro</p>
<p>Ave, o Maria</p>
<p>Credo</p>

<p>[GOSPEL]</p>
"""

def holy_hour(d: date, sd: date) -> str:
    return "<p>Holy Hour</p>"

from pathlib import Path

def dump_to(path: str, content: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

curr_date = START_DATE
while curr_date < END_DATE:
    dump_to(f"./pages/titles/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-title.html", day_title(curr_date, START_DATE))
    dump_to(f"./pages/daytime/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-morning.html", morning(curr_date, START_DATE))
    dump_to(f"./pages/daytime/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-midday.html", morning(curr_date, START_DATE))
    dump_to(f"./pages/daytime/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-evening.html", morning(curr_date, START_DATE))
    if cals.is_feast(curr_date):
        dump_to(f"./pages/holy_hours/{curr_date.year}_{curr_date.month:02}_{curr_date.day:02}-holy_hour.html", holy_hour(curr_date, START_DATE))

    curr_date += timedelta(1)
