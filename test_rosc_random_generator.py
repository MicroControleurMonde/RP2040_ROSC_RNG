from rosc_random_generator import ROSCRandomGenerator

# Initialize and use the ROSC Random Generator
generator = ROSCRandomGenerator()
generator.generate_continuous_random_values(32, 10)

# 32 - for 32 bits, you can adjust it to 4 / 8 / 16 / 24 as you wish.
# 10 - for the number of randon values needed.
