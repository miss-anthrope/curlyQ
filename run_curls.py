import subprocess
import shlex

def execute_curl_commands(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        commands = [line.strip() for line in file if line.strip()]

    if not commands:
        print("No cURL commands found in the file.")
        return

    with open("curl-out.txt", "w", encoding='utf-8') as outfile:
        for i, curl_command in enumerate(commands, start=1):
            print(f"\n=== Running command {i}/{len(commands)} ===")
            print(curl_command)

            # Tokenize safely
            try:
                args = shlex.split(curl_command)
            except ValueError as e:
                print(f"Error parsing command {i}: {e}")
                continue

            # Execute command
            try:
                result = subprocess.run(
                    args,
                    capture_output=True,
                    text=True
                )

                print("=== Output ===")
                print(result.stdout)
                if result.stderr:
                    print("=== Errors ===")
                    print(result.stderr)

                # Save results
                outfile.write(f"\n=== Command {i} ===\n")
                outfile.write(f"{curl_command}\n\n")
                outfile.write(result.stdout)
                if result.stderr:
                    outfile.write("\n--- Errors ---\n")
                    outfile.write(result.stderr)
                outfile.write("\n" + "="*60 + "\n")

            except Exception as e:
                print(f"Execution error for command {i}: {e}")

    print("\nAll commands completed. Results saved to 'curl-out.txt'.")

if __name__ == "__main__":
    input_file = input("Enter the path to the file containing cURL commands: ").strip()
    execute_curl_commands(input_file)
