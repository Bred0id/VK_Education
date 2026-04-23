class WordSearchII:
    def findWords(self, board, words):
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word

        rows, cols = len(board), len(board[0])
        result = []

        def backtrack(r, c, parent):
            letter = board[r][c]
            curr_node = parent.get(letter)
            if not curr_node:
                return

            if '#' in curr_node:
                result.append(curr_node['#'])
                del curr_node['#']

            board[r][c] = '#'
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    backtrack(nr, nc, curr_node)
            board[r][c] = letter

            if not curr_node:
                parent.pop(letter)

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, root)
        return result