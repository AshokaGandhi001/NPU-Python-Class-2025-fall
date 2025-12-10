from pi import buffon_needle_simulation

throw_time = [10, 20, 50, 100, 500, 1000, 5000, 10000, 50000]
for time in throw_time: 
    print(buffon_needle_simulation(time))