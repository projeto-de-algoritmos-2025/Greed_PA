import heapq

class Solution:
    def scheduleCourse(self, courses):
        # Ordena os cursos pelo último dia em que podem ser finalizados
        courses.sort(key=lambda x: x[1])

        total_time = 0
        max_heap = []

        for duration, lastDay in courses:
            # Adiciona a duração (negativa) do curso no heap máximo
            heapq.heappush(max_heap, -duration)
            total_time += duration

            # Se o tempo total exceder o limite, remove o curso mais longo
            if total_time > lastDay:
                total_time += heapq.heappop(max_heap)  # valor negativo compensa

        return len(max_heap)
    