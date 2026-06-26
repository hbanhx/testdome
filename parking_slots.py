def get_minimum_slots(large_slots, small_slots, buses, cars):
    lots_used = 0
    remaining_large_slots = large_slots
    remaining_small_slots = small_slots
    remaining_buses = buses
    remaining_cars = cars

    # fit buses - if too many buses then return -1
    if remaining_large_slots >= remaining_buses:
        remaining_large_slots -= remaining_buses
        lots_used += remaining_buses
    else:
        return -1
    
    if remaining_large_slots > 0:
        remaining_cars = remaining_cars - (remaining_large_slots * 3)
        

        lots_used += remaining_large_slots 
        remaining_cars = remaining_cars % 3

        if remaining_small_slots > remaining_cars:
            lots_used += remaining_small_slots // remaining_cars
        else:
            return -1
    
    
    return lots_used

print(get_minimum_slots(2, 12, 1, 4)) # should print 3