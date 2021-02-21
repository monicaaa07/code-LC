def twoSum(self, nums: List[int], target: int) -> List[int]:
      orig = nums.copy()
      nums.sort()
      first,last = 0,len(nums) - 1
      while last > first:
          this_sum = nums[last] + nums[first]
          if this_sum < target:
              first = first + 1
          elif this_sum > target:
              last = last - 1
          else:
              return_val = []
              for i,ele in enumerate(orig):
                  if ele == nums[first]:
                      return_val.append(i)
                  elif ele == nums[last]:
                      return_val.append(i)
              return return_val

            
