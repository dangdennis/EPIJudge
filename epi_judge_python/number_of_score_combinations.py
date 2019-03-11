from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # TODO - you fill in here.
    # print('final score', final_score)
    # print('individual_play_scores', individual_play_scores)
    num_combinations_for_score = [[1] + [0] *
                                  final_score for _ in individual_play_scores]
    # print('num_combinations_for_score',num_combinations_for_score)

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (
                num_combinations_for_score[i-1][j] if i >= 1 else 0)
            # print('without_this_play', without_this_play)
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)

            # print('with_this_play', with_this_play)
            num_combinations_for_score[i][j] = (
                without_this_play + with_this_play)

    # print('num_combinations_for_score', num_combinations_for_score)
    return num_combinations_for_score[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
