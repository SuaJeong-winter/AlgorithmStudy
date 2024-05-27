def solution(ineq, eq, n, m):
    t_ineq = ""
    t_eq = ""

    if n==m:
        if ineq==">" or ineq=="<":
            if eq== "=":
                return 1
            else:
                return 0
    else:
        if n>m:
            if ineq==">":
                return 1
            else:
                return 0
        else:
            if ineq=="<":
                return 1
            else:
                return 0
