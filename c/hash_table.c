// example.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 20792

typedef struct {
    double x;
    double y;
} POINT;

typedef struct {
    int key;
    int value;
} UvData;


UvData* uv_compare(POINT data_1[], POINT data_2[]) {
    UvData* uv_data = (UvData*)malloc(SIZE * sizeof(UvData));
    int num = 0;
    for (int i =0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++) {
            if (memcmp(&data_1[i],&data_2[j],sizeof(POINT))==0){
                uv_data[num].key = i;
                uv_data[num].value = j;
                num++;
            }
        }
    }
    return uv_data;
}
