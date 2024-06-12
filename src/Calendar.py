from datetime import datetime
import icalendar
import uuid
import subprocess
import os
import tempfile
import time
cal = icalendar.Calendar()
cal.add('prodid', '-//Mi Calendario//mxm.dk//')
cal.add('version', '2.0')
evento = icalendar.Event()
def CreateEvent(summary,dtstart,dtend):
    """CreateEvent method \n
    Open your default calendar app creating a new event.

    Args:
        summary: Title of the event
        dtstart: Event start Datetime.
        dtend: Event end Datetime.
    """
    evento.add('summary', summary)
    evento.add('dtstart', dtstart)  # Hora de inicio antes que la hora de fin
    evento.add('dtend', dtend)
    evento.add('dtstamp', datetime.now())
    evento['uid'] = str(uuid.uuid4())
    evento.add('priority', 5)
    cal.add_component(evento)
    with tempfile.NamedTemporaryFile(suffix='.ics', delete=False) as temp_file:
        temp_file.write(cal.to_ical())
        temp_file_name = temp_file.name
    if os.name == 'nt':
        subprocess.run(['start', temp_file_name], shell=True)
    else:
        subprocess.run(['xdg-open', temp_file_name])
