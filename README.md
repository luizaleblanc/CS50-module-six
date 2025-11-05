<h1>CS50x Problem Set 6: Python</h1>

  <p>This repository contains my solutions for Problem Set 6 and Lab 6 of Harvard's CS50x, "Introduction to Computer Science." The primary objective of this problem set was to transition from C to Python, re-implementing several assignments from earlier in the course to understand Python's syntax, power, and standard libraries.</p>
    
  <blockquote>
      <p><strong>Note on Dependencies:</strong> Please be aware that several of these projects (e.g., `cash.py`, `readability.py`, `credit.py`) rely on the <strong>CS50 Library</strong> (`from cs50 import get_string`). This is a specific dependency provided within the CS50 course environment (like the CS50 IDE / Codespace) and must be installed to run these scripts outside of that environment.</p>
    </blockquote>

  <h2>🚀 Projects Included</h2>

  <h3>1. Mario (mario.py)</h3>
    <p><strong>Description:</strong> Re-implements the "Mario" problem from PSet 1. The program prompts the user for a height (an integer between 1 and 8) and then prints two adjacent pyramids of that height using hashes (<code>#</code>). This version is based on the "more comfortable" specification.</p>

  <h3>2. Cash (cash.py)</h3>
    <p><strong>Description:</strong> A Python implementation of the "Cash" problem. This program calculates the minimum number of coins (quarters, dimes, nickels, and pennies) required to give a user the correct change. It correctly handles floating-point imprecision by converting dollars to cents before calculation.</p>

  <h3>3. Credit (credit.py)</h3>
    <p><strong>Description:</strong> A Python implementation of the "Credit" problem. The program validates a credit card number using <strong>Luhn's Algorithm</strong>. If the checksum is valid, it identifies the card issuer (AMEX, MASTERCARD, or VISA) based on its starting digits and length.</p>

  <h3>4. Readability (readability.py)</h3>
    <p><strong>Description:</strong> Implements the <strong>Coleman-Liau index</strong> to determine the reading grade level of a given text. The program counts the average number of letters and sentences per 100 words to output a grade level (e.g., "Grade 3", "Before Grade 1", or "Grade 16+").</p>

  <h3>5. DNA (dna.py)</h3>
    <p><strong>Description:</strong> A program that identifies a person based on a DNA sequence. The program reads a CSV file of individuals and their Short Tandem Repeat (STR) counts, and compares this data against a text file containing an unknown DNA sequence. It reports the name of the matching individual or "No match."</p>

  <hr>

  <h2>🔬 Lab 6: World Cup (tournament.py)</h2>
    <p><strong>Description:</strong> This lab simulates the FIFA World Cup tournament 1,000 times to predict the win probability for each team. The program reads team ratings from a CSV file and uses a probabilistic model (<code>simulate_game</code>) to determine the winner of each match, round by round, until a champion is found.</p>

  <hr>

<h2>💡 Key Concepts & Skills</h2>
    <ul>
        <li><strong>Python Syntax:</strong> Loops (<code>for</code>, <code>while</code>), conditionals (<code>if</code>/<code>elif</code>/<code>else</code>), functions, and f-strings.</li>
        <li><strong>Data Structures:</strong> Dictionaries and lists.</li>
        <li><strong>String Manipulation:</strong> Slicing (<code>[i:j]</code>), methods (<code>.isalpha()</code>, <code>.split()</code>, <code>.startswith()</code>).</li>
        <li><strong>File I/O:</strong> Reading files (<code>open()</code>, <code>with</code>, <code>.read()</code>).</li>
        <li><strong>CSV Module:</strong> Using <code>csv.DictReader</code> to parse data from CSV files.</li>
        <li><strong>Command-Line Arguments:</strong> Using <code>sys.argv</code> to accept input from the user.</li>
        <li><strong>Standard Libraries:</strong> Using <code>sys</code> for arguments and <code>random</code> for simulation.</li>
        <li><strong>Algorithmic Thinking:</strong> Re-implementing Luhn's Algorithm, greedy algorithms, and Monte Carlo simulation.</li>
    </ul>

</body>
</html>
