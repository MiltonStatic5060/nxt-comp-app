import inputs
import thread

#g1 = inputs.DeviceManager().gamepads[0]
#g2 = inputs.DeviceManager().gamepads[1]

def update(g):
    while 1:
        events = g.read()
        for event in events:
            print(event.code,event.state)
for g in inputs.DeviceManager().gamepads:
    thread.start_new_thread(update,(g, ))
#thread.start_new_thread(update,(g1, ))
#thread.start_new_thread(update,(g2, ))

while 1:
    pass
