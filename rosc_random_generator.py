import machine
import time

# Base address of the ROSC
ROSC_BASE = 0x40060000

# Offset to access the RANDOMBIT register
RANDOMBIT_OFFSET = 0x1C
ROSC_STATUS_OFFSET = 0x18
ROSC_CTRL_OFFSET = 0x00

# Constants to control the activation/deactivation of ROSC
ROSC_CTRL_ENABLE = 0xFAB << 12
ROSC_CTRL_DISABLE = 0xD1E << 12

class ROSCRandomGenerator:
    def __init__(self):
        # Check ROSC status on initialization
        if not self.check_rosc_status():
            raise RuntimeError("ROSC is not stable on initialization.")
        
    # Function to check the status of the ROSC
    def check_rosc_status(self):
        status = machine.mem32[ROSC_BASE + ROSC_STATUS_OFFSET]
        enabled = (status >> 12) & 0x1
        stable = (status >> 31) & 0x1
        return enabled and stable

    # Function to reset the ROSC in case of an error
    def reset_rosc(self):
        print("Resetting ROSC...")
        machine.mem32[ROSC_BASE + ROSC_CTRL_OFFSET] = ROSC_CTRL_DISABLE
        time.sleep(0.1)
        machine.mem32[ROSC_BASE + ROSC_CTRL_OFFSET] = ROSC_CTRL_ENABLE
        time.sleep(0.1)

    # Function to read a random bit value
    def read_random_bit(self):
        return machine.mem32[ROSC_BASE + RANDOMBIT_OFFSET] & 0x1

    # Function to generate a random value over n bits
    def generate_random_value(self, n_bits):
        random_value = 0
        for _ in range(n_bits):
            random_bit = self.read_random_bit()
            random_value = (random_value << 1) | random_bit
        return random_value

    # Function to generate and display continuous random values
    def generate_continuous_random_values(self, n_bits, num_values):
        for i in range(num_values):
            random_value = self.generate_random_value(n_bits)
            print(f"Random value # {i + 1}:\t {random_value}")
            if not self.check_rosc_status():
                print("ROSC is not stable. Resetting...")
                self.reset_rosc()

        #print(f"Generated and displayed {num_values} random values.")

# Example of how to use the ROSC Random Generator
def start_random_generation():
    try:
        # Initialize the ROSC Random Generator
        generator = ROSCRandomGenerator()
        print("ROSC is stable. Starting random number generation...\n")
        
        # Generate 10 random values and display them
        n_bits = 32  # Size of random values (32 bits)
        num_values = 10  # Number of values to generate
        generator.generate_continuous_random_values(n_bits, num_values)
        
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_random_generation()
