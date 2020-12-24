#include<iostream>
#include<fileapi.h>


using namespace std;

main()
{
    int a,islem,deg;
    int diz[141];
    char dizi[141] , degdiz[141];
    FILE *in , *out , *dizim;
    dizim=fopen("dizi.jpeg","r");
    in=fopen("gelen.jpeg","r");
    cout<<"Yapilacak islemi seciniz: \n 1:Yaz 2:Oku 3:Dosyalari Temizle\n";
    cin>>islem;
    switch(islem)
    {
        case 1:
            {
                cout<<"Mesaj Giriniz: ";
                out=fopen("giden.jpeg","w");
                for(int say=0;say<140;say++)
                {
                    cin>>dizi[say];
                    if(dizi[say]=='q')
                        break;
                }

                for(int sayi=0;sayi<140;sayi++)
                {
                fscanf(dizim,"%d",&deg);
                dizi[sayi]+=deg;
                fprintf(out,"%c",dizi[sayi]);
                }
            break;
            }
        case 2:
            {
                in=fopen("gelen.jpeg","w");
                out=fopen("giden.jpeg","r");
                for(int sayac=0;sayac<140;sayac++)
                {
                    fscanf(dizim,"%d",&deg);
                    fscanf(out,"%c",&degdiz[sayac]);
                    degdiz[sayac]-=deg;
                }
                for(int sayac=0;sayac<140;sayac++)
                    fprintf(in,"%c",degdiz[sayac]);
            }


            }
            system("pause");
    }
