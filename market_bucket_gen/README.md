# Food Basket Generator

The Food Basket Generator is a command-line application that generates a CSV file containing a basket of randomly selected food items.

## Usage

To use the Food Basket Generator, run the script with the following command-line arguments:

```bash
python script_name.py <rows> <columns> <filename> [--custom-food-list FOOD_ITEMS...]
```

- `<rows>`: Number of rows in the CSV file (required, integer).
- `<columns>`: Number of columns in the CSV file (required, integer).
- `<filename>`: Filename for the generated CSV file (required, string).
- `--custom-food-list FOOD_ITEMS...`: Optional flag to specify a custom list of food items separated by spaces.

### Example Usage:

```bash
python script_name.py 5 4 output.csv --custom-food-list Pizza Ice_Cream Broccoli
```

This command generates a CSV file named `output.csv` with 5 rows and 4 columns, containing randomly chosen food items from the default list along with additional items provided in the `--custom-food-list` flag.

## How it Works

- The script uses the `argparse` library to handle command-line arguments.
- It generates random combinations of food items to create a basket based on the specified rows and columns.
- Optionally, it allows users to provide a custom list of food items to include in the basket.

## Requirements

- Python 3.x
- Required Python packages: `csv`, `random`, `argparse`

## Installation

1. Clone the repository:

2. Navigate to the directory:

3. Run the script with the provided command-line arguments as described in the "Usage" section.
