#include<stdio.h>
FILE *f;
int n=456, m=7, b[3][7];
unsigned int q=882334423;
float ff=456.79608, a[10];
double s, c[3];
int qwerty[9]={67878,2398,5865,7987,65978,8234,1235,89754,123};
float deneme[5]={456.87345,879.5654,345.6589,345.87965,12354.324324};
long xxx[12]={34543,34534543,534534,5,346575,75,67,65765765,1324657,6890957,5293467,7426657};
long doublelong[4][5]={{438748,96968,3292948,4800785,1653740},{5474748,3759773,375893,4960784,2625154},{4648703,284967,4867038,109394,2939406},{3475345,678768,430952,569780,456904}};
double doubledouble[3][3]={{56.56565,546546.54654,23413.123},{34.57898,123.12368,78987.78965},{1233.5676,982345.12345,3457.7688}};
char doublechar[3][11]={{12,67,87,34,90,69,12,34,45,56,67},{13,24,35,46,57,68,79,80,14,25,36},{86,58,39,71,26,29,37,40,68,65,43}};
unsigned int doubleuint[2][13]={{456,346,679,234,689,124,379,19,1357,791,8903,983,6890679},{345,345,4353434,54367876,589089,34709,5379,44575,43567,534,879895,34234,1312312423}};
unsigned char x=13;
char xx=11;
long y=3;
char yy=9;
unsigned char abc=5;
main()
{ int i,j;
f = fopen("1-binary.dat","w");
fwrite(&abc,sizeof(unsigned char),1,f);
fwrite(&yy,sizeof(char),1,f);
fwrite(&xx,sizeof(char),1,f);
fwrite(&y,sizeof(long),1,f);
fwrite(&x,sizeof(unsigned char),1,f);
fwrite(qwerty,sizeof(int),9,f);
fwrite(deneme,sizeof(float),5,f);
fwrite(xxx,sizeof(long),12,f);
fwrite(doublelong,sizeof(long),20,f);
fwrite(doubledouble,sizeof(double),9,f);
fwrite(doublechar,sizeof(char),33,f);
fwrite(doubleuint,sizeof(unsigned int),26,f);
fclose(f); }