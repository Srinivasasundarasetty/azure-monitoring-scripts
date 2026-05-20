# Azure VM CPU Alert Checker
# Simple example script for monitoring CPU utilization

def check_cpu_usage(cpu_percentage):
    threshold = 80

    print(f"Current CPU Usage: {cpu_percentage}%")

    if cpu_percentage > threshold:
        print("ALERT: CPU usage is above threshold!")
    else:
        print("CPU usage is normal.")

# Example values
check_cpu_usage(45)
check_cpu_usage(92)
