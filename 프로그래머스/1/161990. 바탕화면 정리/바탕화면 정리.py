def solution(wrapper):
    lux, luy = 50, 50
    rdx, rdy= 0, 0
    for x in range(len(wrapper)):
        for y in range(len(wrapper[0])):
            if wrapper[x][y] == "#":
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x)
                rdy = max(rdy, y)
    return [lux, luy, rdx + 1, rdy + 1]
