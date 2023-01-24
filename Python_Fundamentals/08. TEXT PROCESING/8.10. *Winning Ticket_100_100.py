tickets_list = [''.join([t for t in ticket if not t == ' ']) for ticket in input().split(", ")]
result = ''
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:
    symbol_match = False
    if len(ticket) == 20:
        first_half_ticket = ticket[: 10]
        second_half_ticket = ticket[10:]
        for ch in winning_symbols:
            if ch * 6 in first_half_ticket and ch * 6 in second_half_ticket:
                symbol_match = True
                number = min(first_half_ticket.count(ch), second_half_ticket.count(ch))
                if number == 10:
                    result += f'ticket "{ticket}" - 10{ch} Jackpot!\n'
                else:
                    result += f'ticket "{ticket}" - {number}{ch}\n'
        if not symbol_match:
            result += f'ticket "{ticket}" - no match\n'
    else:
        result += "invalid ticket\n"

print(result)
