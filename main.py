def f(s, m):
    if s >= 301: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 3, m - 1), f(s * 5, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h) # any(h) для 19й задачи т.к. неуд ход

print('19', [s for s in range(1, 301) if f(s, 2)])
print('20', [s for s in range(1, 301) if f(s, 3) and not f(s, 1)])
print('21', [s for s in range(1, 301) if f(s, 4) and not f(s, 2)])