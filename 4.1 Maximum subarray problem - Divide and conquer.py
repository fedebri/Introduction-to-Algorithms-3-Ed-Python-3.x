def findmax_xsubarray (array, low, mid, high):

    left_sm = -1000
    sm = 0
    max_left = 0
    for i in range (mid, low-1, -1):
        sm += array[i]
        if sm > left_sm:
            left_sm = sm
            max_left = i
            #print('max_left:', max_left)

    right_sm = -1000
    sm = 0
    max_right = 0
    for j in range(mid+1, high+1):
        sm += array[j]
        if sm > right_sm:
            right_sm = sm
            max_right = j
            #print('max_right:', max_right)

    #print ('max_left:',max_left, 'max_right:',max_right, 'left_sm+right_sm:', left_sm+right_sm)
    return (max_left, max_right, left_sm+right_sm)
    

def findmax_subarray (array, low, high):
    #Returns both the lowest and the highest index of the max subarray and the sum of the values in the subarray

    if high == low:
        return (low, high, array[low])

    else:
        mid = int((high+low)/2)

        left_low, left_high, left_sm = findmax_subarray(array, low, mid)
        #print ('left_low:', left_low, 'left_high:', left_high,'left_sm:', left_sm) 

        right_low, right_high, right_sm = findmax_subarray(array, mid+1, high)
        #print('right_low:', right_low, 'right_high:', right_high, 'right_sm:', right_sm)

        x_low, x_high, x_sm = findmax_xsubarray(array, low, mid, high)
        #print('x_low:', x_low, 'x_high:', x_high, 'x_sm:', x_sm)

        if left_sm > right_sm and left_sm > x_sm:
            return (left_low, left_high, left_sm)
        elif right_sm > left_sm and right_sm > x_sm:
            return (right_low, right_high, right_sm)
        else:
            return (x_low, x_high, x_sm)
