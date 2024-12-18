# RP2040 ROSC RNG

![Image locale](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/RP2040-resizeimage3.png)

A Micro-python library that provides an interface to generate a random number using the recommended method (ROSC reading) by Raspberry.

---
# Under construction !

## Context:

Raspberry foundation recently updated their Pico Datasheet:
`Raspberry Pi Pico Datasheet - Build-date: 2024-10-15 / Build-version: eec2b0c-clean`

Page 222.  Chapter 2.17. Ring Oscillator (ROSC), here is what we can read:

    2.17.5. Random Number Generator
    
    If the system clocks are running from the XOSC and/or PLLs the ROSC can be used to generate random numbers.
    Simply enable the ROSC and read the RANDOMBIT register to get a 1-bit random number and read it n times to get an n-
    bit value. This does not meet the requirements of randomness for security systems because it can be compromised,
    but it may be useful in less critical applications. If the cores are running from the ROSC then the value will not be
    random because the timing of the register read will be correlated to the phase of the ROSC.
    
The random number generator uses the ROSC (Resonance Oscillator) to produce random bits.

---
## Project Description

This project implements a True Random Number Generator (TRNG) using the RP2040 microcontroller. The generator collects Use the Resonance Oscillator as preconized in the Datasheet.

## Requirements

- RP2040-based microcontroller.
- MicroPython firmware installed on the board.
- **`machine`**, **`time`** (built-in with MicroPython).

## Usage

## How it Works

## Performance

## Ent Test Report

## Dieharder Test Report


## Acknowledgements

The project is based on the RP2040 microcontroller, and its MicroPython firmware.
- Waveshare RP2040-Plus: MicroPython ef518cbf2-dirty on 2023-03-24;
- XIAO seed studio: MicroPython v1.22.1 on 2024-01-05;

## Disclaimer

The code contained in this repository is provided “as is”, without any warranty of performance, accuracy or result. The author shall not be liable for any direct or indirect damages that may result from the use of this code, including, but not limited to, loss of data or interruption of service.

Use of this code is entirely at your own risk. Please ensure that you fully understand the code before using it in a production environment or integrating it into your projects.
