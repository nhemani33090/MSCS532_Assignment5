# Quicksort Algorithm: Implementation and Analysis

## Overview
This project explores the **Quicksort algorithm**, including **deterministic** and **randomized versions**, analyzing their performance on different types of input data.

## Files
- **quicksort_analysis.py** – Python script implementing both versions of Quicksort and measuring their performance.

## How to Run
1. **Install Python:**
   Make sure Python 3.x is installed on your machine. If not, download and install it from [python.org](https://www.python.org/).

2. Clone this repository:
    ```bash
   git clone https://github.com/nhemani33090/MSCS532_Assignment5.git
   cd MSCS532_Assignment5
   ```
3. Run the script using:
   ```sh
   python3 quicksort_analysis.py
   ```
4. The program will generate execution times for both sorting algorithms on random, sorted, and reverse-sorted data.

## Quicksort Implementations
### **1. Deterministic Quicksort**
- Uses a **fixed pivot** (middle element) for partitioning.
- Performs **O(n log n) on average** but can degrade to **O(n²) in the worst case** if the pivot choice leads to unbalanced partitions.

### **2. Randomized Quicksort**
- Picks a **random pivot**, reducing the chance of worst-case behavior.
- Expected to perform **O(n log n) in most cases**, even for structured input.

## Performance Analysis
The program measures execution times for both versions on:
- **Random data**
- **Sorted data**
- **Reverse-sorted data**

### **Observations**
- **Random Data:** Both versions performed similarly with **O(n log n)** time, but **Randomized Quicksort had a slight overhead** due to random pivot selection.  
- **Sorted Data:** **Deterministic Quicksort was faster** because choosing the middle pivot avoided worst-case behavior, while **Randomized Quicksort was slightly slower** due to extra pivot selection steps.  
- **Reverse-Sorted Data:** Similar to sorted input, **Deterministic Quicksort remained efficient**, while **Randomized Quicksort had minor overhead** from random pivot selection.  

### **Conclusion**
Both **deterministic and randomized Quicksort** achieved **O(n log n)** time in practice with a good pivot strategy. If **deterministic Quicksort had used the first or last element as the pivot**, sorted input would have triggered **O(n²) time complexity**. **Randomized Quicksort helps avoid worst-case scenarios**, but a **well-chosen deterministic pivot (like the middle element) can be slightly faster** due to avoiding the extra step of selecting a random pivot.