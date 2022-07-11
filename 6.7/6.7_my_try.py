# Crushed it!! wow!!

def look_and_say(n):
    arr = ["1"]

    for i in range(n):
        val = arr[i][0]
        count = 0
        idx = 0

        str_add = ""
        while idx < len(arr[i]):

            if arr[i][idx] == val:
                count += 1
            else:
                str_add += str(count) + str(val)
                val = arr[i][idx]
                count = 1
            idx += 1

        str_add += str(count) + str(val)
        arr.append(str_add)
        print(arr)

look_and_say(6)