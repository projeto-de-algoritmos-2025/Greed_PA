class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0  # último índice

        jumps = 0  # Contador de saltos
        max_reach = 0  # Alcance máximo possível no momento
        end_of_jump = 0  # Fim do alcance do pulo atual

        for i in range(n - 1):  # Não precisa considerar o último índice
            max_reach = max(max_reach, i + nums[i])  # Atualiza alcance máximo

            #novo salto
            if i == end_of_jump:
                jumps += 1
                end_of_jump = max_reach

                if end_of_jump >= n - 1:
                    break

        return jumps
