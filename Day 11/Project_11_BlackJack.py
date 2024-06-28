import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
user_cards=[]
comp_cards=[]
is_game_over= False
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw"
    elif comp_score==0:
        return "Lose, opponent has BlackJack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score==0:
        return "You went over, You Lose."
    elif user_score==0:
        return "Opponent went over, You win"
    elif user_score>comp_score:
        return "You win"
    else:
        return "You Lose"
    

for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())


while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"Your cards: {user_cards}, current_score:{user_score}")
    print(f"Computer first card: {comp_cards[0]}")
    if user_score==0 or comp_score==0 or user_score>21:
        is_game_over=True
    else:
        if input("Type 'y' to get another card, type 'n' to pass: "):
            user_cards.append(deal_card())
        else:
            is_game_over=True
while comp_score !=0 and comp_score<17:
    comp_cards.append(deal_card())
    comp_score=calculate_score(comp_cards)
print(f"Your final hand:{user_cards}, final news: {user_score}")
print(f"Your final hand:{comp_cards}, final news: {comp_score}")
print(compare(user_score, comp_score))