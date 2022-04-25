using System;
using System.IO;

namespace GeneratorApp
{
    class Generator
    {
        static void Main(string[] args)
        {
            Random r = new Random();
            int x, y;
            string path = @"C:\Users\kazik\Desktop\work\algorytmy2\otoczka_wypukla\dane.txt";
            int n_pktow = 10;
            using(StreamWriter sw = File.CreateText(path))
            {
                sw.WriteLine(n_pktow);
              for (int i = 0; i<n_pktow;++i)
              {
                 x = r.Next(-100, 100);
                  y = r.Next(-100, 100);
                  sw.WriteLine("{0} {1}", x, y);
               }
            }
        }
    }
}
