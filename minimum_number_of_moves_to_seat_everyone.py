def minMovesToSeat(seats, students):
        
    seats.sort()
    students.sort()
    if len(seats) == len(students):
        moves = 0
    for i, j in zip(seats, students):
        if i!= j:
            moves += abs(i-j)
    return moves

seats = [3,1,5]
students = [2,7,4]
print(minMovesToSeat(seats, students))