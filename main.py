# Assumptions
# - Box kinds are unique
# 

import operator

def max_number_of_units(box_descriptions, truck_capacity):
    
    # Create sorted list by total units list with (boxes_available, box_capacity) as key
    unsorted_remaining_boxes = {}
    for boxes_available, box_capacity in box_descriptions:
        unsorted_remaining_boxes[(boxes_available, box_capacity)] = boxes_available * box_capacity
    remaining_boxes = sorted(unsorted_remaining_boxes.items(), key=operator.itemgetter(1), reverse=True)
    print(f"{remaining_boxes}")
    # print(f"{remaining_boxes}")
    
    units_loaded = 0
    while truck_capacity > 0 and len(remaining_boxes) > 0:
        # Get first item out of list
        box = remaining_boxes[0]
        ((boxes_remaining, box_capacity), total_units) = box
        # print(f"{boxes_remaining}, {box_capacity}, {total_units}")
        
        # check if i can dump all of the boxes in the truck
        
        
        # If i can , great!
        # do it, deduct the toal number of boxes from the capacity and continue
        if boxes_remaining < truck_capacity:
            units_loaded = units_loaded + total_units
            truck_capacity = truck_capacity - boxes_remaining
            remaining_boxes.pop(0)
        else:
             # If I can't, deduct as much as I can and I should exit loop normally
             boxes_used = truck_capacity
             truck_capacity = truck_capacity - boxes_used
             units_loaded = units_loaded + (boxes_used * box_capacity)
             remaining_boxes.pop(0)
        
        # truck_capacity = truck_capacity - 1
        print(f"{box}, {truck_capacity}, {units_loaded}")
       
        
    
    return units_loaded