def get_minimum_slots(large_slots, small_slots, buses, cars):
    result = 1
    remaining_large_slots = 0
    remaining_small_slots = 0
    remaining_buses = 0
    remaining_cars = 0

    if large_slots >= buses:
        remaining_large_slots = large_slots - buses

    else:
        return -1
    
    if remaining_large_slots > 0:
        remaining_small_slots = remaining_large_slots - cars // 3


        remaining_small_cars
            
    return result

print(get_minimum_slots(2, 12, 1, 4)) # should print 3