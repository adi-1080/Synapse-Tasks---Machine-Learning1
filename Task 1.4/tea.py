customers = [[5,2],[5,4],[10,3],[20,1]]

def average_waiting_time(customers):
    current_time = 0
    waiting_time = []
    for arrival_time,time_required in customers:
        if(arrival_time>current_time):
            iroh_waiting_time = arrival_time - current_time
            current_time = current_time + iroh_waiting_time
        
        wait_time = current_time + time_required - arrival_time
        waiting_time.append(wait_time)
        
        current_time = current_time + time_required
        
    avg = sum(waiting_time)/ len(customers)
    return avg

avg_time = average_waiting_time(customers)
print(f"Average waiting time of customers : {avg_time}")