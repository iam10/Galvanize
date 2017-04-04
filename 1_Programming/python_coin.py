

def find_change(coins, value):
    value_left = value
    num_coins = 0
    for i in reversed(coins):
        while value_left - i >= 0:
            num_coins += 1
            value_left -= i
        if value_left == 0:
            break
    return num_coins

if __name__ == '__main__':
    print(find_change([1,5,10,25], 100))
