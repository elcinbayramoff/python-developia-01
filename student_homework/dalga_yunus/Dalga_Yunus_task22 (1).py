# 1

# import datetime
# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
#         self.account_holder = account_holder
#         self.balance = initial_balance
#         self.interest_rate = interest_rate
#         self.transaction_history = []

#     def get_balance(self):
#         return f"Balans: ${self.balance:.2f}"

#     def apply_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         self._add_transaction("Faiz", interest)
#         return f"Faiz tətbiq olundu. Balans yeniləndi: ${self.balance:.2f}"

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Yatırılan məbləğ sıfır və ya mənfi ola bilməz."
#         self.balance += amount
#         self._add_transaction("Yatırma", amount)
#         return f"${amount:.2f} yatırıldı. {self.get_balance()}"

#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Çıxarılan məbləğ sıfır və ya mənfi ola bilməz."
#         if amount > self.balance:
#             return "Balansda kifayət qədər pul yoxdur."
#         self.balance -= amount
#         self._add_transaction("Çıxarma", amount)
#         return f"${amount:.2f} çıxarıldı. {self.get_balance()}"

#     def get_transaction_history(self):
#         if not self.transaction_history:
#             return "Əməliyyat tarixçəsi boşdur."
#         history = "\n".join(self.transaction_history)
#         return f"Əməliyyat Tarixçəsi:\n{history}"

#     def _add_transaction(self, transaction_type, amount):
#         transaction = f"{transaction_type}: ${amount:.2f} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#         self.transaction_history.append(transaction)

#     def account_info(self):
#         return f"Hesab Sahibi: {self.account_holder}\n" + self.get_balance()

# account1 = BankAccount("Dalga Yunus", initial_balance=1200, interest_rate=0.03)

# print(account1.account_info())
# print(account1.deposit(200))
# print(account1.deposit(150))
# print(account1.apply_interest())
# print(account1.withdraw(100))
# print(account1.get_transaction_history())
# print(account1.get_balance())





# 2

# import datetime

# class FootballPlayer:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.goals = 0
#         self.assists = 0
#         self.yellow_cards = 0
#         self.red_cards = 0
#         self.matches_played = 2

#     def get_player_info(self):
#         return f"{self.name} ({self.position}) - Qollar: {self.goals}, Asistlər: {self.assists}, Sarı Kartlar: {self.yellow_cards}, Qırmızı Kartlar: {self.red_cards}, Oynadığı Oyunlar: {self.matches_played}"

#     def update_performance(self, goals, assists, yellow_cards, red_cards):
#         self.goals += goals
#         self.assists += assists
#         self.yellow_cards += yellow_cards
#         self.red_cards += red_cards
#         self.matches_played += 1

# class FootballTeam:
#     def __init__(self, team_name):
#         self.team_name = team_name
#         self.players = {}
#         self.matches = []
#         self.wins = 0
#         self.losses = 0
#         self.draws = 0
#         self.total_goals = 0

#     def add_player(self, player_name, position):
#         self.players[player_name] = FootballPlayer(player_name, position)
    
#     def add_player_performance(self, player_name, goals, assists, yellow_cards, red_cards):
#         if player_name in self.players:
#             self.players[player_name].update_performance(goals, assists, yellow_cards, red_cards)
#         else:
#             return f"Xəta: {player_name} komandada yoxdur."
    
#     def add_match(self, opponent_team, our_goals, opponent_goals):
#         match = {
#             'opponent': opponent_team,
#             'our_goals': our_goals,
#             'opponent_goals': opponent_goals,
#             'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         }
#         self.matches.append(match)
        
#         if our_goals > opponent_goals:
#             self.wins += 1
#         elif our_goals < opponent_goals:
#             self.losses += 1
#         else:
#             self.draws += 1
        
#         self.total_goals += our_goals
    
#     def get_team_statistics(self):
#         return f"Komanda adı: {self.team_name}\nQalibiyyətlər: {self.wins}\nMəğlubiyyətlər: {self.losses}\nBərabərliklər: {self.draws}\nCəmi qollar: {self.total_goals}"
    
#     def get_player_statistics(self, player_name):
#         if player_name in self.players:
#             return self.players[player_name].get_player_info()
#         else:
#             return f"Xəta: {player_name} komandada yoxdur."
    
#     def get_last_matches(self, num_matches=5):
#         last_matches = self.matches[-num_matches:]
#         result = "\n".join([f"Tarix: {match['date']} | Rəqib: {match['opponent']} | Bizim nəticə: {match['our_goals']} | Rəqibin nəticə: {match['opponent_goals']}" for match in last_matches])
#         return f"Son {num_matches} oyun:\n{result}"

# team = FootballTeam("Dalga FC")

# team.add_player("Osimhen", "Hücumçu")
# team.add_player("Sanchez", "Müdafiəçi")
# team.add_player("Muslera", "Qapıçı")

# team.add_player_performance("Osimhen", goals=2, assists=1, yellow_cards=1, red_cards=0)
# team.add_player_performance("Sanchez", goals=0, assists=0, yellow_cards=0, red_cards=0)
# team.add_player_performance("Muslera", goals=0, assists=0, yellow_cards=0, red_cards=0)

# team.add_match("Qarabağ", our_goals=2, opponent_goals=1)
# team.add_match("Neftçi", our_goals=1, opponent_goals=1)
# team.add_match("Sumqayit", our_goals=3, opponent_goals=0)

# print(team.get_team_statistics())

# print(team.get_player_statistics("Osimhen"))
# print(team.get_player_statistics("Sanchez"))
# print(team.get_player_statistics("Muslera"))

# print(team.get_last_matches(3))