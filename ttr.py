import time
import sys

def run_timer(duration_seconds=None):
    """
    Display a running timer in the console.
    If duration_seconds is provided, the timer will count down from that value.
    Otherwise, it will count up indefinitely.
    """
    start_time = time.time()
    
    try:
        while True:
            if duration_seconds:
                # Countdown timer
                elapsed = time.time() - start_time
                remaining = max(0, duration_seconds - elapsed)
                
                if remaining <= 0:
                    sys.stdout.write("\rTime's up!           \n")
                    break
                
                mins, secs = divmod(int(remaining), 60)
                hours, mins = divmod(mins, 60)
                timer_str = f"Time remaining: {hours:02d}:{mins:02d}:{secs:02d}"
            else:
                # Count up timer
                elapsed = time.time() - start_time
                mins, secs = divmod(int(elapsed), 60)
                hours, mins = divmod(mins, 60)
                timer_str = f"Time elapsed: {hours:02d}:{mins:02d}:{secs:02d}"
            
            sys.stdout.write(f"\r{timer_str}")
            sys.stdout.flush()
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nTimer stopped.")

# Example usage:
if __name__ == "__main__":
    # For a countdown timer (e.g., 5 minutes)
    # run_timer(5 * 60)
    
    # For a stopwatch (counting up)
    run_timer()