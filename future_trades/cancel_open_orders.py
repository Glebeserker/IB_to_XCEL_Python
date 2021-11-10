from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading
import time

class CancelOrder(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        
    def cancel(self):
        self.reqGlobalCancel()
        
def run_loop():
    app.run()
    
app = CancelOrder()
app.connect('127.0.0.1', 7497, 123)

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(3)

app.cancel()

app.disconnect()
