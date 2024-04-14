class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        oa:int = 0 # original_array
        _ma:int = 0 # maximun_attitiude
        for i in gain:
            oa = oa + i # new_element
            if(oa > _ma):
                _ma = oa
        return _ma
        