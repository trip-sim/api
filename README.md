# Roadtrip Cost Simulator
A little program to help calculate the cost of a road trip. Intended for a road trip where a car is rented and with the passengers flying back. It can be used for a round trip by omitting flight costs and doubling the distance.

## Features
* Simulates the price for a road trip for a range of passengers and duration so that cost can be compared.
* Chooses the most cost-efficient rental vehicles from a given options
* Calculates number of cars needed and number of lodging rooms needed based on passengers
* Provides output in an easy-to-understand format through pandas

## Usage
There is no user interface, so the source must be edited directly. Relevant files are ```__main__.py``` and ```simulate.py```. Everything else should (probably) be untouched.

## Example Output
```bash
   number of people  number of days  gas cost  rental cost  lodging cost  flight cost  food cost  total cost  cost per person  cost per day  cost per day per person
6                 3               7     153.0          700           750          124        147      1874.0            625.0         268.0                     89.0
7                 3               8     153.0          800           875          124        168      2120.0            707.0         265.0                     88.0
8                 3               9     153.0          900          1000          124        189      2366.0            789.0         263.0                     88.0
3                 2               7     153.0          700           750          124         98      1825.0            913.0         261.0                    130.0
4                 2               8     153.0          800           875          124        112      2064.0           1032.0         258.0                    129.0
5                 2               9     153.0          900          1000          124        126      2303.0           1152.0         256.0                    128.0
0                 1               7     153.0          700           750          124         49      1776.0           1776.0         254.0                    254.0
1                 1               8     153.0          800           875          124         56      2008.0           2008.0         251.0                    251.0
2                 1               9     153.0          900          1000          124         63      2240.0           2240.0         249.0                    249.0
```
