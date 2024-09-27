import math

def main():
    x = 0.5  # Buy multiplier
    y = 1.2  # Sell multiplier
    
    input_file = 'input.txt'
    output_file = 'output.txt'
    items = read_items_from_file(input_file)
    write_items_to_file(items, x, y, output_file)

def read_items_from_file(input_file):
    items = {}
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('Buy: ')
            item_name = parts[0].strip().replace('_', ' ').replace('-', '').strip()  
            buy_sell = parts[1].split(' Sell: ')
            buy_price = int(buy_sell[0].strip())
            sell_price = int(buy_sell[1].strip())
            items[item_name] = {'buy': buy_price, 'sell': sell_price}
    return items

def custom_round(value):
    if value - int(value) >= 0.5:
        return math.ceil(value)
    else:
        return int(value)

def write_items_to_file(items, x_multiplier, y_multiplier, output_file):
    with open(output_file, 'w') as file:
        item_count = len(items)
        for index, (item_name, prices) in enumerate(items.items()):
            formatted_name = item_name.replace(' ', '_').upper()
            new_buy = custom_round(prices['buy'] * x_multiplier)
            new_sell = custom_round(prices['sell'] * y_multiplier)
            file.write(f"{formatted_name} {{\n")
            file.write(f"    sellingValue: {new_sell}\n")
            file.write(f"    buyValue: {new_buy}\n")
            if index < item_count - 1:
                file.write("},\n")
            else:
                file.write("}\n")

main()