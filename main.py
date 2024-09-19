import csv

# Function to read sales data from the CSV file
def read_sales_data(filename):
    sales_data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header
        for row in csv_reader:
            sales_data.append(row)
    return sales_data

# Function to calculate the total sales for each customer
def calculate_totals(sales_data):
    customer_totals = {}
    for row in sales_data:
        customer_id = row[0]
        amount = float(row[3])  # Assuming the sales amount is in the 4th column
        if customer_id in customer_totals:
            customer_totals[customer_id] += amount
        else:
            customer_totals[customer_id] = amount
    return customer_totals

# Function to write the sales report to a new CSV file
def write_sales_report(filename, customer_totals):
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Customer ID', 'Total Sales'])
        for customer_id, total in customer_totals.items():
            csv_writer.writerow([customer_id, total])

# Main function to coordinate the tasks
def main():
    input_file = 'sales.csv'
    output_file = 'salesreportFINAL.csv'

    # Step 1: Read the sales data
    sales_data = read_sales_data(input_file)

    # Step 2: Calculate the total sales for each customer
    customer_totals = calculate_totals(sales_data)

    # Step 3: Write the results to a new CSV file
    write_sales_report(output_file, customer_totals)

if __name__ == "__main__":
    main()
