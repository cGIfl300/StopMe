import subprocess
import datetime
from pathlib import Path
from tinydb import TinyDB, Query


def get_available_time_for_today():
    # Get the available time left for today, return 0 if none
    current_time = datetime.datetime.now()
    record_date = f'{current_time.year}-{current_time.month}-{current_time.day}'
    DB_PATH = str(Path.home()) + "\\stopme.json"
    q = Query()

    print(DB_PATH)
    db = TinyDB(DB_PATH)
    r = db.search(q.date == record_date)
    print(r)
    if not r:
        db.insert({'date': record_date})
        return 20
    else:
        return 0
    pass


def logoff():
    # Logoff the computer
    result = subprocess.run("logoff")


def main_program():
    temps = get_available_time_for_today()
    print(temps)
    pass


if __name__ == '__main__':
    main_program()
