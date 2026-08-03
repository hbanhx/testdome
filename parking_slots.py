# def get_minimum_slots(large_slots, small_slots, buses, cars):
#     lots_used = 0
#     remaining_large_slots = large_slots
#     remaining_small_slots = small_slots
#     remaining_buses = buses
#     remaining_cars = cars

#     # fit buses - if too many buses then return -1
#     if remaining_large_slots >= remaining_buses:
#         remaining_large_slots -= remaining_buses
#         lots_used += remaining_buses
#     else:
#         return -1
    
#     if remaining_large_slots > 0:
#         max_cars_in_large = remaining_large_slots * 3

#         if remaining_cars >= max_cars_in_large:
#             remaining_cars -= max_cars_in_large
#             lots_used += remaining_large_slots
#             remaining_large_slots = 0
#         else:
#             lots_used += max_cars_in_large // remaining_cars

#     if remaining_small_slots > remaining_cars:
#         lots_used += remaining_cars
#     else:
#         return -1
    
    
#     return lots_used

# print(get_minimum_slots(2, 12, 1, 4)) # should print 3




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
    
    # fit cars in large slots (3 cars per large slot)
    if remaining_large_slots > 0:
        max_cars_in_large = remaining_large_slots * 3

        if remaining_cars >= max_cars_in_large:
            # fill all large slots with cars
            remaining_cars -= max_cars_in_large
            lots_used += remaining_large_slots
            remaining_large_slots = 0
        else:
            # only some large slots needed
            used_large_for_cars = (remaining_cars + 2) // 3
            lots_used += used_large_for_cars
            remaining_large_slots -= used_large_for_cars
            remaining_cars = 0

    # fit remaining cars in small slots
    if remaining_small_slots >= remaining_cars:
        lots_used += remaining_cars
    else:
        return -1
    
    return lots_used

print(get_minimum_slots(2, 12, 1, 4))  # should print 3
