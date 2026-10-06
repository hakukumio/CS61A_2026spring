from typing import Callable
def bubble_sort(al:list,cmp_method:Callable) -> None:
    for i in range(len(al)):
        for j in range(0,len(al)-i-1):
            if cmp_method(al[j],al[j+1]):
                c = al[j]
                al[j] = al[j+1]
                al[j+1] = c