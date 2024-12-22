# Test_ROSC.py
'''
    Test and manage the Ring Oscillator (ROSC) of a microcontroller.
    This script interacts with the ROSC registers to enable, check, and reset the ROSC.
    It continuously monitors the status of the ROSC and attempts to keep it stable by resetting it if needed.
    ## Registers:
        ROSC_CTRL (Control Register) - Address used to enable or disable the ROSC.
        ROSC_STATUS (Status Register) - Address used to check the ROSC's status (enabled/disabled and stable/unstable).
    ## Key Functions:
        - configure_rosc() : Enables the ROSC and waits for it to stabilize.
        - check_rosc_status() : Reads and reports the current status of the ROSC (enabled and stable).
        - reset_rosc() : Disables and re-enables the ROSC to reset it.
    ## Main Loop:
        The script continuously checks the ROSC status at regular intervals (2 seconds) and attempts to reset it if it becomes unstable or disabled.
        The loop will stop after the ROSC has been stable for 5 consecutive checks.
    ## Constants:
        ROSC_CTRL_ENABLE : Value used to enable the ROSC in the control register.
        ROSC_CTRL_DISABLE : Value used to disable the ROSC in the control register.
    ## Usage:
        - This script is designed to be run specifically on a RP2040 MCU.
        - It uses the `machine` module to access memory-mapped registers and control hardware.
    Author: [MicroControleurMonde]
    Date: [22.12.2024]
'''

import machine
import time

# Define the base address for the ROSC registers
ROSC_BASE = 0x40060000

# Define registers and their offsets
ROSC_CTRL_OFFSET = 0x0
ROSC_STATUS_OFFSET = 0x18

# Register addresses
ROSC_CTRL = ROSC_BASE + ROSC_CTRL_OFFSET
ROSC_STATUS = ROSC_BASE + ROSC_STATUS_OFFSET

# Constants for ROSC control
ROSC_CTRL_ENABLE = 0xFAB << 12
ROSC_CTRL_DISABLE = 0xD1E << 12

def configure_rosc():
    # Enable ROSC
    machine.mem32[ROSC_CTRL] = ROSC_CTRL_ENABLE
    time.sleep(0.1)  # Wait for the ROSC to stabilise

def check_rosc_status():
    status = machine.mem32[ROSC_STATUS]
    enabled = (status >> 12) & 0x1
    stable = (status >> 31) & 0x1
    
    print(f"ROSC Status: {'Enabled' if enabled else 'Disabled'}, {'Stable' if stable else 'Unstable'}")
    return enabled and stable

def reset_rosc():
    print("Resetting ROSC...")
    machine.mem32[ROSC_CTRL] = ROSC_CTRL_DISABLE
    time.sleep(0.1)
    machine.mem32[ROSC_CTRL] = ROSC_CTRL_ENABLE
    time.sleep(0.1)

# Initialise and configure the ROSC
configure_rosc()

# Main loop
success_count = 0
max_success = 5
check_interval = 2  # secondes

while True:
    if check_rosc_status():
        success_count += 1
        if success_count >= max_success:
            print(f"ROSC stable for {max_success} consecutive checks. Stopping tests.")
            break
    else:
        print("ROSC error detected. Resetting...")
        reset_rosc()
        success_count = 0
    
    time.sleep(check_interval)


