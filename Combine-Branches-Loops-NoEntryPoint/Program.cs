using System;

int sum = 0;
for(int num = 1; num <= 20; ++num)
{
    if (num % 3 == 0 )
    {
        sum += num;
    }
}
Console.WriteLine($"The sum is {sum}");