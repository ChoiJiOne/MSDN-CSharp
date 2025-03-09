using System;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        StringBuilder builder = new();
        builder.AppendLine("The following arguments are passed: ");

        foreach (var arg in args)
        {
            builder.AppendLine($"Argument={arg}");
        }

        Console.WriteLine(builder.ToString());
    }
}