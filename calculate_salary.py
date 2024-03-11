employees = {
    "Alice": {"base_salary": 5000, "performance_bonus": 1000, "medical_leaves": 2},
    "Jen": {"base_salary": 6000, "performance_bonus": 1200, "medical_leaves": 1},
    "Martin": {"base_salary": 3000, "performance_bonus": 1000, "medical_leaves": 0},
    "Patrik": {"base_salary": 2800, "performance_bonus": 800, "medical_leaves": 4},
    "David": {"base_salary": 3000, "performance_bonus": 1500, "medical_leaves": 0},
    "Maria": {"base_salary": 4500, "performance_bonus": 500, "medical_leaves": 3},
    "Alexandra": {"base_salary": 8000, "performance_bonus": 500, "medical_leaves": 5},
    "Eva": {"base_salary": 5000, "performance_bonus": 1100, "medical_leaves": 1},
}


def calculate_monthly_salary(employee_data):
    base_salary = employee_data["base_salary"]
    performance_bonus = employee_data["performance_bonus"]
    medical_leaves = employee_data["medical_leaves"]

    monthly_salary = base_salary + performance_bonus - (
                medical_leaves * 100)  # Assuming a deduction of $100 for each medical leave
    return monthly_salary


for employee, data in employees.items():
    monthly_salary = calculate_monthly_salary(data)
    print(f"{employee}: ${monthly_salary}")


