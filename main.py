def f(s, m):
    if s >= 301: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 3, m - 1), f(s * 5, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h) # any(h) для 19й задачи т.к. неуд ход

