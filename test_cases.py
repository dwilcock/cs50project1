import subprocess

def run_test(dataset, source, target):
    """Run degrees.py with specified dataset, source, and target."""
    # Construct the command to run the Python script with parameters
    command = ['python3', 'degrees.py', dataset, source, target]
    
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Output results
    print(f"Testing connection from {source} to {target}:")
    if result.stdout:
        print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)

# Example test cases
run_test('large', 'Kevin Bacon', 'Tom Hanks')
run_test('large', 'Meryl Streep', 'Tom Cruise')
run_test('large', 'Person A', 'Person B')  # Assuming 'Person A' or 'Person B' might not exist
