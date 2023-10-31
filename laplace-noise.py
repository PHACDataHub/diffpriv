import math
import csv

def sum(file_path, column_index):
	try:
		with open(file_path, 'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			column_sum = 0
			for row in csv_reader:
				try:
					value = float(row[column_index])
					column_sum += value
				except (ValueError, IndexError):
					print(f"Skipping invalid or missing value in row {csv_reader.line_num}.")
			return column_sum
	except FileNotFoundError:
		print(f"File not found: {file_path}")
		return None
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		return None

def laplace_noise(scale):
	uniform1 = 0.5
	uniform2 = 0.5
	return round(-scale * math.copysign(1, uniform1 - 0.5) * math.log(1 - 2 * abs(uniform2 - 0.5)))

file_path = input("Enter the path to the CSV file: ")
column_index = int(input("Enter the index of the column to sum: "))
epsilon = float(input("Enter the value of epsilon for Laplace noise: "))

result = sum(file_path, column_index)
if result is not None:
	print(f"Sum of the column {column_index} in the CSV file: {result}")
	noise = laplace_noise(1 / epsilon)
	noisy_sum = result + noise
	print(f"Noisy sum with Laplace noise: {noisy_sum}")
	