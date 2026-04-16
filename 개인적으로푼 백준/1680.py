trashcar_move = []
tcase = int(input())
for i in range(tcase):
    tcurrent = 0
    tcarmove = 0
    jic = 0
    Tc_cap, tc_visit = map(int,input().split())
    for j in range(tc_visit):
        t_dis, t_weight = map(int,input().split())
        tcarmove += (t_dis - jic)
        if Tc_cap > tcurrent + t_weight:
            tcurrent +=t_weight
            jic = t_dis
        elif Tc_cap == tcurrent + t_weight:
            tcarmove += t_dis
            tcurrent = 0
            jic = 0
        else :
            tcarmove += t_dis * 2
            tcurrent =t_weight
            jic = t_dis
    if tcurrent  > 0:
        tcarmove += t_dis
    trashcar_move.append(tcarmove)
for i in range(len(trashcar_move)):
    print(trashcar_move[i])