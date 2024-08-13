#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
print("------------------------------------------------------------")
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
print("------------------------------------------------------------")
print("")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print("------------------------------------------------------------")
print("")

print("Edge Cases")
boxes = [[]]
print(boxes)
print(canUnlockAll(boxes), "expected=> True")
print("------------------------------------------------------------")
print("")

boxes = []
print(boxes)
print(canUnlockAll(boxes), "expected=> True")
print("------------------------------------------------------------")
print("")

boxes = [[1, 2, 3, 4], [], [], [], []]
print(boxes)
print(canUnlockAll(boxes), "expected=> True")
print("------------------------------------------------------------")
print("")

boxes = [[1], [2], [0], []]
print(boxes)
print(canUnlockAll(boxes), "expected=> False")
print("------------------------------------------------------------")
print("")

boxes = [[1], [2], [4], [], [5]]
print(boxes)
print(canUnlockAll(boxes), "expected=> False")
print("------------------------------------------------------------")
print("")

boxes = [[1, 1], [2, 2], [3, 3], []]
print(boxes)
print(canUnlockAll(boxes), "expected=> True")
print("------------------------------------------------------------")
print("")

boxes = [[1, 2, 5], [], [], []]
print(boxes)
print(canUnlockAll(boxes), "expected=> False")
print("------------------------------------------------------------")
print("")

