#pragma once

#include "algorithms.h"
#include <ctime>

void TimeMeasureThreads(int start, int n_threads, int iters);
void TimeMeasureLength(int start, int max_len, int step, int iters);