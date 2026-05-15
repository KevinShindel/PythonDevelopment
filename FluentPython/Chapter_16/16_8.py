# семантика yield from
import collections
import queue

Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        for proc in sorted(self.procs.values()):
            first_event = next(proc)
            self.events.put(first_event)
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * ' ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def main():
    taxis = {
        0: taxi_process(ident=0, trips=2, start_time=0),
        1: taxi_process(ident=0, trips=2, start_time=0),
        2: taxi_process(ident=0, trips=2, start_time=0),
    }

    sim = Simulator(taxis)
