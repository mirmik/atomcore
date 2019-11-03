import atomcore
import pycrow
import time

crowaddr = pycrow.compile_address(".12.127.0.0.1:10009") 
print(crowaddr)

def main():
	print("main")
	pycrow.diagnostic(True)
	pycrow.create_udpgate(12, 10020)
	pycrow.start_spin()
	pycrow.start_alive(addr=crowaddr, netname="testnode", resend_time=1000, dietime=4000, qos=0, ackquant=200)
	print("atomcore main")

	while(1):
		time.sleep(1)

	pycrow.finish_spin()
