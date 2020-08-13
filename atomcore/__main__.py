import atomcore
import pycrow
import time

import signal

crowaddr = pycrow.address(".12.127.0.0.1:10009") 
print(crowaddr)

def eee(a, b):
	pycrow.stop_spin()

def incoming_packet(pack):
	print(pack)

def undelivered_packet(pack):
	print(pack)

def main():
	signal.signal(signal.SIGINT, eee)

	print("main")
	pycrow.diagnostic(True)
	pycrow.create_udpgate(12, 10020)
	pycrow.start_spin()

	corenode = pycrow.libcrow.PyNode(incoming_packet, undelivered_packet)
	corenode.bind(12)

	#corenode = pycrow.create_node(
	#	incoming_handler = incoming_handler,
	#	undelivered_handler = undelivered_handler
	#)

	#corenode.bind(1)

	pycrow.join_spin()
