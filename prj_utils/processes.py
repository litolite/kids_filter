import psutil


class Process:
    def __init__(self):
        self.args = ['name', 'username']
        self.procs = [p.info for p in psutil.process_iter(attrs=self.args) if p.info['username'] is not None]
        self.proc_by_name = None

    def get_procs(self):
        return self.procs

    def get_unique_procs(self):
        new_set = set()
        new_procs = []
        for proc in self.procs:
            t = tuple(proc.items())
            if t not in new_set:
                new_set.add(t)
                new_procs.append(proc)
        return new_procs

    def find_procs_by_name(self, name):
        self.proc_by_name = [proc for proc in self.procs if proc['name'] == name]
        return self.proc_by_name

    def kill_proc(self, name):
        pass
