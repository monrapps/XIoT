#include <stdio.h>
#include "Xsocket.h"

// This is a workaround to get the localdag using C api since SWIG api is broken
int main(){
	// Get localdag 
	char dag[200], fid[100];
	int sock = Xsocket(AF_XIA, SOCK_STREAM, 0);	
	XreadLocalHostAddr(sock, dag, 200, fid, 100);
	
	// Save localdag in a file
	FILE *fp = fopen("./localdag","w");
	fputs(dag, fp);
        fclose(fp);
	
	return 0;
}
