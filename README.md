# Stress Strain Calculator
Stress and Strain Analysis System

## Group Members:

| Member | Primary Responsibility |
|---|---|
| Mikaela Stefanie Tilo | Task 1 – Basic Stress and Strain Calculator |
| Mary Belle Cubol | Task 2 – Control Structures and Validation |
| Pauline Ashley Balangue | Task 3 – Data Structures and Test History |
| Coleen Dian Fernandez | Task 4 – Functions and Modular Programming |
| Rolando Banjo Alano | Task 4 – Functions and Modular Programming |
| Meghan Isabelle Espiritu | Task 5 – Object-Oriented Programming |

**Task 6 – Modular Integration was completed collaboratively by all members.**

### Project Description

The Stress and Strain Analysis System is a Python-based application designed to calculate and analyze the stress and strain of materials.

### Program Features
- Calculate stress and strain  
- Calculate Young's modulus  
- Calculate factor of safety  
- Support predefined and custom materials  
- Support metals, plastics, and composites  
- Validate user inputs  
- Handle invalid values  
- Perform multiple calculations  
- Store calculation history  
- Track unique materials used  
- Generate session summaries  
- Compare and analyze materials and test results  
- Save and load results using JSON  
- Export test data to CSV  
- Record test timestamps  
- Manage files and directories  
- Generate simulated test data where appropriate  
- Use a modular program structure  

### Installation/Requirements

- Python 3.11 or later
- No additional packages are required

## How to Run the Program

Run the following command in the project directory:

```
python main.py
```

### Repository Structure

Brief description of the modules used in the project.

main.py – Main entry point and User Interface  
database.py – Initial material loading and predefined records  
material.py – Handles object-oriented Material hierarchy  
utils.py – Handles pure mathematical and validation functions  
tests.py – Test representations and test suites  
properties.py – Handles material data containers and  properties




### Testing 
The Stress and Strain Analysis System was tested using different input values to verify that the calculations, validation, data storage, and file operations work correctly.

Test 1 – Steel

Input:  
Force: 50,000 N  
Area: 0.01 m²  
Original Length: 10 m  
Change in Length: 0.005 m  

Expected Output:  
Stress = 5,000,000 Pa  
Strain = 0.0005  




Test 2 – Aluminum

Input:  
Force: 10,000 N  
Area: 0.002 m²  
Original Length: 1 m  
Change in Length: 0.0015 m  

Expected Output:  
Stress = 5,000,000 Pa  
Strain = 0.0015  

### Additional Tests
The application was also tested for:  
- Invalid numeric inputs  
- Negative input values  
- Zero area  
- Zero original length  
- Different material selections  
- Multiple test records  
- JSON implementation  
- CSV export implementation  
- Execution of the main program  

All tests were completed successfully.

