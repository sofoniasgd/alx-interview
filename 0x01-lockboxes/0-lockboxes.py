#!/usr/bin/python3
""" 0. Lockboxes """


def canUnlockAll(boxes):
    """ A method that determines if all the boxes can be opened
        You have n number of locked boxes in front of you. Each box
        is numbered sequentially from 0 to n - 1 and each box may contain
        keys to the other boxes.
        Args:
            boxes: list of lists
        Properties: A key with the same number as a box opens that box
                You can assume all keys will be positive integers
                There can be keys that do not have boxes
                The first box boxes[0] is unlocked
        Return True if all boxes can be opened, else return False
    """

    keys_list = []
    keys_list.append(0)
    temp_list = []

    # empty list
    if boxes == []:
        return True
    # get key/s in boxes[0] since its unlocked
    for key in boxes[0]:
        if key not in keys_list and key < len(boxes):
            keys_list.append(key)
    # now unlock boxes of which we have keys
    for key in keys_list:
        if key >= len(boxes):
            continue
        else:
            temp_list = boxes[key]
        for unlock_key in temp_list:
            if unlock_key not in keys_list and unlock_key < len(boxes):
                keys_list.append(unlock_key)
    # print("length of keys_list=", len(keys_list))
    # print(keys_list)
    # print("length of box list=", len(boxes))
    # print(boxes)

    # return if number of keys is equal to boxes length
    return (len(keys_list) == len(boxes))
