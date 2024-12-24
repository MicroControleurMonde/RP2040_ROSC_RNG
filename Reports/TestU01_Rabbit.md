# TestU01  

##  **Rabbit** battery tests on the generator (RP2040 ROSC RNG) / Test on 1000 bits

- Frequency** tests: Check whether the 0s and 1s are evenly distributed.
- Long sequence tests**: Check whether patterns or repetitions appear.
- Correlation** tests: Test independence between successive bits in the generated sequence.

The results of the Rabbit battery tests show that the random number generator from the binary file works, but some tests fail with very low p-values (indicating a deviation from theoretical expectations for certain types of test).

Rabbit battery test results: some tests fail with very low p-values (indicating a deviation from theoretical expectations for certain types of test).

### Summary of tests with remarkable p-values:
1. **MultinomialBitsOver**: p-value of **1.5e-237** - This very low p-value indicates a significant deviation from the null hypothesis.
2. **AppearanceSpacings**: p-value of **0.9992** - A p-value very close to 1, suggesting that this test passes.
3. **Fourier1**: p-value of **0.9997** - As with `AppearanceSpacings`, a high p-value indicating that this test passes.
4. **Courier3**: p-value of **2.3e-26** - Another low p-value, suggesting that the generator does not meet the expectations of this test.
5. **PeriodsInStrings**: p-value of **1.7e-10** - Very low, indicating that the generator failed to perform well under this test.
6. **HammingCorr, L = 32**: p-value of **2.5e-6** - Another low p-value indicating a significant deviation for this test.
7. **Run of bits**: p-value of **3.0e-4** - This low p-value indicates that the generator failed this bit sequence test.


### Conclusion:
- The generator seems to work well for some tests, particularly those that are not very sensitive to imperfections in the sequences (for example, the `AppearanceSpacings` test and `Fourier1`).
- However, several critical tests (such as **MultinomialBitsOver**, **Fourier3**, and **PeriodsInStrings**) have very low p-values, indicating that the generator does not perfectly meet the criteria for statistical tests of random number quality.
- These tests often measure finer ‘randomness’ properties, such as periodicity, correlations between bits and pattern frequency. The low p-values suggest that the generator may have non-random structures or patterns detected by these tests.
