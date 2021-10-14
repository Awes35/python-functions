#author Kollen Gruizenga
#recursive function to take string S and int N, return
#string S repeated N times

def repeatNTimes(S, N):
    if N == 0:
        return ''
    else:
        return S + repeatNTimes(S, N-1)

