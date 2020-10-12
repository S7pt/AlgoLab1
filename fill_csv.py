import csv
import random

if __name__ == '__main__':
    with open('csv_list.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['color', 'RPM', 'stroke_frequency', 'producer_name'])
        for i in range(15000):
            csv_writer.writerow(
                [random.randint(0, 1999), random.randint(0, 1999), random.randint(0, 1999), random.randint(0, 1999)])
