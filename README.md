# RP2040 ROSC RNG 🇬🇧

###### 🇫🇷 [Version française ici](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Lisez_moi_fr.md) 

![Image locale](https://github.com/MicroControleurMonde/RP2040-RNG/blob/main/Reports/RP2040-resizeimage3.png)

https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Lisez_moi_fr.md

A Micro-python library that provides an interface to generate a random number using the recommended method (ROSC reading) by Raspberry.
- Library : `rosc_random_generator.py` -  Python library for generating random numbers
- Test Script: `test_rosc_random_generator.py` - Example script demonstrating how to use the library.

##### (Update 12.22.2024)
- `Test_ROSC.py` - The initial code that I used to test RP2040 ROSC.
---
## Index
1. [Context](#context)
2. [Project description](#project-description)
3. [Prerequisites](#prerequisites)
4. [Use](#use)
5. [Example of output](#example-of-output)
6. [Operation](#operation)
7. [Performance test](#performance-test)
8. [Statistical and quality tests](#statistical-and-quality-tests)
9. [Acknowledgment](#Acknowledgment)
10. [Disclaimer](#Disclaimer)
11. [Special tribute](#tribute-special)
---
## Context:

Raspberry foundation recently updated their Pico Datasheet:
`Datasheet - Build-date: 2024-10-15 / Build-version: eec2b0c-clean` 

[RP2040 Pico datasheet (Chapter 2.17)](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)

**Page 222.  Chapter 2.17. Ring Oscillator (ROSC)**, here is what we can read:

    2.17.5. Random Number Generator
    
    If the system clocks are running from the XOSC and/or PLLs the ROSC can be used to generate 
    random numbers. Simply enable the ROSC and read the RANDOMBIT register to get a 1-bit 
    random number and read it n times to get an n-bit value. This does not meet the requirements
    of randomness for security systems because it can be compromised, but it may be useful in 
    less critical applications. If the cores are running from the ROSC then the value will not be
    random because the timing of the register read will be correlated to the phase of the ROSC.
    
The random number generator uses the ROSC (Resonance Oscillator) to produce random bits.

---
## Project Description

This project implements a True Random Number Generator (TRNG) using the RP2040 microcontroller. The generator use the Ring Oscillator as recommended in the datasheet..

## Requirements

- RP2040-based microcontroller.
- MicroPython firmware installed on the board.
- **`machine`**, **`time`** (built-in with MicroPython).

## Usage

1. **rosc_random_generator.py – Library for generating random numbers**

This Python library provides a class `ROSCRandomGenerator` that generates random numbers based on the RP2040's RSOC.

2. **test_rosc_random_generator.py – Example script**

This script imports the `ROSCRandomGenerator` class from rosc_random_generator.py and generates random numbers

### Installation
- Save thess codes in files named `rosc_random_generator.py` and `test_rosc_random_generator.py`.
- To use this library in another project, just import it like any Python module.

### Output Example:

The RP2040 ROSC RNG generates random integer numbers as **32-bit values**.

        ROSC is stable. Starting random number generation...

        Random value # 1:	 2880935910
        Random value # 2:	 3756622924
        Random value # 3:	 4041343900
        Random value # 4:	 41689329
        Random value # 5:	 1860732466
        Random value # 6:	 2376253135
        Random value # 7:	 2057898098
        Random value # 8:	 3392796777
        Random value # 9:	 1501861143
        Random value # 10:	 238555703
## How it Works

- 1 - The program declares the variables and constants required to interact with the ROSC.
- 2 - It checks the state of the ROSC to ensure that it is stable.
- 3 - If the ROSC is stable, it generates 32-bit random values, displaying each value and regularly checking the stability of the ROSC.
- 4 - If instability is detected, the program resets the ROSC and waits for it to stabilize before continuing.
- 5 - Once the values have been generated, it displays an end message.

This way, this process ensures that the ROSC is correctly initialised and stable before random values are generated, and manages the reset in the event of a stability problem during the process.

## Performance Test

**Caution**: no writing on flash !

- Estimated time to generate 1'425'424 values: **2'143 seconds** (approx. 35 minutes)
- Average time per value: **0.0015 sec**
- Throughput: **2660 Bytes/sec**
- Number of values generated per second: **665 values/sec**

- [Data sample](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rp2040_rosc_rng_1425424.bin)

## Statistical and Quality Tests

**Note:** Following a kind reminder from Scruss [(Link)](https://github.com/scruss), I changed the output file format from ASCII to Binary.

        When converting random integers into ASCII strings, there is a loss of entropy ! A 32-bit 
        integer represents a value that can be expressed in a range of 4,294,967,296 possible 
        values (from 0 to 2^32 - 1). This integer range contains 32 bits of entropy.
        
        Due to the way ASCII characters are represented (for example, numbers or letters), 
        some of the entropy is lost due to the limited number of possible characters. Each 
        character in ASCII contains approximately 3.45 bits of entropy instead of the 
        8 possible entropy bits for a complete byte (Log₂ 11 ≈ 3.459).


### 1. `Ent` Test Report 
#### (Updated 22.12.2024)

  ([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Sample size: **5.43 Mo MB**
- Total generated: **1'425'424 values**
- Entropy = **7.973888** bits per byte (measure of randomness - Max=**8**)

- [Ent Report - Raw](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Ent_rp2040_rosc_rng_1425424.txt)
- [Ent Report Analyse](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Ent_1Mil_Report_Analyse.md)

[Scatter plot representation](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Scatter%20Plot.png) [Full size]

![Scatter](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Webp.net-resizeimage2.png)

[Values histogram](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Histogram%20of%20Random%20Numbers.png) [Full size]

![Histogram](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Webp.net-resizeimage.png)


### 2. `Dieharder` Test Report
##### (Updated 22.12.2024)
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **5.43 Mo MB**
- Total generated: **1'425'424 values**

- [Dieharder Report - Raw](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Dieharder_rp2040_rosc_rng_1425424.txt)
- [Dieharder Report Analyses](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/Dieharder_1Mil_Report_Analyse.md)

### 3. `TestU01` (**Rabbit** battery)
##### (Updated 24.12.2024)
(https://simul.iro.umontreal.ca/testu01/tu01.html)
- C code snippet (only Main):


        int main() {
            // Path to binary file
            const char *filename= "/home/user_name/rp2040_rosc_rng_1425424.bin";
            // Create a generator from the file
            unif01_Gen *gen = create_gen(filename);
            if (gen == NULL) {
             return 1;
            }
            // Example with the Rabbit test battery
            printf("Starting tests from the \n file");
            bbattery_Rabbit(gen, 1000); // Test on 1000 bits

            // Memory release
            close(global_gen->file);
            free(global_gen); // Free the generator state
            free(gen); // Free the generator
            
            return 0;
  
[TestU01 Raw](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/TestU01_results_test.txt)
  
[Test Report](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/TestU01_Rabbit.md)

- Some low p-values suggest that the generator may have _**non-random structures or patterns**_ detected by these tests.


### 4. `rngtest` (Validation FIPS 140-2)
##### (Updated 24.12.2024)
(https://salsa.debian.org/hmh/rng-tools/)
- Test result: **all the FIPS tests failed** :warning:

[`rngtest` Test Report](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rngtest_rp2040_rosc_rng_1425424.txt)

[`rngtest` Report Analyse](https://github.com/MicroControleurMonde/RP2040_ROSC_RNG/blob/main/Reports/rngtest_rp2040_rosc_rng_1425424.md)

## Acknowledgements

The project is based on the RP2040 microcontroller, and its MicroPython firmware.
- `Waveshare RP2040-Plus: MicroPython ef518cbf2-dirty on 2023-03-24;`
- `XIAO seed studio: MicroPython v1.22.1 on 2024-01-05;`

## Disclaimer

The code contained in this repository is provided “as is”, without any warranty of performance, accuracy or result. The author shall not be liable for any direct or indirect damages that may result from the use of this code, including, but not limited to, loss of data or interruption of service.

Use of this code is entirely at your own risk. Please ensure that you fully understand the code before using it in a production environment or integrating it into your projects.

## Special tribute:

### Passing of John Walker

We are deeply saddened to hear of the passing of John Walker, one of the founders of Autodesk. He died at home in Switzerland, on 2nd February 2024, aged 74.

[The announcement was shared here.](https://www.engineering.com/a-cad-legend-passes-autodesk-founder-john-walker-1949-to-2024/)
