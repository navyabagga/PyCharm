'''
Sam is given a rectangular paper having dimensions h*w, where h is the height and w is the width. Sam wants to
fold the paper so its dimensions are h1*w1 in the minimum number of moves. The paper can only be folded parallel
to its edges and after folding, the dimensions should be integers.

For example, given h=8 and w=4, fold the paper until it is h1, w1 = 6, 1. First fold along the long edge 6 units from a
side, resulting in a paper that is 6*4. Next, fold along the width 2 units from the 4 unit edge to have 6*2.
Fold along the center of the 2 unit edge to achieve a 6*1 page in three folds.
minMoves has following parameters :
h : an integer that denotes the initial height
w : an integer that denotes the initial width
h1 : an integer that denotes the final height
w1 : an integer that denotes the final width
Constraints
1 <= h, w, h1, w1 <= 10^15
h1 <= h
w1 <= w
Sample Input 0
2
3
2
2
Sample Output
1
'''
h=int(input())
w=int(input())
h1=int(input())
w1=int(input())
if h==h1 and w==w1:
    print("0")
c = 0
while h!=h1 and w!=w1:
    while h!=h1:
        if h//2>=(h-h1):
            h=h-(h-h1)
            c+=1
        else:
            h=h//2
            c+=1
    while w!=w1:
        if w//2>(w-w1):
            w=w-(w-w1)
            c=c+1
        else:
            w=w//2
            c+=1
print(c)

