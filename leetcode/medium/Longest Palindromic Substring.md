> 풀이 날짜 : 2024.01.11  
> 문제 유형 : String, Dynamic Programming  
> 문제 제목 : Longest Palindromic Substring  
> 문제 링크 : https://leetcode.com/problems/longest-palindromic-substring/

### Intuition


### Approach
- 다이나믹 프로그래밍을 사용하여 중복 계산 최소화. 작은 부분 문제들의 해결을 통해 전체 문제를 해결한다.
  - 부분 문제 정의
    - dp[i][j]는 부분 문제로, 문자열 s의 인덱스 i부터 j까지의 부분 문자열이 팰린드롬인지 여부를 나타냄
  - 초기 조건 설정:
    - 길이가 1인 모든 부분 문자열은 팰린드롬이므로 dp[i][i]를 모두 true로 초기화
  - 최소 부분 문제에서 최종 문제로
    - 길이가 2인 부분 문자열에 대해서도 팰린드롬 여부를 미리 계산하고 초기화
  - 점화식(Recurrence Relation)
    - 길이가 3 이상인 부분 문자열에 대해서는 dp[i + 1][j - 1] 값과 문자열 양 끝이 같은지(s[i] === s[j]) 여부를 확인하여 부분 문자열이 팰린드롬인지 결정
  - 최적 부분 구조(Optimal Substructure):
    - 큰 문제를 작은 부분 문제로 나누어 해결하고, 이를 조합하여 최종적인 해를 얻는다.

### Complexity
- Time complexity: O(N^2)
  - 가장 길이가 1인 부분 문자열에 대한 초기화: O(n) 
  - 가장 길이가 2인 부분 문자열에 대한 초기화: O(n)
  - 길이가 3 이상인 부분 문자열의 팰린드롬 검사할 때 중첩 반복문 사용되므로 O(N^2) 
- Space complexity: O(N^2)
  - dp 배열: O(n^2)  
  - 상수 개의 변수(start, maxLength)와 임시 변수들: O(1)

### Code
```javascript
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    // dp[i][j]는 문자열 s의 인덱스 i부터 j까지의 부분 문자열이 팰린드롬인지 여부를 저장
    const dp = Array(s.length).fill(0).map(() => Array(s.length).fill(false));
    let start = 0; // 가장 긴 팰린드롬의 시작 인덱스
    let maxLength = 1; // 가장 긴 팰린드롬의 길이

    // 모든 길이가 1인 부분 문자열은 팰린드롬
    for (let i = 0; i < s.length; i++) {
        dp[i][i] = true;
    }

    // 길이가 2인 부분 문자열 중 팰린드롬인 경우 처리
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }

    // 길이가 3 이상인 팰린드롬 처리
    for (let len = 3; len <= s.length; len++) {
        // i: 부분 문자열의 시작 인덱스, j: 부분 문자열의 마지막 인덱스
        for (let i = 0; i <= s.length - len; i++) {
            let j = i + len - 1;
            // 부분 문자열의 양 끝이 같고, 그 사이 부분 문자열이 팰린드롬일 때
            if (dp[i + 1][j - 1] && s[i] === s[j]) {
                // i~j 인덱스가 팰린드롬
                dp[i][j] = true;
                // 최대 팰린드롬의 시작인덱스 갱신
                start = i;
                // 최대 팰린드롬의 길이 갱신
                maxLength = len;
            }
        }
    }

    // 가장 긴 팰린드롬 부분 문자열 반환
    return s.substring(start, start + maxLength);
};
```