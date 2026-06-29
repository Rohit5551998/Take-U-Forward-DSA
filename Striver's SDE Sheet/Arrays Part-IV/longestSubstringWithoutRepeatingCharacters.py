# QUESTION: Longest Substring Without Repeating Characters
# Given a string, S. Find the length of the longest substring without repeating characters.


"""
#Brute Force:
1. We don't know where the longest repeat-free substring starts, so try every
   start i and grow the substring rightward with j.
2. For each start i, use a fresh 256-slot seen-array (one entry per ASCII char)
   reset to -1, so it only tracks characters inside the CURRENT window [i..j].
3. Extend j: if s[j] was already marked seen in this window, a repeat would form,
   so stop this start (break) — the window can't grow further from i.
4. Otherwise mark s[j] as seen and update maxLen with the window length j - i + 1.
5. Restart from the next i. The reset-per-start + inner expansion is the cost.
TC -> O(n^2), SC -> O(256) ~ O(1)

#Better Approach:
1. Same sliding-window idea as the optimal, with a hashMap of each char's LAST-seen
   index — but instead of jumping left in one step, walk it forward one position at a time.
2. Move right across the string. For char = s[right], shrink with an inner loop:
   while char was seen before AND its last index is still inside the window
   (left < hashMap[char] + 1), do left += 1, advancing past the old occurrence.
3. The guard left < hashMap[char] + 1 does double duty: it detects the in-window
   duplicate and stops the moment left passes it. A stale occurrence sitting BEFORE
   left fails the guard, so the inner loop doesn't run (left never rewinds).
4. Record hashMap[char] = right, then update maxLen with right - left + 1.
5. left only ever moves forward and is capped at len(s), so the inner increments
   total <= n across the WHOLE run — amortized linear, same big-O as the optimal.
   The only difference: left takes single steps (up to ~2n pointer moves) instead
   of one O(1) jump, so the optimal wins on constant factor, not asymptotics.
TC -> O(n) amortized (O(2n)), SC -> O(min(n, 256))

#Optimal Approach:
1. Keep a sliding window [left, right] that is always repeat-free, and a hashMap
   storing the LAST index at which each character was seen.
2. Move right across the string one char at a time. Look up char = s[right].
3. If char was seen before AND its last position is inside the current window
   (i.e. >= left), it would duplicate, so jump left just past that position:
   left = max(left, hashMap[char] + 1). The max(...) guard is essential — a stale
   occurrence sitting BEFORE left must NOT drag left backwards.
4. Record/overwrite hashMap[char] = right as the newest position of this char.
5. The window [left..right] is now repeat-free, so update maxLen with right-left+1.
6. Each index is visited once by right and left never moves back, so it's a single
   linear pass — far better than the brute's restart-per-start.
TC -> O(n), SC -> O(min(n, 256))

#KEY INSIGHT:
- Storing each char's LAST-seen index lets left jump directly past a duplicate in
  O(1) instead of shrinking one step at a time. The max(left, hashMap[char] + 1)
  guard prevents an out-of-window earlier occurrence from rewinding left — that
  single guard is what makes the one-pass window correct.
"""


class Solution:
    def longest_substring_without_repeating_characters_brute(self, s: str) -> int:
        maxLen = 0
        for i in range(0, len(s)):
            hashMap = [-1 for _ in range(0, 256)]
            for j in range(i, len(s)):
                if hashMap[ord(s[j])] != -1:
                    break

                hashMap[ord(s[j])] = 1

                maxLen = max(maxLen, j - i + 1)

        return maxLen

    def longest_substring_without_repeating_characters_better(self, s: str) -> int:
        maxLen = 0
        hashMap = {}
        left = 0
        right = 0

        while right < len(s):
            char = ord(s[right])

            # Walk left forward one step at a time until the window is repeat-free.
            # The guard left < hashMap[char] + 1 detects an in-window duplicate and
            # stops once left passes it; a stale occurrence BEFORE left fails the
            # guard, so the loop doesn't run and left never rewinds.
            while char in hashMap and left < hashMap[char] + 1:
                left += 1

            hashMap[char] = right

            maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen

    def longest_substring_without_repeating_characters_optimal(self, s: str) -> int:
        maxLen = 0
        hashMap = {}
        left = 0
        right = 0

        while right < len(s):
            char = ord(s[right])

            # If this char was seen before, jump left just past its last position so
            # the window stays repeat-free. max(...) guards against a stale occurrence
            # that lies BEFORE left — it must not drag left backwards.
            # (Equivalent explicit form: if char in hashMap and left < hashMap[char] + 1:
            #     left = hashMap[char] + 1)
            if char in hashMap:
                left = max(left, hashMap[char] + 1)

            hashMap[char] = right

            maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen


if __name__ == "__main__":
    sol = Solution()
    string = "abcabcbb"
    print(sol.longest_substring_without_repeating_characters_brute(string))
    string = "abcabcbb"
    print(sol.longest_substring_without_repeating_characters_better(string))
    string = "abcabcbb"
    print(sol.longest_substring_without_repeating_characters_optimal(string))
