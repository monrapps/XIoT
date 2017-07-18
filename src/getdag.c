#include <stdio.h>
#include "Xsocket.h"

int main(){
	char dag[200], fid[100];
	int sock = Xsocket(AF_XIA, SOCK_STREAM, 0);	
	XreadLocalHostAddr(sock, dag, 200, fid, 100);	
	FILE *fp = fopen("./dag","w");
	fputs(dag, fp);
        fclose(fp);
	return 0;
}
