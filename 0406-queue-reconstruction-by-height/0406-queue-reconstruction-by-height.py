from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_dict = defaultdict(list)
        for height, front in people:
            people_dict[height].append(front)

        heights = sorted(people_dict.keys())
        rem_indices = [i for i in range(len(people))]
        results = [None] * len(people)

        for h in heights:
            chosen_indices = []
            for front in people_dict[h]:
                results[rem_indices[front]] = [h, front]
                chosen_indices.append(rem_indices[front])
            rem_indices = sorted(list(set(rem_indices) - set(chosen_indices)))
            


        return results
                