def exclusiveTime(n, logs):
    times = [0] * n
    prev_t = 0
    stack = []
    for log in logs:
        f, status, t = log.split(':')
        f, t = int(f), int(t)
        if status == 'start':
            if stack:
                times[stack[-1]] += t - prev_t
            stack.append(f)
            prev_t = t
        else:
            times[stack.pop()] += t - prev_t + 1
            prev_t = t + 1
    return times

n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
res = exclusiveTime(n, logs)
print(res)