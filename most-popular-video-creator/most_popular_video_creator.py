from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        cMostPoplarLookup = dict()
        cViewCount = defaultdict(lambda: 0)
        for creator, id, viewCount in zip(creators, ids, views):
            mostPopular = None
            if creator in cMostPoplarLookup:
                mostPopular = cMostPoplarLookup[creator]
            if mostPopular == None:
                mostPopular = (id, viewCount)
            else:
                existing_id, existing_viewCount = mostPopular
                if existing_viewCount < viewCount:
                    mostPopular = (id, viewCount)
                elif existing_viewCount == viewCount and id < existing_id:
                    mostPopular = (id, viewCount)
            cMostPoplarLookup[creator] = mostPopular
            cViewCount[creator] += viewCount
    
        max_views = max(cViewCount.values())
        max_creators = [creator for creator,viewCount in cViewCount.items() if viewCount == max_views]
        result = []
        for c in max_creators:
            result.append([c, cMostPoplarLookup[c][0]])
        return result
