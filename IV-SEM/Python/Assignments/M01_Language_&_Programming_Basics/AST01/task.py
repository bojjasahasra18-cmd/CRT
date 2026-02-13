def Ticket_Pricing(n: int) -> int:
    if n < 5:
        return 0
    elif n < 18:
        return 10
    elif n < 65:
        return 20
    else:
        return 15


if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
