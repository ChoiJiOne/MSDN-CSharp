var fibonacciNumbers = new List<int>() { 1, 1 };

while (fibonacciNumbers.Count < 20)
{
    var previous1 = fibonacciNumbers[fibonacciNumbers.Count - 1];
    var previous2 = fibonacciNumbers[fibonacciNumbers.Count - 2];
    fibonacciNumbers.Add(previous1 + previous2);
}

Console.WriteLine($"20 Fibonacci is {fibonacciNumbers[19]}");