from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    while len(args) > 0:
        kwargs['a'] += args.popleft()
        if args:
            kwargs['s'] -= args.popleft()
        if args:
            divider = args.popleft()
            if not divider == 0:
                kwargs['d'] /= float(divider)
        if args:
            kwargs['m'] *= args.popleft()
    return(kwargs)

print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))