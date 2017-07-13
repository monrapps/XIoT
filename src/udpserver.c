/*
 * udpserver.c
 *
 * This is an example TCP/IP UDP socket server.
 * It will read packets sent to 'portno' and write them back
 * to the sender.  It has no reliability functions.
 * It will loop forever and must be killed in order to make
 * it terminate.
 *
 * Protocol independant( working for both IPV4 and IPV6)
 * syntax:
 *      % udpserver portno &
 *
 * Start the server first and then start the udpclient.c app to
 * send packets to it.  Use the debug switch with udpclient.c to
 * see if any of the packets disappear.  They won't disappear on
 * localhost, but they might go away if they are crossing a busy 
 * router.
 */
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/times.h>
#include <errno.h>
#include <signal.h>

#define ACK  'z'

#define MAXBUF	10 * 1024 


int main(int argc, char **argv)
{
  int sockfd;
  ssize_t m;
  int n;
  socklen_t addrlen, len;
  struct sockaddr *cliaddr;
  int port;
  struct addrinfo hints, *res, *ressave;
  char buf[MAXBUF];
  int current = 0;
  int ackvar = ACK;

 if(argc== 2){
   port=argv[1];
 }
 else
 {  printf("usage: udpserver <portnumber>\n");
    exit(0);
 }  
 /*initilize addrinfo structure*/ 
 bzero(&hints, sizeof(struct addrinfo));
 hints.ai_flags=AI_PASSIVE;
 hints. ai_family= AF_UNSPEC;
 hints. ai_socktype= SOCK_DGRAM;
 hints.ai_protocol=IPPROTO_UDP;

 if((n = getaddrinfo(NULL, port, &hints, &res)) !=0)
   printf("udpserver error for %s: %s",port,gai_strerror(n));

 ressave=res;

 do {/* each of the returned IP address is tried*/
    sockfd=socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if (sockfd<0)
      continue; /* fail, try next one*/
   
    if (bind(sockfd, res->ai_addr, res->ai_addrlen) == 0)
      break; /*success*/
    
    close(sockfd);

 }while( (res=res->ai_next)!= NULL); 
 
 if(&addrlen)
   addrlen=res->ai_addrlen;

 freeaddrinfo(ressave);

 cliaddr=malloc(addrlen);

 len=addrlen;
 
 for ( ;; ) {     /* do forever */
	int rc;

	if ((rc=recvfrom(sockfd, buf, MAXBUF, 0, cliaddr, &len)) < 0 ) {
		printf("server error: errno %d\n",errno);
		perror("reading datagram");
		exit(1);
	}

	printf("udpserver: got packet %d: ", current);

	if( sendto(sockfd,&ackvar,sizeof(long), 0,cliaddr,len  ) < 0 ) {
        	perror("sendto");
		if (errno == ENOBUFS)
			continue;
		exit(1);
	}
	current++;

}
/* can't get here, but just in case: close sockets
*/
close(sockfd);
return(0);

} 

