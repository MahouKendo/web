using System;
using System.Collections.Generic;
using System.Text;

namespace StockManagement
{
    public class StockItem
    {
        private int code;
        private string name;
        private int quantityInStock;

        public int Code 
        { 
            get { return code; } 
            set{}
        }
        public string Name 
        {
            get { return name; }
            set {}
        }
        public int QuantityInStock 
        { 
            get { return quantityInStock; }
            set {}
        }

        public StockItem(int code, string name, int qtyInStock)
        {
            switch (name) 
            {
                case "" when code < 0 && qtyInStock <= 0:
                    throw new Exception("Item code must be a positive integer. Item name cannot be blank. Quantity cannot be zero or negative. ");
                case "":
                    throw new Exception("Item name cannot be blank. ");
            }//check name

            if(name.Length > 20)
            {
                throw new Exception("Name must only contain at most 19 characters");
            }//check name length

            if (string.IsNullOrWhiteSpace(name) == true && code < 0)
            {
                throw new Exception("Item code must be a positive integer. Item name cannot be just spaces. ");
            }//check space with code

            else if (string.IsNullOrWhiteSpace(name) == true)
            {
                throw new Exception("Item name cannot be just spaces. ");
            }//check space

            else
            {
                this.name = name;
            }//add name

            string check = Convert.ToString(code);
            if(check.Length > 9)
            {
                throw new Exception("Code must be at most 9 characters");
            }//check code length

            switch (code) 
            {
                case int n when n < 0:
                    throw new Exception("Item code must be a positive integer. ");
                default:
                    this.code = code;
                    break;
            }//check code

            switch (qtyInStock)
            {
                case int n when n <= 0:
                    throw new Exception("Quantity cannot be zero or negative. ");
                default:
                    this.quantityInStock = qtyInStock;
                    break;
            }//check stock

        }

        public void AddQuantity(int qty)
        {
            if (qty < 0)
            {
                throw new Exception("Quantity cannot be negative");
            }
            this.quantityInStock += qty;
        }//add quantity

        public void SubtractQuantity(int qty)
        {
            if (qty < 0)
            {
                throw new Exception("Quantity cannot be negative");
            }
            if (this.quantityInStock < qty)
            {
                throw new Exception("Insufficient quantity in stock");
            }
            this.quantityInStock -= qty;
        }//subtract quantity

        public int GetCode()
        {
            return code;
        }//get code

        public string GetName()
        {
            return name;
        }//get name

        public int GetQuantityInStock()
        {
            return quantityInStock;
        }//get quantity


    }
}

