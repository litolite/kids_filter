import schedule
import time

from prj_utils.db_session import session as Session
from prj_utils.processes import Process as Proc
from models import Process


def update_processes_table():
    sess = Session()
    proc = Proc()
    procs = proc.get_unique_procs()
    new_procs = []
    for item in procs:
        proc = sess.query(Process).filter(Process.username == item['username'] and Process.name == item['name']).count()
        if proc == 0:
            new_procs.append(item)
    if not new_procs:
        print("No new processes!")
    else:
        sess.bulk_insert_mappings(Process, new_procs)
        sess.commit()
        print("Done!")


schedule.every(5).minutes.do(update_processes_table)
while True:
    schedule.run_pending()
    time.sleep(1)
