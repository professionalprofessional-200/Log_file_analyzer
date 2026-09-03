def analyze_log_file(filename):
    info_count = 0
    warning_count = 0
    error_count = 0

    error_logs = []

    try:
        # Open and read the log file
        with open(filename, "r") as file:

            for line in file:
                line = line.strip()

                # Ignore empty lines
                if not line:
                    continue

                # Validate log format
                if ":" not in line:
                    print(f"Invalid log entry ignored: {line}")
                    continue

                # Get log type
                log_type = line.split(":", 1)[0].strip().upper()

                # Count log types
                if log_type == "INFO":
                    info_count += 1

                elif log_type == "WARNING":
                    warning_count += 1

                elif log_type == "ERROR":
                    error_count += 1
                    error_logs.append(line)

                else:
                    print(f"Invalid log type ignored: {line}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
        return

    except Exception as error:
        print(f"Unexpected error: {error}")
        return

    # Calculate total logs
    total_logs = info_count + warning_count + error_count

    # Find most frequent log type
    log_counts = {
        "INFO": info_count,
        "WARNING": warning_count,
        "ERROR": error_count
    }

    most_frequent_type = max(log_counts, key=log_counts.get)

    # Display ERROR logs
    print("\n" + "=" * 50)
    print("                 ERROR LOGS")
    print("=" * 50)

    if error_logs:
        for log in error_logs:
            print(log)
    else:
        print("No ERROR logs found.")

    # Display summary report
    print("\n" + "=" * 50)
    print("                SUMMARY REPORT")
    print("=" * 50)

    print(f"Total Logs       : {total_logs}")
    print(f"Total INFO Logs  : {info_count}")
    print(f"Total WARNING Logs : {warning_count}")
    print(f"Total ERROR Logs : {error_count}")
    print(f"Most Frequent Log Type : {most_frequent_type}")

    print("=" * 50)


# Start the log analyzer
analyze_log_file("log.txt")