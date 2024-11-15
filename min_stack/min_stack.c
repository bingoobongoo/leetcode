#include <stdlib.h>

typedef struct {
    int* arr;
    int len;
    size_t cap;
} MinStack;


MinStack* minStackCreate() {
    size_t cap = 30000 * sizeof(int);
    int* arr = malloc(cap);
    int len = 0;
    MinStack* minstack = malloc(sizeof(MinStack));

    minstack->arr = arr;
    minstack->len = len;
    minstack->cap = cap;

    return minstack;
}

void minStackPush(MinStack* obj, int val) {
    size_t required_cap = obj->cap + sizeof(int);
    if (obj->cap < required_cap) {
        obj->arr = realloc(obj->arr, required_cap);
        obj->cap = required_cap;
    }
    obj->arr[obj->len] = val;
    obj->len++;
}

void minStackPop(MinStack* obj) {
    obj->len--;
}

int minStackTop(MinStack* obj) {
    return obj->arr[obj->len-1];
}

int minStackGetMin(MinStack* obj) {
    int min = __INT32_MAX__;
    for (int i=0; i<obj->len; i++) {
        if (obj->arr[i] < min) {
            min = obj->arr[i];
        }
    }

    return min;
}

void minStackFree(MinStack* obj) {
    free(obj->arr);
    free(obj);
}