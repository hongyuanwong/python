distances = [3, 5, 2, 8, 6, 4, 7, 5]
for distance in distances: 
    print(distance)
    shortest = min(distances)
    longest = max(distances)
    total = sum(distances)
    average = total / len(distances)
    print(f"The shortest distance: {shortest}")
    print(f"The longest distance: {longest}")
    print(f"The total distance: {total}")
    print(f"The average dstance is: {average}")
numbers = list(range(1,9))
print(numbers) # no training days
distances_km = [3, 5, 2, 8, 6, 4, 7, 5]
distances_meters = [km * 1000 for km in distances_km]
print(distances_meters)
distances = [3, 5, 2, 8, 6, 4, 7, 5]
first_three = distances[0:3]
middle_three = distances[3:6]
last_three = distances [5:8]
print(f"First three distances: {first_three}")
print(f"Middle three distances: {middle_three}")
print(f"Last three distances: {last_three}")
distances = [3, 5, 2, 8, 6, 4, 7, 5]
updated_distances = distances[:]
updated_distances.append('10')
print("Original distances:")
print(distances)
print("Updated distances:")
print(updated_distances)
track_size = (100, 50)
print("Original track dimensions:")
for track in track_size:
    print(track)
track_size = (120, 60)
print("\nNew track dimensions:")
for track in track_size:
    print(track)
    