import psutil


class Process:
    def __init__(self):
        self.args = ['name', 'username']
        self.procs = [p.info for p in psutil.process_iter(attrs=self.args)]
        self.proc_by_name = None

    def get_procs(self):
        return self.procs

    def find_procs_by_name(self, name):
        self.proc_by_name = [proc for proc in self.procs if proc['name'] == name]
        return self.proc_by_name

    def kill_proc(self, name):
        pass


prc = Process()
print(prc.get_procs())