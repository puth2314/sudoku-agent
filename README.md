# sudoku-solver
A simple sudoku solver.


- https://sudokuessentials.com/x-wing/
- https://sudokuessentials.com/sudoku-xy-wing/
- http://sudokuessentials.com/Sudoku_Swordfish/

- https://www.thonky.com/sudoku/singles
- https://sudoku.com.au/Sudoku-Tips-and-Strategies.aspx
- http://www.sudokusnake.com/techniques.php
- http://hodoku.sourceforge.net/en/tech_singles.php
- https://www.sudopedia.org/wiki/Solving_Technique


Optimizations for Backtracking in Sudoku

    Constraint Propagation:
        Naked Singles: If a cell can only take one possible number, place that number immediately.
        Hidden Singles: If a number can only appear in one cell within a row, column, or box, place it there.

    Forward Checking:
        Before placing a number in a cell, check if it leads to a conflict later on. If placing a number reduces the options for other cells to zero, backtrack immediately.

    Least Constraining Value:
        When choosing which number to place next, select the one that leaves the most options open for other cells. This helps reduce the likelihood of hitting dead ends.

    Most Constrained Variable:
        Select the cell with the fewest valid candidates first. This reduces the search space and can lead to quicker solutions.

    Using Heuristics:
        Combine various heuristics to guide the search process, helping the algorithm focus on the most promising paths first.

For Very Difficult Puzzles

When dealing with particularly tough Sudoku puzzles, additional techniques may be useful:

    Constraint Satisfaction Techniques:
        Advanced algorithms like AC-3 can be employed to reduce the search space more effectively by enforcing arc consistency.

    Backtracking with Lookahead:
        Implement a deeper lookahead strategy, where the algorithm simulates placing numbers in several cells ahead to identify potential issues before they arise.

    Exact Cover Problem Approach:
        Transform the Sudoku into an exact cover problem and use algorithms like Dancing Links (DLX) for a more efficient search.

    Stochastic Methods:
        Techniques like simulated annealing or genetic algorithms can be used, especially for generating solutions or when exact solutions are hard to find.

    Machine Learning Approaches:
        Train models on various Sudoku puzzles to predict placements or identify promising strategies.

These optimizations and techniques can significantly enhance the efficiency and effectiveness of solving very difficult Sudoku puzzles.

    # Naked SIngle, Hidden Single
    # Naked Pair, Hidden Pair, # Pointing Pair
    # Naked Triple, Naked Quad, Pointing Triples, Hidden Triple, Hidden quad
    # Xwing, Swordfish, jellyfish, xywing, xyzwing

https://en.wikipedia.org/wiki/Sudoku_solving_algorithms 
https://github.com/neeru1207/AI_Sudoku
https://github.com/MorvanZhou/sudoku
https://github.com/dhhruv/Sudoku-Solver
https://github.com/jeffsieu/py-sudoku
https://github.com/JoeKarlsson/python-sudoku-generator-solver
https://github.com/obijywk/grilops
https://github.com/ashutosh1919/neuro-symbolic-sudoku-solver
https://github.com/manpreet1130/RealTime-Sudoku-Solver
https://github.com/aakashjhawar/SolveSudoku
https://github.com/ctjacobs/sudoku-genetic-algorithm
https://github.com/Nisheet-Patel/Sudoku-Solver-Pro
https://github.com/cabustillo13/Resolvedor-de-Sudoku
https://github.com/AsadiAhmad/Sudoku-Solver
https://github.com/vmunoz82/sudoku-challenge
https://github.com/David-Elkabas/Sudoku
https://github.com/sraaphorst/dlx-python
https://github.com/rg1990/cv-sudoku-solver
https://github.com/unmade/dokusan
https://github.com/LiorSinai/SudokuSolver-Python
https://github.com/ScriptRaccoon/sudoku-solver-python