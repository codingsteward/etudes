# Redis notes

Put down a list of stuff that I'll find useful and need to learn

1. TCP
2. ...

Transmission Control Protocol (TCP)
1. Guarantee 1: Reliable delivery
    - Asking receiver to acknowledge all packets, retransmitting if acknowledgement isn't received
2. Guarantee 2: In-order delivery of packets
    - Label each packet with a sequence number. Receiver tracks and reorder packet by sequence number
3. TCP is a connection-oriented protocol, must establish a connection first between server and client
4. TCP handshake
    - Client initiates connection by sending SYN packet
    - Server acknowledges by sending SYN-ACK packet 
    - Client acknowledges server's packet by sending ACK packet. The connection is established when server receives this.

Web server socket

1. https://www.youtube.com/watch?v=1HF-UAGcuvs (python)
2. https://www.youtube.com/watch?v=4IMc3CaMhyY (TCP)
3. https://docs.python.org/3/howto/sockets.html#socket-howto
4. https://pymotw.com/2/SocketServer/index.html#module-SocketServer 


HTTP
1. https://www.jmarshall.com/easy/http/#sample

Berkeley Software Distribution (BSD) sockets

Main APIs

1. socket() => creates a new socket 
2. bind() => used on server side, associate socket with address e.g local IP and port #
3. listen() => used on server side, causes a bound TCP socket to enter listening state
4. accept() => used on server side, accepts incoming connection to create a new TCP connection from remote client, creates a new socket associated with the new address on the other side
5. send(), recv() => send/receive data
6. connect() => used on client side, assigns a free local port on socket and attempts a TCP connection
7. close() => release resources, close connection


