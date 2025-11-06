import subprocess

def execute_curl_from_file(filename):
    # Read the cURL command from the specified file
    with open(filename, 'r') as file:
        curl_command = file.read().strip()

    # Execute the cURL command using subprocess
    try:
        result = subprocess.run(
            curl_command,
            shell=True,
            capture_output=True,
            text=True
        )

        # Print the output to the terminal
        print("=== cURL Output ===")
        print(result.stdout)

        # Print any errors (stderr) if they exist
        if result.stderr:
            print("=== cURL Errors ===")
            print(result.stderr)

        # Save both stdout and stderr to a file
        with open("curl-out.txt", "w") as outfile:
            outfile.write("=== cURL Output ===\n")
            outfile.write(result.stdout)
            if result.stderr:
                outfile.write("\n=== cURL Errors ===\n")
                outfile.write(result.stderr)

        print("\nOutput saved to 'curl-out.txt'.")

    except Exception as e:
        print(f"Error executing cURL command: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to the file containing the cURL command: ").strip()
    execute_curl_from_file(input_file)
