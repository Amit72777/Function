// calculate a salary
#include<stdio.h>
#include<conio.h>
#include<math.h>
float har( float basic , float  h);
float  da( float basic, float d);
void main ()
{
float  basic,h,d,g;
clrscr();
printf("Enter the basic salary ");
scanf("%f",&basic);

if ( basic<=10000)
{ h=20;
 d=80;
 h=har(basic,h);
 d=da(basic,d);
 g = basic + h+d;
 printf("gross salary is =%f",g);
 }
 else if (basic<=20000)
 {
 h=25; d=90;
 h=har(basic,h);
 d=da(basic,d);
 g=basic +h+d;
 printf("gorss salary is %f",g);
 }
 else if ( basic >=20001)
 { h=30;d=95;
 h=har(basic,h);
 d=da(basic,d);
 g=basic+h+d;
 printf("gross salary is %f",g);
 }
 getch();
 }

 float  har(float basic ,float h)
 {
 h=basic*(h/100.0);
 return h;
 }
 float da(float basic,float  d)
 {
 d=basic*(d/100.0);
  return d;
  }
