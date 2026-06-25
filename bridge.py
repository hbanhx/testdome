def usage_count(bridge):
    # Write your code here
    result = 0

    # ok = True
    # for b in bridge:
    #     if b <= 0:
    #         ok = False
    ok = True
    while ok:
        new_list = []                   # temporary bridge
        for b in bridge:            
            new_list.append(b - 2)      # integrity -2 
        
        bridge = new_list               # replace with new bridge
        
        for b in bridge:                # check integrety
            if b <= 0:
                ok = False

        if ok:                          # count another pass
            result += 1

    return result

bridge = [7, 6, 5, 8]
print(usage_count(bridge)) # Should print 2
