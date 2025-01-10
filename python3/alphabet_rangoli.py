def print_rangoli(size):
    if not size > 0:
        print()

    # height    = (2 * size) - 1
    # width     = ((size - 1) * 4 ) + 1
    # character max =  ascii = size + 60
    # gen [] of chars?
    #  each char above 1 adds 4 width

    char_arr = [chr(x) for x in range(size + 96, 96, -1)]
    mask_arr = list(range(size - 1, 0, -1)) + list(range(size))

    # gen the thing through...
    # sweet fucking easy my ass
    # so starts with (height - 1) * "-" then char_arr[0] and (height - 1) * "-"
    # then its 2 less "-" and char_arr[1] + "-" and char_arr[0]
    # print(mask_arr)
    # everything but the last gets a "-" postfixed ...
    # str += char_arr[i] + "\n" if i == (size - 1) else char_arr[i] + "-"
    
    
    
    # need a loop, j
    # "--" if j < i
    # char_arr[i] + "-"
    #   Middle line xD
    for j in mask_arr:
        
        result_str = ""
        
        for i in range(size):
            if i < j:
                result_str += "--"
            else:
                result_str += char_arr[i-j] + "-"
                
        for i in range(size - 2, -1, -1):
            if i < j:
                result_str += "--" if i != 0 else "-"
            else:
                result_str += char_arr[i-j] if i == 0 else char_arr[i-j] + "-"
            
        print(result_str)
    
    # 1 = a
    
    # 2 = --b--
    #     b-a-b
    #     --b--
    
    # 3 = ----c----
    #     --c-b-c--
    #     c-b-a-b-c
    #     --c-b-c--
    #     ----c----


