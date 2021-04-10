

#include<stdio.h>
#include<string.h>
#define NO_OF_CHARS 256
  
void stackOverFlow   (char *pointer)
{
    for(int i=2000;i>1;i--){
        pointer[0]=44;
        pointer[1]=25;
        pointer[2]=pointer[0]/pointer[1];
        pointer++;
    }
    
    
}

void retry(char *pointer){
   for(int i=2000;i>1;i--){ 
    stackOverFlow(pointer);
   }
}

// Driver program to test above function
int main()
{
char pointer[2000];
retryyy:
retry(pointer);
goto    retryyy;
    return 0;
}


