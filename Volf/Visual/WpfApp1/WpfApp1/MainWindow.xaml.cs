using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        
        public MainWindow()
        {
            InitializeComponent();
        }
        
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Random rnd = new Random();
            int rand_num1 = rnd.Next(100);
            rand1.Text = rand_num1.ToString();

        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Random rnd = new Random();
            int rand_num2 = rnd.Next(100);
            rand2.Text = rand_num2.ToString();
            
        }

        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            int a = Convert.ToInt32(rand1.Text);
            int b = Convert.ToInt32(rand2.Text);
            int vysledek = a + b;
            soucet.Text = vysledek.ToString();

        }
    }
}
