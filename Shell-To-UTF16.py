#!/usr/bin/python
import sys, socket
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

def convert_to_utf16(payload):
	enc_payload = ''
	for i in range(0, len(payload), 2):
		num = 0
		for j in range(0, 2):
			num += (ord(payload[i + j]) & 0xff) << (j * 8)
		enc_payload += '%%u%04x' % num
	return enc_payload

def main():
	buf = raw_input("Enter your hex coded shell (ex: \xx\xx): ")
	print("UTF-16 Encoded Payload:\n")
	print("---------------------------------------------------------------\n")
	print convert_to_utf16(buf)

if __name__ == '__main__':
	main()
