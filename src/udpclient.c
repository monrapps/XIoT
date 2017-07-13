/*
 * udpclient.c
 *
 * OS: FreeBSD
 * compiler: cc
 *      To compile: cc -o udpclient -g udpclient.c
 *
 * Protocol Independant (working for both IPV4 and IPV6)
 *
 * udpclient assumes udpserver.c is running first.
 * It sends 'count' packets to the server which in turn writes
 * them back to the client; i.e., the server provides an echo service.
 *
 * To run:
 *      1. first run udpserver on some udp port that is not used.
 *      (you can make sure ports are not used with %netstat -a | grep udp)
 *
 *      % udpserver 10000&
 *
 *      2. then run the client
 *
 *      %udpclient localhost 10000 512
 *      %udpclient mchugh.cs.pdx.edu 10000 512
 *      %udpclient 131.252.215.20 10000 512
 *      %udpclient 2001:468:1f04:2f0:250:daff:fe83:d48c 10000 512
 *
 * syntax:
 *      % udpclient remote_host udp_port number_of_packets_to_echo
 *
 */


#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <sys/time.h>
#include <errno.h>

extern int errno;

#define ACK 'z'

#define BUFSIZE	1024

int main (int argc, char **argv){
  
  int sockfd, n, rc;
  socklen_t salen;
  struct sockaddr *sa;
  struct addrinfo hints, *res, *ressave;
  char *host, *port, *count;
  int i;
  struct msgbuf {
		long count;      /* current buffer count 0..n */
		char buf[BUFSIZE];
  } mbuf;
  int fromlen;
  int ackvar;
  int nonacks,acks;

  nonacks=0;
  acks=0;
 
  if(argc != 4)
   { printf("usage: tcpclient <hostname/IPaddress> <portnumber> <count> \n");
     exit(0);
   }

  host=argv[1];
  port=argv[2];
  count=atoi(argv[3]);
 
  /*initilize addrinfo structure*/
  bzero(&hints, sizeof(struct addrinfo));  
  hints.ai_family=AF_UNSPEC;
  hints.ai_socktype=SOCK_DGRAM;
  hints.ai_protocol=IPPROTO_UDP;

  if((n=getaddrinfo(host, port, &hints, &res)) != 0)
    printf("udpclient error for %s, %s: %s", host, port, gai_strerror(n));
  ressave=res;

  do{/* each of the returned IP address is tried*/
    sockfd=socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if(sockfd>= 0)
      break; /*success*/
  }while ((res=res->ai_next) != NULL);

  sa=malloc(res->ai_addrlen);
  memcpy(sa, res->ai_addr, res->ai_addrlen);
  salen=res->ai_addrlen;

  freeaddrinfo(ressave);
 
  fillBuf(mbuf.buf, BUFSIZE);

  for ( i = 0; i < count; i++) {

   printf("client msg no [%d]\n", i);

   mbuf.count = i;

   /* write msg to remote system
   * sock
   * buf
   * sizeof (union msg)
   * 0,
   * client
   * sizeof (client)
   */
   if( rc = sendto(sockfd,&mbuf,sizeof (struct msgbuf),0,sa, salen) <0 ) {
	/* buffers aren't available locally at the moment,
	 * try again.
	 */
	if (errno == ENOBUFS)
		continue;
	perror("sending datagram");
	exit(1);
   }


   /* read acknowledgement from remote system
   */
   if (recvfrom(sockfd, &ackvar, sizeof(long), 0, NULL, NULL) < 0 ) {
	printf("server error: errno %d\n",errno);
	perror("reading datagram");
	exit(1);
   }

   if ( ackvar == ACK)
        acks++;
   else
        nonacks++;

 }/*end of for */ 
  printf("udpclient: count sent %d\n", count);
  printf("udpclient: acks %d nonacks %d\n",acks,nonacks);
  close(sockfd);
  return(0);

}

static char bufval =  'a';

/*
 * fill buffer with a character value
 *
 * Successive calls fill buffer with next character a-z...
 */

fillBuf(buf,size)
register char *buf;
register int size;
{
	register int i;

	for ( i = 0; i < size; i++)
		*buf++ = bufval;
	bufval++;
}











