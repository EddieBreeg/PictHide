#include <iostream>
#include <windows.h>
#include <conio.h>

using namespace std;

int main()
{
    system("title PictHide");
    cout << "-Cacher une image (1)" << endl << "-Reveler une image (2)" << endl;
    int key = getch();
    if (key == 49)
    {
        system("@echo off");
        system("python main.py \"hide()\"");
    }
    else if (key == 50)
    {
        system("@echo off");
        system("python main.py \"reveal()\"");
    }
}
