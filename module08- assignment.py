# Module 6 Assignment: Functions and Modular Programming
# TechRetail Sales Analysis System

print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# -----------------------------------------------------------
# DATA STRUCTURES
# -----------------------------------------------------------

sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# -----------------------------------------------------------
# SALES ANALYSIS FUNCTIONS
# -----------------------------------------------------------

def calculate_total_sales():
    """Returns total revenue from all sales."""
    total = 0
    for sale in sales_data:
        total += sale[2] * sale[3]
    return total


def calculate_category_sales(category):
    """
    Returns total revenue for a specific category.
    
    Args:
        category (str): Category name.
        
    Returns:
        float: Category revenue.
    """
    total = 0
    for sale in sales_data:
        if sale[1] == category:
            total += sale[2] * sale[3]
    return total


def find_best_selling_product():
    """
    Finds product with highest revenue.
    
    Returns:
        tuple: (product_name, revenue)
    """
    best_product = ""
    highest_revenue = 0

    for sale in sales_data:
        revenue = sale[2] * sale[3]
        if revenue > highest_revenue:
            highest_revenue = revenue
            best_product = sale[0]

    return (best_product, highest_revenue)

# -----------------------------------------------------------
# COMMISSION FUNCTIONS
# -----------------------------------------------------------

def calculate_employee_commission(employee_id):
    """
    Calculates commission for one employee.
    
    Args:
        employee_id (str)
        
    Returns:
        float: Commission amount
    """
    total_sales = 0

    for sale in sales_data:
        if sale[4] == employee_id:
            total_sales += sale[2] * sale[3]

    commission_rate = employees[employee_id][1]
    return total_sales * commission_rate


def calculate_total_commission():
    """Returns total commission for all employees."""
    total = 0
    for emp_id in employees:
        total += calculate_employee_commission(emp_id)
    return total

# -----------------------------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------------------------

def get_products_by_category(category):
    """
    Returns list of product names in a category.
    
    Args:
        category (str)
        
    Returns:
        list
    """
    products = []
    for sale in sales_data:
        if sale[1] == category:
            products.append(sale[0])
    return products


def calculate_average_sale_price():
    """
    Calculates average sale price across all units sold.
    
    Returns:
        float
    """
    total_revenue = 0
    total_quantity = 0

    for sale in sales_data:
        total_revenue += sale[2] * sale[3]
        total_quantity += sale[3]

    return total_revenue / total_quantity

# -----------------------------------------------------------
# REPORT FUNCTIONS
# -----------------------------------------------------------

def generate_sales_summary(include_categories=True):
    """
    Generates formatted sales summary report.
    
    Args:
        include_categories (bool)
        
    Returns:
        str
    """
    report = ""
    total = calculate_total_sales()
    average_price = calculate_average_sale_price()

    report += f"Total Sales Revenue: ${total:.2f}\n"
    report += f"Average Sale Price: ${average_price:.2f}\n"

    if include_categories:
        report += "\nCategory Breakdown:\n"
        categories = set([sale[1] for sale in sales_data])
        for category in categories:
            report += f"{category}: ${calculate_category_sales(category):.2f}\n"

    return report


def generate_employee_report():
    """
    Generates employee performance report.
    
    Returns:
        str
    """
    report = ""

    for emp_id, info in employees.items():
        name = info[0]
        total_sales = 0

        for sale in sales_data:
            if sale[4] == emp_id:
                total_sales += sale[2] * sale[3]

        commission = calculate_employee_commission(emp_id)

        report += f"{name} - Sales: ${total_sales:.2f} | Commission: ${commission:.2f}\n"

    return report

# -----------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------

def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)

    print("\nTOTAL QUARTERLY SALES:")
    print(f"${calculate_total_sales():.2f}")

    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for category in categories:
        print(f"{category}: ${calculate_category_sales(category):.2f}")

    print("\nBEST-SELLING PRODUCT:")
    product, revenue = find_best_selling_product()
    print(f"{product} - ${revenue:.2f}")

    print("\nEMPLOYEE COMMISSIONS:")
    for emp_id, info in employees.items():
        commission = calculate_employee_commission(emp_id)
        print(f"{info[0]}: ${commission:.2f}")

    print("\nQUARTERLY SALES SUMMARY REPORT:")
    print(generate_sales_summary())

    print("\nEMPLOYEE PERFORMANCE REPORT:")
    print(generate_employee_report())


if __name__ == "__main__":
    main()