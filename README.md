# Math Homework Helpers: Pseudo-Random Number Generation

Small Python scripts that check coursework calculations by computer instead of by hand.

## Monte Carlo: Linear Congruential Generators (`monte_carlo/A1.py`)

A **linear congruential generator (LCG)** produces pseudo-random integers with the recurrence

$$x_{n+1} = (a\,x_n + c) \bmod m$$

The script:

- generates LCG sequences from several seeds and parameter sets (for example `a = 5, c = 7, m = 13` and `a = 3, c = 1, m = 13`) to inspect cycles and periods;
- checks the **Hull–Dobell theorem** conditions for a full period `m`:
  1. `c` and `m` are coprime,
  2. `a − 1` is divisible by every prime factor of `m`,
  3. `a − 1` is divisible by 4 if `m` is divisible by 4.

  This uses a small prime-factorization helper, applied to `a = 8121, m = 134456`.

## Running it

```bash
pip install -r rqmts.txt
python monte_carlo/A1.py
```

## Tech stack

Python · SymPy
