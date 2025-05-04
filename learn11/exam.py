import concurrent.futures
import time

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate(numbers):
    for number in numbers:
        cpu_bound(number)

def calculate_concurrent(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)

def main():
    start = time.time()
    numbers = [100 + x for x in range(2000)]
    calculate(numbers)
    # calculate_concurrent(numbers)
    end = time.time()
    print("total time: {:.2f} seconds".format(end - start))

if __name__ == '__main__':
    main()