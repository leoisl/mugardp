import random


def error_out():
    raise ValueError("Da mais nao mano, nao consigo mais fazer time")


def get_sample_with_unique_players(box):
    for _ in range(1000):
        try:
            players = random.sample(box, 3)
            players_are_unique = len(set(players)) == 3
            if players_are_unique:
                return players
        except ValueError:
            error_out()
    error_out()


def remove_players_from_box(box, players):
    for player in players:
        box.remove(player)


def draw(forwards_box, midfielders_box):
    forwards = get_sample_with_unique_players(forwards_box)
    midfielders = get_sample_with_unique_players(midfielders_box)

    remove_players_from_box(forwards_box, forwards)
    remove_players_from_box(midfielders_box, midfielders)

    return forwards + midfielders

def output_games(original_forwards_box, original_midfielders_box, number_of_draws):
    forwards_box = list(original_forwards_box)
    midfielders_box = list(original_midfielders_box)
    for draw_index in range(number_of_draws):
        game = draw(forwards_box, midfielders_box)
        print(f"Jogo #{draw_index + 1} = {game}")


def main():
    forwards_box = []
    midfielders_box = []
    while True:
        nome = input("Nome do jogador (Fim para terminar)? ")
        if nome.lower()=="fim":
            break
        frequencia = int(input("Frequencia? "))
        tipo = input("Tipo (A=atacante, M=meia)? ").upper()
        assert tipo in "AM"

        box = forwards_box if tipo=="A" else midfielders_box
        box.extend([nome]*frequencia)

    while True:
        number_of_draws = input("Nova draw, quantos jogos quer (Fim para terminar)? ")
        if number_of_draws.lower() == "fim":
            break
        number_of_draws = int(number_of_draws)
        try:
            output_games(forwards_box, midfielders_box, number_of_draws)
        except ValueError:
            print("Nao consigo mais fazer jogos.")
            pass

main()
