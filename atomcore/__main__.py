import atomcore
import pycrow
import time

import threading
import signal

import time
import os

ATOMCORE_NODE = None
CANCEL_TOKEN = False
atomaddr = pycrow.address(".12.127.0.0.1:10015") 

def eee(a, b):
	global CANCEL_TOKEN
	pycrow.stop_spin()
	CANCEL_TOKEN = True

def incoming_packet(pack):
	msg = pack.message().decode('utf-8').strip()
	print(msg)
	if msg == "shutdown":
		print("shutdown")	
		os.system("shutdown 0")

def undelivered_packet(pack):
	print(pack)

def pulse_thread_function():
	while True:
		if CANCEL_TOKEN:
			return

		ATOMCORE_NODE.send(1, atomaddr, "alive", 0, 200)

		time.sleep(0.5)


def main():
	global ATOMCORE_NODE
	signal.signal(signal.SIGINT, eee)

	#pycrow.diagnostic(True)
	pycrow.create_udpgate(12, 10020)
	pycrow.start_spin()

	corenode = pycrow.libcrow.PyNode(incoming_packet, undelivered_packet)
	corenode.bind(12)

	ATOMCORE_NODE = corenode

	thr = threading.Thread(target=pulse_thread_function)
	thr.start()

	pycrow.join_spin()
