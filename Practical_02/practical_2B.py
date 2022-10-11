pass_stats = 0.15
pass_coding_with_stats = 0.60   #pass_coding_With_Stats
pass_coding_without_stats = 0.40
p_both = pass_stats * pass_coding_with_stats
p_coding = p_both + ((1-pass_stats)*pass_coding_without_stats)

stats_given_coding = p_both /p_coding
print(stats_given_coding)
