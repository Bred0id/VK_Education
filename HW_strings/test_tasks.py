import pytest
from task208 import Trie
from task211 import WordDictionary
from task212 import WordSearchII

def test_task208_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

def test_task211_word_dictionary():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("b...") is False

def test_task212_word_search_ii():
    solver = WordSearchII()
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    result1 = solver.findWords(board1, words1)
    assert sorted(result1) == ["eat","oath"]

    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    assert solver.findWords(board2, words2) == []

if __name__ == "__main__":
    pytest.main(["-v"])