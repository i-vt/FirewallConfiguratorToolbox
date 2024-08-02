import socketserver
from dnslib import DNSRecord, DNSHeader, RR, A, QTYPE, RCODE

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        request = DNSRecord.parse(data)
        print(f"Received DNS request: {request.q.qname}")
        reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
        qname = str(request.q.qname)
        qtype = QTYPE[request.q.qtype]
        if qtype == 'A':
            if qname == "example.com.":
                reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.0.2.1")))
            elif qname == "test.com.":
                reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.0.2.2")))
            else:
                reply.header.rcode = RCODE.NXDOMAIN
        else:
            reply.header.rcode = RCODE.NXDOMAIN
        socket.sendto(reply.pack(), self.client_address)
        print(f"Sent DNS response: {reply}")

if __name__ == "__main__":
    server = socketserver.UDPServer(("localhost", 53), DNSHandler)
    print("DNS server started on localhost:53")
    server.serve_forever()
# Probably should use iNetSim - as it is easier and has more features.
