
import math
def solution(character, monsters):
    answer = ""
    p_a,p_b,p_c = list(map(int,character.split()))

    exe = 0
    sec_exe = 0
    
    for monster in monsters:
        monster_list = monster.split()
        m_a = monster_list[0]
        m_b,m_c,m_d,m_e = list(map(int,monster_list[1:]))

        player_damage = max(0,p_b - m_e)
        monster_damage = max(0,m_d - p_c)

        
        if m_c - player_damage <= 0:
            if sec_exe < m_b:
                answer = m_a
                sec_exe = m_b
                exe = m_b
            elif sec_exe == m_b:
                if exe < m_b:
                    answer = m_a
                    exe = m_b     
            continue

        if p_a - monster_damage <= 0:
            if answer == "":
                answer = m_a
            continue
        if player_damage == 0 :continue

        cnt = math.ceil(m_c/player_damage)
        curr_exe = (m_b/cnt)
        if sec_exe < curr_exe:
            answer = m_a
            sec_exe = curr_exe
            exe = m_b
        elif sec_exe == curr_exe:
            if exe < m_b:
                answer = m_a
                exe = m_b
    
    return answer

print(solution("10 5 2",["Knight 5 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]))