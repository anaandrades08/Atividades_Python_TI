class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_towards_player(self, player_x, player_y):
        # Calcula a direção para o jogador
        if player_x > self.x:
            self.x += 1
        elif player_x < self.x:
            self.x -= 1

        if player_y > self.y:
            self.y += 1
        elif player_y < self.y:
            self.y -= 1

# Criação de um NPC e um jogador
npc = NPC(5, 5)
player_x, player_y = 10, 10

# Movimento do NPC em direção ao jogador
npc.move_towards_player(player_x, player_y)
print(f"Nova posição do NPC: ({npc.x}, {npc.y})")
