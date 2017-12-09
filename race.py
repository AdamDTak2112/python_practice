import math;

def race(v1, v2, g):
    if (v1 >= v2):
        return;

    catchRate = v2 - v1;
    catchTime = catchRate / g;

    totalSeconds = catchTime * 60 * 60;
    seconds = totalSeconds % 60;
    totalMinutes = totalSeconds / 60;
    minutes = totalMinutes % 60;
    hours = totalMinutes / 60;

    return [math.floor(hours), math.floor(minutes), math.floor(seconds)];