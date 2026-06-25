def get_minimum_slots(large_slots, small_slots, buses, cars):
    lots_used = 0
    remaining_large_slots = 0
    remaining_small_slots = 0
    remaining_buses = 0
    remaining_cars = 0

    # fit buses - if too many buses then return -1
    if large_slots >= buses:
        remaining_large_slots = large_slots - buses
        lots_used += large_slots - buses
    else:
        return -1
    
    if remaining_large_slots > 0:

        lots_used += remaining_large_slots / ( cars // 3) 
        remaining_cars = remaining_large_slots % 3

        if small_slots > remaining_cars:
            lots_used += small_slots / cars
        else:
            return -1
    
    
    return lots_used

print(get_minimum_slots(2, 12, 1, 4)) # should print 3