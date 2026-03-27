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
<p>Nel nome del Padre, del Figlio e dello Spirito Santo. Amen.</p>
<p>Padre nostro che sei nei cieli, sia santificato il tuo nome, venga il tuo regno, sia fatta la tua volontà come in cielo così in terra. Dacci oggi il nostro pane quotidiano, e rimetti a noi i nostri debiti come anche noi li rimettiamo ai nostri debitori, e non abbandonarci alla tentazione, ma liberaci dal male. Amen.</p>
<p>Ave, o Maria, piena di grazia, il Signore è con te. Tu sei benedetta fra le donne e benedetto è il frutto del tuo seno, Gesù. Santa Maria, Madre di Dio, prega per noi peccatori, adesso e nell'ora della nostra morte. Amen.</p>
<p>Credo in un solo Dio, Padre onnipotente, Creatore del cielo e della terra, di tutte le cose visibili e invisibili.<br/>
Credo in un solo Signore, Gesù Cristo, unigenito Figlio di Dio, nato dal Padre prima di tutti i secoli: Dio da Dio, Luce da Luce, Dio vero da Dio vero, generato, non creato, della stessa sostanza del Padre; per mezzo di lui tutte le cose sono state create. Per noi uomini e per la nostra salvezza discese dal cielo, e per opera dello Spirito Santo si è incarnato nel seno della Vergine Maria e si è fatto uomo. Fu crocifisso per noi sotto Ponzio Pilato, morì e fu sepolto. Il terzo giorno è risuscitato, secondo le Scritture, è salito al cielo, siede alla destra del Padre. E di nuovo verrà, nella gloria, per giudicare i vivi e i morti, e il suo regno non avrà fine.<br/>
Credo nello Spirito Santo, che è Signore e dà la vita, e procede dal Padre e dal Figlio. Con il Padre e il Figlio è adorato e glorificato, e ha parlato per mezzo dei profeti.<br/>
Credo la Chiesa, una santa cattolica e apostolica. Professo un solo Battesimo per il perdono dei peccati. Aspetto la risurrezione dei morti e la vita del mondo che verrà. Amen.</p>

<p>[APOSTLE]</p>

<p>Nel nome del Padre, del Figlio e dello Spirito Santo. Amen.</p>
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
    dump_to(f"./pages/daytime/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-midday.html", midday(curr_date, START_DATE))
    dump_to(f"./pages/daytime/{curr_date.year}/{curr_date.month:02}_{curr_date.day:02}-evening.html", evening(curr_date, START_DATE))
    if cals.is_feast(curr_date):
        dump_to(f"./pages/holy_hours/{curr_date.year}_{curr_date.month:02}_{curr_date.day:02}-holy_hour.html", holy_hour(curr_date, START_DATE))

    curr_date += timedelta(1)
