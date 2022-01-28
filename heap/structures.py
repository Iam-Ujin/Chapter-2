class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 인덱스는 1부터 / 0번째 요소를 None으로
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직메서드
        # 첫번째 요소를 제외하기 위해 - 1
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다
        # 전체길이
        cur = len(self)
        # left라면 2*cur, right라면 cur*2+1 이므로 parent는 항상 cur // 2
        parent = cur // 2

        # 현재 요소의 값이 부모 요소의 값보다 크다면 위치 변경
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            # 부모요소를 현재요소로 선언 후 반복
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1
        # 왼쪽이 범위 안에 있고 부모보다 크다면 좌표값을 변경
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left
        # 오른쪽이 범위 안에 있고 부모보다 크다면 좌표값을 변경
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            # 값만 주고 받았고 자식요소 중 가장 큰 요소의 인덱스가 biggest임! 헷갈리지 말기
            self._percolate_down(biggest)

    def insert(self, k):
        # 삽입
        self.items.append(k)
        # 부모 노드와 비교해서 자리 이동
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        # 루트와 마지막 요소 위치 변경
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root