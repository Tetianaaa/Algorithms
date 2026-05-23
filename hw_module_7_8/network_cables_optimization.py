import heapq

def min_cable_costs(cables):
    if not cables or len(cables) < 2:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        current_cost = first + second
        total_cost += current_cost
        heapq.heappush(cables, current_cost)

    return total_cost

# checking:
cables = [4, 10, 3, 5, 1]
print(f"MIN cost: {min_cable_costs(cables)}")