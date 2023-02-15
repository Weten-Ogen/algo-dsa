def draw_line(tick_len, tick_label= ''):

    line = '-' * tick_len

    if tick_label:
        line +=  ' ' + tick_label
    
    print(line)

def draw_interval(center_len):
    if center_len > 0:
        draw_interval(center_len - 1)
        draw_line(center_len)
        draw_interval(center_len - 1)
    

def draw_ruler(inches, major_len):
    draw_line(major_len, '0')
    for j in range(1, 1 + inches):
        draw_interval(major_len - 1)
        draw_line(major_len,str(j))


draw_ruler(1000000000000, 5)