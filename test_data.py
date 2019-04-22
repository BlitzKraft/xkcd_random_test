import random
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt # pylint: disable=C0413

# number of comics read per week
READ_COMICS = 400

# number of comics released per week
RELEASED_COMICS = 3

START = 1700
END = 2140

# number of additional iterations after latest comic
TAIL_ITERS = 1

def get_week(start=START, count_dict={}): # pylint: disable=W0102
    sample = random.sample(range(1, start), READ_COMICS)
    # For testing wiht shuffle instead of choosing randomly
    # sample = list(range(1, start))
    # random.shuffle(sample)
    # sample = sample[:READ_COMICS]
    for index in sample:
        count = count_dict.get(index, 0)
        count_dict.update({index: count + 1})
    if start < END:
        start += RELEASED_COMICS
        get_week(start, count_dict)
    else:
        for _ in range(0, TAIL_ITERS):
            sample = random.sample(range(1, start), READ_COMICS)
            for index in sample:
                count = count_dict.get(index, 0)
                count_dict.update({index: count + 1})
    return count_dict


def draw_graph(count):
    # for trimming the results to only after a certain comic index
    cur = 0
    keylist = list(count.keys())
    keylist.sort()
    plt.xkcd()
    plt.figure(figsize=(12, 6), dpi=100)
    plt.xlabel("Comic index")
    plt.ylabel("Number of views")
    run_len = range(cur, max(keylist))
    plt.scatter(run_len, [count.get(i, 0) for i in run_len])
    plt.savefig('graph.png')

COUNTS_PER_COMIC = get_week()
draw_graph(COUNTS_PER_COMIC)
