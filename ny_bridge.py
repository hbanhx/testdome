def usage_count(bridge):
    # Write your code here
    result = 0

    # ok = True
    # for b in bridge:
    #     if b <= 0:
    #         ok = False
    ok = True
    while ok:
        new_list = []
        for b in bridge:
            new_list.append(b - 2)
        
        bridge = new_list
        
        for b in bridge:
            if b <= 0:
                ok = False

        if ok:
            result += 1

    return result

bridge = [7, 6, 5, 8]
print(usage_count(bridge)) # Should print 2
