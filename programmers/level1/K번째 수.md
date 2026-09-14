> 풀이 날짜 : 2026.06.23  
> 문제 유형 : 정렬  
> 문제 제목 : 째 수  
> 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

<br>

### Intuition

---

- 각 command는 배열의 `i`번째부터 `j`번째까지 자른 뒤, 정렬했을 때 `k`번째 수를 구하라는 의미이다.
- 문제에서 주어지는 `i`, `j`, `k`는 1-based index이므로 Java 배열에서 사용할 때는 `i - 1`, `k - 1`로 변환해야 한다.
- 각 command는 서로 독립적이므로, 매번 필요한 구간만 복사해서 정렬하면 된다.
- `array`의 길이는 최대 `100`, `commands`의 길이는 최대 `50`이므로 구간 복사와 정렬을 반복하는 방식으로 충분히 해결할 수 있다.

<br>

### Approach

---

- 정답을 저장할 `List<Integer>`를 만든다.
- `commands`를 하나씩 순회하면서 `i`, `j`, `k`를 꺼낸다.
- `Arrays.copyOfRange(array, i - 1, j)`를 사용해 `i`번째부터 `j`번째까지의 구간을 복사한다.
  - `copyOfRange`의 시작 인덱스는 포함되고, 끝 인덱스는 포함되지 않는다.
  - 문제의 `j`는 1-based index이므로 그대로 넘기면 Java 기준으로 원하는 끝 위치 다음 인덱스가 된다.
- 복사한 배열을 `Arrays.sort()`로 오름차순 정렬한다.
- 정렬된 배열에서 `k - 1`번째 값을 정답 리스트에 추가한다.
- 모든 command를 처리한 뒤 `int[]`로 변환해 반환한다.

<br>

### Complexity

---

- Time complexity: `O(n * m log m)`
  - `commands`의 길이를 `n`, command에서 잘라내는 구간의 최대 길이를 `m`이라고 하자.
  - command 하나를 처리할 때 최대 `m`개의 원소를 복사하므로 `O(m)`이 걸린다.
  - 복사한 배열을 `Arrays.sort()`로 정렬하는 데 `O(m log m)`이 걸린다.
  - command 하나의 비용은 `O(m + m log m)`이고, 더 큰 항만 남기면 `O(m log m)`이다.
  - 이를 `commands`의 길이 `n`번 반복하므로 전체 시간 복잡도는 `O(n * m log m)`이다.

- Space complexity: `O(n + m)`
  - command마다 최대 길이 `m`의 부분 배열을 새로 만든다.
  - 현재 풀이는 정답을 `List<Integer>`에 저장한 뒤 배열로 변환하므로 정답 저장 공간 `n`도 사용한다.

<br>

### Code (Java)

---

```java
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answers = new ArrayList<>();

        for (int[] command: commands) {
            int i = command[0];
            int j = command[1];
            int k = command[2];

            int[] ranged = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(ranged);
            int answer = ranged[k-1];

            answers.add(answer);
        }

        return answers.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}
```

<br>

### Code (C++)

---

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (vector<int> command : commands) {
        int i = command[0];
        int j = command[1];
        int k = command[2];

        auto start = array.begin() + i - 1;
        auto end = array.begin() + j;

        vector<int> sliced(start, end);

        sort(sliced.begin(), sliced.end());

        answer.push_back(sliced[k-1]);
    }

    return answer;
}
```

- `vector<int>`는 크기가 변하는 정수 배열이다. `push_back()`으로 각 명령의 결과를 `answer` 뒤에 추가한다.
- `begin()`은 벡터의 첫 원소를 가리키는 반복자를 반환한다. 반복자에 `i - 1`과 `j`를 더해 복사할 구간의 시작과 끝을 정한다.
- `vector<int> sliced(start, end)`는 `[start, end)` 범위의 원소를 복사해 새 벡터를 만든다.
- `<algorithm>`의 `sort()`는 반복자 범위를 오름차순으로 정렬한다.
- `auto`를 사용하면 `start`와 `end`의 반복자 타입을 컴파일러가 추론한다.
